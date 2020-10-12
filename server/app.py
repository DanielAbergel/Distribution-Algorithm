import numpy as np
import sys
from _sha256 import sha256
from threading import Thread
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dominate import document
from dominate.tags import *
from string import Template

sys.path.append('../')
from flask import Flask, request, render_template, jsonify, send_from_directory
from flask_restful import Resource, Api, reqparse
from algorithm.Version3.FairEnvyFreeAllocationProblem import FairEnvyFreeAllocationProblem
from algorithm.Version3.FairProportionalAllocationProblem import FairProportionalAllocationProblem

app = Flask(__name__)
api = Api(app)
URL = '161.35.20.108'


@app.route('/')
def home():
    return send_from_directory('../web/', 'Home.html')


@app.route('/<string:html>')
def send_html(html):
    return send_from_directory('../web/', html)


@app.route('/DOM/<string:dom>')
def send_dom(dom):
    return send_from_directory('../web/DOM', dom)


@app.route('/css/<string:css>')
def send_css(css):
    return send_from_directory('../web/css', css)


@app.route('/images/<string:image>')
def send_images(image):
    return send_from_directory('../web/images', image)


@app.route('/generated_html/<string:data>')
def build_result(data):
    return send_from_directory('../web/generated_html/', data)


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


def long_time_algorithm(data):
    result = run_algorithm(data)
    url = generate_table(agents=data['agents'], items=data['items'],
                         data=result, file_name=sha256(str(data['values']).encode('utf-8')).hexdigest())
    send_email(data['email'], url)


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


def run_algorithm(data):
    matrix = np.array(data['values'])
    if data['problem'] == 'EnvyFree':
        ProblemObject = FairEnvyFreeAllocationProblem(matrix)
        ans = ProblemObject.find_allocation_with_min_shering()
        print('Using EnvyFree Algorithm')
    elif data['problem'] == 'Proportional':
        ProblemObject = FairProportionalAllocationProblem(matrix)
        ans = ProblemObject.find_allocation_with_min_shering()
        print('Using Proportional Algorithm')
    return ans.tolist()


class Algorithm(Resource):

    def get(self):
        return {'algorithm': 'available'}

    def post(self):

        data = request.get_json()

        if int(data['num_of_agents']) > 3:

            thread = Thread(target=long_time_algorithm, args=(data,), daemon=True)
            thread.start()

            json_request = {
                'message': 'to many agents , the algorithm results will send by email.',
                'RESULT': 1
            }

            req = jsonify(json_request)
            req.status_code = 200
            print("starting algorithm with thread task...")
            return req

        else:

            result = run_algorithm(data)

            json_request = {
                'problem': data['problem'],
                'agents': data['agents'],
                'items': data['items'],
                'values': result
            }

            print(json_request)
            req = jsonify(json_request)
            req.status_code = 200
            print("done")
            return req


api.add_resource(Algorithm, '/calculator')

if __name__ == '__main__':
    app.run(debug=False, port=5000)
