import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dominate import document
from dominate.tags import *
from string import Template
import numpy as np


"""
generate HTML file that represent the algorithm results.
and save the HTML with unique identifier in the generated_html folder.
:param agents represent the agents names list (str list)
:param items represent the items names list (str list)
:param data represent the Algorithm results as numpy.np
:param file_name represent the output file name (unique identifier)
"""


def generate_table(agents, items, data, file_name, data_json):
    with document(title='Algorithm Results') as doc:
        head_page = head()
        head_page += link(rel='shortcut icon', href="../images/web-logo.png")
        head_page += link(rel="stylesheet", type="text/css", href="../css/Home.css")
        head_page += link(href="https://fonts.googleapis.com/css2?family=Special+Elite&display=swap", rel="stylesheet")
        head_page += link(href="https://fonts.googleapis.com/css2?family=Permanent+Marker&display=swap",
                          rel="stylesheet")
        link(rel="stylesheet", href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css",
             integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm",
             crossorigin="anonymous")
        link(rel="stylesheet", type="text/css", href="../css/styles.css")
        content_div = div(cls='topnav')
        content_div += a('Home', cls='active', href='../Home.html')
        content_div += a('About Us', cls='active', href='../About_Us.html')
        content_div += a('Contact us', cls='active', href='../Contact_Us.html')

        h1('Results', cls='header')

        result_table = table(cls='content-table')
        link(rel='stylesheet', href='../css/table.css')
        header_thread = thead()
        header_tr = tr()
        header_tr += th('Items')
        for agent in agents:
            header_tr += th(agent)
        header_thread += header_tr

        item_index = 0

        thread_body = tbody()
        for item in items:
            item_tr = tr()
            item_tr += th(item)
            for score in [z[item_index] for z in data[0:]]:
                item_tr += td('{} %'.format(score))
            item_index += 1
            thread_body += item_tr

        result_table += header_thread
        result_table += thread_body

        if data_json['problem'] == 'EnvyFree':
            explanations = build_envy_free_output(data, data_json)
        elif data_json['problem'] == 'Proportional':
            explanations = build_proportional_output(data, data_json)

        h1('Results Explanation', cls='header')

        result_explanation_table = table(cls='content-table')
        thread_body = tbody()
        for index, explanation in enumerate(explanations):
            item_tr = tr()
            item_tr += th(agents[index])
            item_tr += td(explanation)
            thread_body += item_tr
        result_explanation_table += thread_body

    with open('web/generated_html/{}.html'.format(file_name), 'w') as f:
        f.write(doc.render())

    with open('web/generated_html/{}.html'.format(file_name), 'r') as f:
        file_data = f.read()

    # Replace the target string
    file_data = file_data.replace('&lt;br&gt;', '<br>')

    # Write the file out again
    with open('web/generated_html/{}.html'.format(file_name), 'w') as f:
        f.write(file_data)

    print('generated url is {}'.format(file_name))
    return '/generated_html/{}.html'.format(file_name)


"""
sending email with the algorithm results.
:param email_receiver is a valid email of the receiver of the results
:param url represent the site url that contain the algorithm results
"""


def send_email(email_receiver, url):
    print('send email to: {}'.format(email_receiver))
    sender_email = os.environ.get('EMAIL', None)
    receiver_email = email_receiver
    password = os.environ.get('EMAIL_PASSWORD', None)

    if (password or sender_email) is None:
        print('EMAIL or EMAIL_PASSWORD is None , Please check HeroKu ENV')

    message = MIMEMultipart("alternative")
    message["Subject"] = "Fairness.io Results"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message

    with open('web/html_email_template.html', 'r+') as f:
        template = Template(f.read())
        html = (template.substitute(URL=url))

    # Turn these into plain/html MIMEText objects
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )


"""
build proportional explanation with the algorithm results for each user.
:param results represent the proportional algorithm results
:param data represent the JSON data as described in README file
"""


def build_proportional_output(results, data):
    points_per_item = np.array(results) * np.array(data['values'])
    agents_results = [sum(e) for e in points_per_item]
    explanation = []
    for index, agent_result in enumerate(agents_results):
        explanation.append(
            'Hey {}, The total value of the items you received, according to your evaluation, is {} points.{}' \
            'This is at least 1/{} of the total value of your rates which is {}.'.format(
                data['agents'][index], agent_result, '<br>', len(agents_results), 100))
    return explanation


"""
build envy-free explanation with the algorithm results for each user.
:param results represent the proportional algorithm results
:param data represent the JSON data as described in README file
"""


def build_envy_free_output(results, data):
    explanation = []
    for agent_index, agent in enumerate(data['agents']):

        results_per_agent_index = np.array(results) * np.array(data['values'][agent_index])
        agents_results = [sum(e) for e in results_per_agent_index]
        explanation_per_agent = 'Hey {}, The total value of the items you received, according to your evaluation  ' \
                                'is {} points. {} according to your evaluation: '.format(agent,
                                                                                         agents_results[agent_index],
                                                                                         '<br>')

        for other_agent_index, other_agent in enumerate(data['agents']):
            if agent_index != other_agent_index:
                explanation_per_agent += '{} got {} points .'.format(other_agent,
                                                                     agents_results[other_agent_index])
        explanation_per_agent += '{} but according to your evaluation you got {} points, which is the best result ' \
                                 'according to your evaluation '.format('<br>', agents_results[agent_index])
        explanation.append(explanation_per_agent)
    return explanation
