import json
import os

#the "database"
FILE_PATH = "./lib/tasks.json"

def create_json_file(data):
  if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, 'w') as f:
      json.dump("test", f, indent=4)

create_json_file("test2")
