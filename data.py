import json
import os

from errors import Errors

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
  
  try:
    with open(FILE_PATH, 'a') as f:
      f.write(new_task)
    except IOError:
      sys.exit(Errors.WRITE_FAIL)
