from enum import Enum

class Errors(Enum):
  MISSING_ARG = "Missing arguments"
  WRITE_FAIL = "Error: Could not update db file"

class Status(Enum):
  SUCCESS = "DB file successfully written"