import json
import helper

from task import Task

#the "database"
file_path = "./lib/tasks.json"
data = []

def initialize_data():
  try:
    with open(file_path, 'r') as f:
      tasks = json.load(f)
      for t in tasks:
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
