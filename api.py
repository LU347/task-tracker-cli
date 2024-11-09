#the "API"
import db

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

