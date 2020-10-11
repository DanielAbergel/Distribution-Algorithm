import numpy as np
import sys
from threading import Thread
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

sys.path.append('../')
from flask import Flask, request, render_template, jsonify, send_from_directory
from flask_restful import Resource, Api, reqparse
from algorithm.Version3.FairEnvyFreeAllocationProblem import FairEnvyFreeAllocationProblem
from algorithm.Version3.FairProportionalAllocationProblem import FairProportionalAllocationProblem

app = Flask(__name__)
api = Api(app)


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


@app.route('/result/<string:data>')
def build_result(data):
    print(data)
    return send_from_directory('../web/', 'Home.html')


def genrate_result_table(data):


def long_time_algorithm(data):
    send_email(data['email'], data['values'])


def send_email(email_receiver, values):
    sender_email = "fairnessalgorithm.io@gmail.com"
    receiver_email = email_receiver
    password = os.environ['EMAIL_PASSWORD']

    message = MIMEMultipart("alternative")
    message["Subject"] = "Fairness.io Results"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """need to complete here"""
    html = """need to complete here"""

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )


class Algorithm(Resource):

    def get(self):
        return {'algorithm': 'available'}

    def post(self):
        data = request.get_json()
        matrix = np.array(data['values'])

        if data['num_of_agents'] > 3:

            # for email support will finish it later.
            # thread = Thread(target=long_time_algorithm, daemon=True)
            # thread.start()

            json_request = {
                'message': 'to many agents , the algorithm results will send by email.',
                'RESULT': 1
            }

            req = jsonify(json_request)
            req.status_code = 200
            print("starting algorithm with thread task...")
            return req

        else:
            if data['problem'] == 'EnvyFree':
                ProblemObject = FairEnvyFreeAllocationProblem(matrix)
                ans = ProblemObject.find_allocation_with_min_shering()
            elif data['problem'] == 'Proportional':
                ProblemObject = FairProportionalAllocationProblem(matrix)
                ans = ProblemObject.find_allocation_with_min_shering()

            json_request = {
                'num_of_agents': data['num_of_agents'],
                'num_of_items': data['num_of_items'],
                'values': ans.tolist()
            }

            print(json_request)
            req = jsonify(json_request)
            req.status_code = 200
            print("done")
            return req


api.add_resource(Algorithm, '/calculator')

if __name__ == '__main__':
    app.run(debug=False, port=5000)
