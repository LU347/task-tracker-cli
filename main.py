import sys
import api

def main():
  match len(sys.argv):
    case 2:
      api.process_client_request(sys.argv[1])
    case 3:
      api.process_client_request(sys.argv[1], sys.argv[2])
    case 4:
      api.process_client_request(sys.argv[1], sys.argv[2], sys.argv[3])

main()
