from __future__ import print_function

import grpc

import authenticator_pb2
import authenticator_pb2_grpc


def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = authenticator_pb2_grpc.AuthenticatorStub(channel)
 
  # Insert logic for Login.
  # Insert logic for Profile.

if __name__ == '__main__':
  run()
