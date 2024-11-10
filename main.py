import sys
import api

from enums import Errors

#the client
def check_if_arg_exists(index):
  try:
    return sys.argv[index]
  except IndexError:
    sys.exit(Errors.MISSING_ARG.value)

def main():
  match len(sys.argv):
    case 2:
      api.process_client_request(sys.argv[1])
    case 3:
      api.process_client_request(sys.argv[1], sys.argv[2])
    case 4:
      api.process_client_request(sys.argv[1], sys.argv[2], sys.argv[3])

main()
