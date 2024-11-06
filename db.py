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
      json.dump({}, f)

def add_new_row(task_desc):
  #id = len(jsonfile) + 1
  row = Task(0, task_desc, datetime.today())
  file_exists = check_json_file_exists()
  if file_exists:
    try:
      with open(FILE_PATH, 'a') as f:
        #TODO: convert to json and write
    except IOError:
      return Errors.WRITE_FAIL
  else:
    return Status.SUCCESS
