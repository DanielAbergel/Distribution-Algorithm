import datetime
import numpy as np
from flask import Flask, request, render_template, jsonify, send_from_directory
from flask_restful import Resource, Api, reqparse
from algorithm.Version2.FairEnvyFreeAllocationProblem import FairEnvyFreeAllocationProblem

app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/<string:html>')
def send_html(html):
    return send_from_directory('templates/', html)


@app.route('/DOM/<string:dom>')
def send_dom(dom):
    return send_from_directory('templates/DOM', dom)


@app.route('/css/<string:path>')
def send_css(path):
    return send_from_directory('templates/css', path)


@app.route('/images/<string:path>')
def send_images(path):
    return send_from_directory('templates/images', path)


class Algorithm(Resource):

    def get(self):
        return {'algorithm': 'available'}

    def post(self):
        data = request.get_json()
        matrix = np.array(data['values'])

        x = FairEnvyFreeAllocationProblem(matrix)
        g = x.find_allocation_with_min_shering()

        json_request = {
            'num_of_agents': data['num_of_agents'],
            'num_of_items': data['num_of_items'],
            'values': g.tolist()
        }

        print(json_request)
        req = jsonify(json_request)
        req.status_code = 200
        return req


api.add_resource(Algorithm, '/calculator')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
