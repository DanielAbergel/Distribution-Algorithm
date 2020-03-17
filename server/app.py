import datetime

import numpy as np
from flask import Flask, request, render_template, jsonify
from flask_restful import Resource, Api, reqparse
from algorithm.Version2.FairEnvyFreeAllocationProblem import FairEnvyFreeAllocationProblem


app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return render_template('index.html')


class Algorithm(Resource):

    def get(self):
        return {'algorithm': 'available'}

    def post(self):

        data = request.get_json()

        matrix = np.array([0] * data['num_of_items'])
        arr = data['{}'.format(0)]

        for i in range(0, data['num_of_items']):
            matrix[i] = arr[i]
        for i in range(1, data['num_of_agents']):
            arr = data['{}'.format(i)]
            matrix = np.vstack((matrix, arr))

        x = FairEnvyFreeAllocationProblem(matrix)
        g = x.find_allocation_with_min_shering()

        json_request = {
            'num_of_agents': data['num_of_agents'],
            'num_of_items': data['num_of_items'],
        }

        for i in range(0, data['num_of_agents']):
            json_request["{}".format(i)] = list(g[i])
        print(json_request)
        req = jsonify(json_request)
        req.status_code = 200
        return req


api.add_resource(Algorithm, '/calculator')

if __name__ == '__main__':
    app.run(debug=True)
