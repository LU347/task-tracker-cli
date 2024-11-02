import io
import json
import os
import sys

PATH = "tasks.json"

def add_task(task):
  print(task)

def check_if_arg_exists(index):
  try:
    return sys.argv[index]
  except IndexError:
    sys.exit("Missing argument")

def main():  
  valid_commands = ["add", "delete", "update", "list", "mark-done", "mark-in-progress"]
  command = check_if_arg_exists(1)

  if not (command in valid_commands):
    sys.exit("Invalid command\n Valid Commands: add, delete, update, list, mark-done, mark-inprogress")

  match command:
    case "add":
      task = check_if_arg_exists(2)

      if task:
        add_task(task)

main()
