import json

class Task:

  def __init__(self, auto_id, description, created_at):
    self.id = auto_id
    self.desc = description
    self.status = "In-Progress"
    self.created_at = created_at
    self.updated_at = str(None)
  
  def get_json_obj(self):
    return json.dumps(self.__dict__, indent=4)

