import json
import os
import sys

from enums import Errors, Status

#the "database"
FILE_PATH = "./lib/tasks.json"

def check_json_file_exists():
  if os.path.exists(FILE_PATH):
    return True
  else:
    with open(FILE_PATH, 'w') as f:
      json.dump({}, f)


def add_task(new_task):
  file_exists = check_json_file_exists()
  if file_exists:
    try:
      with open(FILE_PATH, 'a') as f:
        f.write(new_task)
    except IOError:
      sys.exit(Errors.WRITE_FAIL.value)
    else:
      return sys.exit(Status.SUCCESS.value)
