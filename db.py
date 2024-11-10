import json

from task import Task
from datetime import datetime
from enums import Errors, Status

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

def write_to_file():
  try:
    with open(file_path, 'w') as f:
      json.dump(data, f, indent=4)
      f.close()
  except IOError:
    return Errors.WRITE_FAIL.value
  return Status.SUCCESS.value

def get_current_datetime():
  current_datetime = datetime.now()
  date_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
  return date_string

def get_row_count():
  count = len(data)
  return count
 
def add_new_row(task_desc):
  initialize_data() 
  auto_id = len(data)
  row = Task(auto_id, str(task_desc), get_current_datetime())
  data.append(row.get_json_obj())
  
  status = write_to_file()
  return status

def delete_row(index):
  initialize_data()

  try:
    data.pop(index)
    for i in range(len(data)):
      data[i]["id"] = i
    status = write_to_file()
    return status
  except IndexError:
    return Errors.INVALID_ROW.value
  
def update_key(auto_id, key, new_value):
  initialize_data()
  auto_id = int(auto_id)

  try:
    data[auto_id][key] = new_value
    data[auto_id]["updated_at"] = get_current_datetime()
    status = write_to_file()
    return status
  except IndexError:
    return Errors.INVALID_ROW.value

def update_task(auto_id, new_task):
  return update_key(auto_id, "desc", new_task)

def update_status(auto_id, new_status):
  return update_key(auto_id, "status", new_status)
 
def list_all_tasks():
  initialize_data()
  return data

def list_filtered_tasks(list_filter):
  initialize_data()
  filtered_data = []

  for task in data:
    if task["status"].lower() == list_filter.lower():
      filtered_data.append(task)
  return filtered_data

