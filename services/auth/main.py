# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC auth server."""

from concurrent import futures
import time

import grpc

# import your gPRC bindings here:

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class AuthService(auth_service_pb2_grpc.AuthServicer):

    def Authenticate(self, request, context):
        # Authenticate the account.
        user = User.objects.get(email=request.email, password=request.password)

        if user:
            return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)
        return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)

    def Validate(self, request, context):
        return helloworld_pb2.HelloReply(message='Hello again, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
