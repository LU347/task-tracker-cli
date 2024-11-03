#the "API"
def add_task(task):
  print("add")

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

