from enum import Enum

class Errors(Enum):
  MISSING_ARG = "Missing arguments"
  WRITE_FAIL = "Error: Could not update db file"

class Status(Enum):
  SUCCESS = "DB file successfully written"

class Type(Enum):
  #0 = In Progress #1 = Done
  IN_PROGRESS = 0
  DONE = 1

