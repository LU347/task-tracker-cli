from enum import Enum

class Errors(Enum):
  MISSING_ARG = "Missing arguments"
  WRITE_FAIL = "ERROR: Could not update db file"
  FETCH_FAIL = "ERROR: Failed to fetch data"
  INVALID_CMD = "ERROR: Invalid command"
  INVALID_ARG = "ERROR: Invalid argument type"

class Status(Enum):
  SUCCESS = "DB file successfully written"

