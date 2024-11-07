import json

from enums import Errors, Status
from datetime import datetime

def get_current_datetime():
  current_datetime = datetime.now()
  date_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
  return date_string

def write_to_file(file_path, data):
  try:
    with open(file_path, 'w') as f:
      json.dump(data, f, indent=4)
      f.close()
  except IOError:
    return Errors.WRITE_FAIL.value
  return Status.SUCCESS.value
