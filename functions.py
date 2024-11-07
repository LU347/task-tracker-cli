#the "API"
import db

def print_response(response):
  print("# " + response + " #\n")
 
def add_task(task):
  print_response(db.add_new_row(task))

def update_task(index, task):
  print("update")

def update_status(index, progress = None):
  print("update status")

def delete_task(index):
  print("delete")

def list_tasks(status = None):
  if status:
    print(status)
  else:
    print("tasks")

