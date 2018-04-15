from flask import jsonify, request
from flask_restful import abort

from app.api.rest.base import NonSecure, Secure, rest_resource


def process_request_data():
    if request.data:
        return request.json
    else:
        abort(400, message='Please Send Raw Data!')


@rest_resource
class BasicRequest(NonSecure):
    endpoints = ['/basic']
    def get(self):
        return jsonify(dict(message="Successful Get Request Made!"))

    def post(self):
        data = process_request_data()
        return jsonify(data)


@rest_resource
class SecureRequest(Secure):
    endpoints = ['/secure']
    def get(self):
        return jsonify(dict(message="Successful Get Request Made!"))

    def post(self):
        data = process_request_data()
        return jsonify(data)