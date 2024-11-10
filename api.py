import db
from enums import Errors

def process_client_request(req, arg1=None, arg2=None):
  match req:
    case "add":
      add_task(arg1)
    case "delete":
      delete_task(arg1)
    case "update":
      update_task(arg1, arg2)
    case "mark-in-progress":
      update_status(arg1, "In-Progress")
    case "mark-done":
      update_status(arg1, "Done")
    case "list":
      list_tasks(arg1)
    case _:
      print_response(Errors.INVALID_CMD.value)
      
def render_status(status):
  if status != "In-Progress":
    return "[x]"
  else:
    return "[ ]"

def print_response(response):
  if type(response) == str:
    print(f"# {response}  #\n")
  elif type(response) == list:
    print("\n#     To Do List     #")
    print("----------------------\n")
    for task in response:
      print(f"{task['id']} - {task['desc']} {render_status(task['status'])} \n")
  else:
    print("# Something went wrong #\n")
 
def add_task(task):
  if task is None or not str:
    print_response(Errors.INVALID_ARG.value)
  else:
    print_response(db.add_new_row(task))

def delete_task(index):
  if index is not None:
    print_response(db.delete_row(int(index)))
  else:
    print_response(Errors.INVALID_ARG.value)
 
def update_task(index, task):
  if index is not None:
    print_response(db.update_task(index, task))
  else:
    print_response(Errors.INVALID_ARG.value)

def update_status(index, status):
  if index:
    print_response(db.update_status(index, status))

def list_tasks(list_filter = None):
  if list_filter:
    print_response(db.list_filtered_tasks(list_filter))
  else:
    print_response(db.list_all_tasks())

