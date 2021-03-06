""" API Backend - Resource Models """

from flask_restful import Resource, abort

from app.api import api_rest
from app.api.security import require_auth


class NonSecure(Resource):

    def get(self, *args, **kwargs):
        abort(405)

    def post(self, *args, **kwargs):
        abort(405)

    def put(self, *args, **kwargs):
        abort(405)

    def patch(self, *args, **kwargs):
        abort(405)

    def delete(self, *args, **kwargs):
        abort(405)


class Secure(NonSecure):
    method_decorators = [require_auth]


def rest_resource(resource_cls):
    """ Decorator for adding resources to Api App """
    api_rest.add_resource(resource_cls, *resource_cls.endpoints)
