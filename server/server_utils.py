import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dominate import document
from dominate.tags import *
from string import Template


URL = '161.35.20.108'


def generate_table(agents, items, data, file_name):
    with document() as doc:
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

    with open('/var/www/html/fairness-algorithm-rest/web/generated_html/{}.html'.format(file_name), 'w') as f:
        f.write(doc.render())
    return '{}/generated_html/{}.html'.format(URL, file_name)


def send_email(email_receiver, url):
    sender_email = "fairnessalgorithm.io@gmail.com"
    receiver_email = email_receiver
    password = ''

    message = MIMEMultipart("alternative")
    message["Subject"] = "Fairness.io Results"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message

    with open('/var/www/html/fairness-algorithm-rest/web/html_email_template.html', 'r+') as f:
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



