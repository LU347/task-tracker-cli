import json
import helper

from task import Task
from enums import Errors, Status

#the "database"
file_path = "./lib/tasks.json"
data = []

def initialize_data():
  try:
    with open(file_path, 'r') as f:
      tasks = json.load(f)
      for t in tasks:
        if isinstance(t, str):
          data.append(json.loads(t))
        else:
          data.append(t)
      f.close()
  except FileNotFoundError:
    with open(file_path, 'w') as f:
      json.dump([], f)
      f.close()

def get_row_count():
  count = len(data)
  return count
 
def add_new_row(task_desc):
  initialize_data()
  
  auto_id = len(data) + 1
  row = Task(auto_id, str(task_desc), helper.get_current_datetime())
  data.append(row.get_json_obj())

  status = helper.write_to_file(file_path, data)

  return status

def update_row(auto_id, new_task):
  initialize_data()
  auto_id = int(auto_id) - 1
  try:
    data[auto_id]["desc"] = new_task
    data[auto_id]["updated_at"] = helper.get_current_datetime()
    helper.write_to_file(file_path, data)
    return Status.SUCCESS.value
  except IndexError:
    return Errors.INVALID_ROW.value

def list_all_tasks():
  initialize_data()
  return data

def list_filtered_tasks(list_filter):
  initialize_data()
  filtered_data = []

  for task in data:
    if task["status"] == list_filter:
      filtered_data.append(task)
  return filtered_data

