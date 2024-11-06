import sys
import functions

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
      functions.add_task(task)
    case "update":
      index = check_if_arg_exists(3)
      new_task = check_if_arg_exists(4)
      functions.update_task(index, new_task)
    case "delete":
      index = check_if_arg_exists(3)
      functions.delete_task(index)
    case "mark-in-progress":
      index = check_if_arg_exists(3)
      functions.update_progress(index, "In-Progress")
    case "mark-done":
      index = check_if_arg_exists(3)
      functions.update_progress(index, "Done")
    case "list":
      status = sys.argv[2] if len(sys.argv) > 2 else None
      functions.list_tasks(status)
        

main()
