import json
import os
import sys

from datetime import datetime
from enums import Errors, Status
from task import Task

#the "database"
FILE_PATH = "./lib/tasks.json"

def check_json_file_exists():
  if os.path.exists(FILE_PATH):
    return True
  else:
    with open(FILE_PATH, 'w') as f:
      f.close()

def get_current_datetime():
  current_datetime = datetime.now()
  datetime_str = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
  return datetime_str
 
def add_new_row(task_desc):
  #id = len(jsonfile) + 1
  row = Task(0, str(task_desc), get_current_datetime())
  file_exists = check_json_file_exists()
  
  try:
    with open(FILE_PATH, 'a') as f:
      f.write(row.get_json_obj())
      f.close()
  except IOError:
      return Errors.WRITE_FAIL.value
  return Status.SUCCESS.value
