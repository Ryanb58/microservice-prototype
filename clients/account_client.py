from __future__ import print_function

import grpc

from protos.accounts import accounts_pb2
from protos.accounts import accounts_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('0.0.0.0:22222') as channel:
        stub = accounts_pb2_grpc.AccountServiceStub(channel)
        response = stub.AuthenticateByEmail(accounts_pb2.AuthenticateByEmailRequest(email='admin@example.com', password='password'))
    print("Account client received: " + response.id)


if __name__ == '__main__':
    run()
