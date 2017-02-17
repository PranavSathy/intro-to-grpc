from __future__ import print_function

import grpc

import authenticator_pb2
import authenticator_pb2_grpc


def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = authenticator_pb2_grpc.AuthenticatorStub(channel)
 
  request = authenticator_pb2.LoginRequest(
	username='Pranav',
	password='grpc'
  ) 
 
  response = stub.Login(request)
  print("Authenticator client received: " + response.jwt)

  # Let's attempt a login.
  request = authenticator_pb2.ProfileRequest(
  	jwt=response.jwt
  )
  response = stub.Profile(request)
  print("Authenticator client received: " + response.username)
  print("Authenticator registered last logged in: %s" % response.last_logged_in.ToDatetime())

if __name__ == '__main__':
  run()
