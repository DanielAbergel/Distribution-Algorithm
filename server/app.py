import time
from threading import current_thread
import numpy as np
import sys
import os
from threading import Thread
from _sha256 import sha256
import random

sys.path.append('../')
from flask import Flask, request, jsonify, send_from_directory
from flask_restful import Resource, Api
from algorithm.Version3.FairEnvyFreeAllocationProblem import FairEnvyFreeAllocationProblem
from algorithm.Version3.FairProportionalAllocationProblem import FairProportionalAllocationProblem
from server_utils import send_email
from server_utils import generate_table

app = Flask(__name__)
api = Api(app)

"""
Each function below receives a URL and returns the content for this URL
HTML , js, CSS , images , etc..
"""


@app.route('/')
def home():
    return send_from_directory('web', 'Home.html')


@app.route('/<string:html>')
def send_html(html):
    return send_from_directory('web', html)


@app.route('/DOM/<string:dom>')
def send_dom(dom):
    return send_from_directory('web/DOM', dom)


@app.route('/css/<string:css>')
def send_css(css):
    return send_from_directory('web/css', css)


@app.route('/images/<string:image>')
def send_images(image):
    return send_from_directory('web/images', image)


"""
:return the generated URL with the Algorithm results and explanation
"""


@app.route('/generated_html/<string:data>')
def build_result(data):
    return send_from_directory('web/generated_html', data)


"""
This class is a Restful API responsible for the communication with the client.
receive the input from the client(website),
calculating the algorithm, send email in case the algorithm takes more than 5 sec, 
and returns the Algorithm results.
"""


def run(x, s):
    time.sleep(s)
    print("%s %s %s" % (current_thread(), x, s))


class Algorithm(Resource):

    def get(self):
        return {'algorithm': 'available'}

    def post(self):

        data = request.get_json()
        print(os.getcwd())
        if int(data['num_of_agents']) > 3:

            for x in range(4):
                Thread(target=run, args=(x, random.random())).start()

            long_time_algorithm(data)

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
            url = generate_table(agents=data['agents'], items=data['items'],
                                 data=result, file_name=sha256(str(data['values']).encode('utf-8')).hexdigest(),
                                 data_json=data)

            json_request = {
                'problem': data['problem'],
                'agents': data['agents'],
                'items': data['items'],
                'values': result,
                'RESULT': 0,
                'url': url
            }

            print(json_request)
            req = jsonify(json_request)
            req.status_code = 200
            print("done")
            return req


api.add_resource(Algorithm, '/calculator')

"""
calculating the algorithm with specific input
:param data represent the JSON that the server receives from the client-side
:return the algorithm result as matrix (numpy.np)
"""


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


"""
runnable function that runs in case of long algorithm (4 agents or more)
calculating the algorithm with specific input , and sending email to the end-user with the algorithm results.
:param data represent the JSON that the server receives from the client-side
"""


def long_time_algorithm(data):
    result = run_algorithm(data)
    url = generate_table(agents=data['agents'], items=data['items'],
                         data=result, file_name=sha256(str(data['values']).encode('utf-8')).hexdigest(), data_json=data)
    send_email(data['email'], url)


# Used for Debugging only
if __name__ == '__main__':
    app.run(debug=False, port=5000)
