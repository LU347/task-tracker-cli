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
  command = check_if_arg_exists(1)
  
  match command:
    case "add":
      task = check_if_arg_exists(2) 
      api.add_task(task)
    case "update":
      index = check_if_arg_exists(3)
      new_task = check_if_arg_exists(4)
      api.update_task(index, new_task)
    case "delete":
      index = check_if_arg_exists(3)
      api.delete_task(index)
    case "mark-in-progress":
      index = check_if_arg_exists(3)
      api.update_progress(index, "In-Progress")
    case "mark-done":
      index = check_if_arg_exists(3)
      api.update_progress(index, "Done")
    case "list":
      status = sys.argv[2] if len(sys.argv) > 2 else None
      api.list_tasks(status)
    case _:
      sys.exit(Errors.INVALID_CMD.value)
        

main()
