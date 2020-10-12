import numpy as np
import sys
from server.server_utils import send_email
from server.server_utils import generate_table
from threading import Thread
from _sha256 import sha256


sys.path.append('../')
from flask import Flask, request, render_template, jsonify, send_from_directory
from flask_restful import Resource, Api, reqparse
from algorithm.Version3.FairEnvyFreeAllocationProblem import FairEnvyFreeAllocationProblem
from algorithm.Version3.FairProportionalAllocationProblem import FairProportionalAllocationProblem

app = Flask(__name__)
api = Api(app)

"""

"""
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


def long_time_algorithm(data):
    result = run_algorithm(data)
    url = generate_table(agents=data['agents'], items=data['items'],
                         data=result, file_name=sha256(str(data['values']).encode('utf-8')).hexdigest())
    send_email(data['email'], url)


if __name__ == '__main__':
    app.run(debug=False, port=5000)
