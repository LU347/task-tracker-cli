#the "API"
import db
from enums import Errors

def process_client_request(req, arg1=None, arg2=None):
  match req:
    case "add":
      add_task(arg1)
    case "update":
      update_task(arg1, arg2)
      print_response(Errors.MISSING_ARG.value)
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
    print("# " + response + " #\n")
  elif type(response) == list:
    print("\n#     To Do List     #")
    print("----------------------\n")
    for task in response:
      print(str(task["id"]) + " - " + task["desc"] + " " + render_status(task["status"]) + "\n")
  else:
    print("# Something went wrong #\n")
 
def add_task(task):
  if type(task) != str:
    print_response(Errors.INVALID_ARG.value)
  print_response(db.add_new_row(task))

def update_task(index, task):
  print("update")

def update_status(index, progress = None):
  print("update status")

def delete_task(index):
  print("delete")

def list_tasks(list_filter = None):
  if list_filter:
    print_response(db.list_filtered_tasks(list_filter))
  else:
    print_response(db.list_all_tasks())

