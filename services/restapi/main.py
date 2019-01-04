from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_jwt_simple import (
    JWTManager, jwt_required, create_jwt, get_jwt_identity
)

import grpc
# import your gRPC bindings here:
from protos.accounts import accounts_pb2
from protos.accounts import accounts_pb2_grpc

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret-jwt-secret'  # Change this!
jwt = JWTManager(app)

api = Api(app, prefix="/api")

# Normally this would be a database.
USER_DATA = {
    "admin": "password"
}


class User(object):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return "User(id='%s')" % self.id

    def identity(payload):
        user_id = payload['identity']
        return {"user_id": user_id}


def verify(email, password):
    if not (email and password):
        return False

    with grpc.insecure_channel('0.0.0.0:22222') as channel:
        stub = accounts_pb2_grpc.AccountServiceStub(channel)
        try:
            authenticated = stub.AuthenticateByEmail(
                accounts_pb2.AuthenticateByEmailRequest(email=email, password=password))
        except Exception as e:
            from ipdb import set_trace;set_trace()
            print("Invalid username or password? Or perphaps we couldn't connect?")
            return False

        print("RESTAPI received: " + authenticated.id)
        if authenticated:
            return User(id=123)


class AuthorizeResource(Resource):
    def post(self):
        # Provide a method to create access tokens. The create_jwt()
        # function is used to actually generate the token
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"})

        params = request.get_json()
        email = params.get('email', None)
        password = params.get('password', None)

        if not email:
            return jsonify({"msg": "Missing email parameter"})
        if not password:
            return jsonify({"msg": "Missing password parameter"})

        user = verify(email, password)
        if not user:
            return jsonify({"msg": "Bad email or password"})

        # Identity can be any data that is json serializable
        ret = {'jwt': create_jwt(identity=user.id)}
        return jsonify(ret)


class PrivateResource(Resource):
    @jwt_required
    def get(self):
        return jsonify({'hello_from': get_jwt_identity()})


api.add_resource(AuthorizeResource, '/authorize')
api.add_resource(PrivateResource, '/private')

if __name__ == '__main__':
    app.run(debug=True)
