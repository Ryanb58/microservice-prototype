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
"""The Python implementation of the GRPC account server."""
from concurrent import futures
import os
import time
import sqlite3

import grpc

# import your gRPC bindings here:
from protos.accounts import accounts_pb2
from protos.accounts import accounts_pb2_grpc

# Models:
# from create_tables import Base, User

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class AccountServicer(accounts_pb2_grpc.AccountServiceServicer):
# class AccountServicer(object):

    def dbConnect(self):
        self.dbconnection = sqlite3.connect("app.sqlite", check_same_thread=False)
        return self.dbconnection.cursor()

    def AuthenticateByEmail(self, request, context):
        print("Auth By Email")
        # Write
        # cursor = self.dbConnect()
        # cursor.execute("INSERT INTO remotefiles VALUES (?, ?, ?, ?)", (hash, sharepath, peerip, size))
        # self.dbconnection.commit()

        cursor = self.dbConnect()
        cursor.execute("SELECT id, name, email, confirm_token, password_reset_token FROM users WHERE email=? AND password=?", (request.email, request.password))
        user = cursor.fetchone()

        # # Get the user from our db if they match.
        # user = session.query(User).filter_by(
        #     email=request.email,
        #     password=request.password
        # ).first()
        if user:
            return accounts_pb2.Account(
                id=str(user[0]),
                name=str(user[1]),
                email=str(user[2]),
                confirm_token=str(user[3]),
                password_reset_token=str(user[4]))
        return grpc.StatusCode.UNAUTHENTICATED("account not found")



def serve():
    print("Starting server...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    accounts_pb2_grpc.add_AccountServiceServicer_to_server(AccountServicer(), server)
    server.add_insecure_port('[::]:22222')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    # Serve gRPC stuff.

    serve()

    # service = AccountServicer()
    # service.
