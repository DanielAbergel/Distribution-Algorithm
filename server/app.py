import datetime
import numpy as np
import sys

sys.path.append('../')
from flask import Flask, request, render_template, jsonify, send_from_directory
from flask_restful import Resource, Api, reqparse
from algorithm.Version2.FairEnvyFreeAllocationProblem import FairEnvyFreeAllocationProblem

app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return send_from_directory('../web/','Home.html')




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
