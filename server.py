from concurrent import futures
from datetime import datetime
import dateutil.parser
import time

import grpc
import jwt

import authenticator_pb2
import authenticator_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_JWT_SECRET = 'grpc_rules'

class Authenticator(authenticator_pb2_grpc.AuthenticatorServicer):

  def Login(self, request, context):
	# Insert logic for Login.

  def Profile(self, request, context):
	# Insert logic for Profile.

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  authenticator_pb2_grpc.add_AuthenticatorServicer_to_server(Authenticator(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  
  print 'Server Started'
  
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()
