'''
import flask
from flask import request, jsonify

app = flask.Flask(__name__)


'''


from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify
import json


def create_resource(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def save_resource(filename, resource):
    with open(filename, 'w') as f:
        json.dump(resource, f)


hallgatok = create_resource('hallgatok.json')
TodoList = create_resource('todolist.json')
tantargyak = create_resource('tantargyak.json')
beosztas = create_resource('beosztas.json')

app = Flask('hallgato_demo')
api = Api(app)


class HallgatoList(Resource):
    def get(self):
        return jsonify(hallgatok)

    def update(self):
        pass


class Hallgato(Resource):
    def get(self, neptun):
        for hallgato in hallgatok:
            if hallgato['NEPTUN'] == neptun:
                return hallgato, 200
        return "Hallgato nincs a listában", 404

    def put(self, neptun):
        parser = reqparse.RequestParser()
        parser.add_argument("tantargy")
        parser.add_argument('Active')
        args = parser.parse_args()
        for hallgato in hallgatok:
            if hallgato['NEPTUN'] == neptun:
                hallgato['Subject'] = args['tantargy']
                hallgato['Active'] = args['Active']
                return hallgato, 200
        return "Hallgato nincs a listaban", 404


class Beosztas(Resource):
    def get(self, name):
        if name not in beosztas.keys():
            abort(404, message="Beosztas for Hallgato {} doesn't exist".format(name))
        return beosztas[name]


class Beosztas_list(Resource):
    def get(self):
        return jsonify(beosztas)


class Tantargyak(Resource):
    def get(self):
        return jsonify(tantargyak)


class Todo_list(Resource):
    def get(self):
        return jsonify(TodoList)


class Todo(Resource):
    def get(self, neptun):
        for hallgato in hallgatok:
            result = []
            if hallgato['NEPTUN'] == neptun:
                todo_indexes = hallgato['TODO']
                for todoidx in todo_indexes:
                    result.append(TodoList[todoidx])
                return result, 200
        return "Hallgato nincs a listaban", 404


api.add_resource(HallgatoList, '/hallgato')
api.add_resource(Hallgato, '/hallgato/<string:neptun>')
api.add_resource(Tantargyak, '/tantargyak')
api.add_resource(Todo_list, '/teendok')
api.add_resource(Todo, '/teendok/<string:neptun>')
api.add_resource(Beosztas_list, '/beosztas')
api.add_resource(Beosztas, '/beosztas/<string:name>')

# api.add_resource(Tracks, '/tracks')  # Route_2
# api.add_resource(Employees_Name, '/employees/<employee_id>')  # Route_3


if __name__ == '__main__':
    app.run(port='5011', debug=True)
