
class Task:

  def __init__(self, auto_id, description, status, created_at, updated_at):
    self.id = auto_id
    self.desc = description
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at

  def get_status():
    return self.status

  def update_status(new_status):
    self.status = new_status

  def get_description():
    return self.desc

  def update_description(new_desc):
    self.desc = new_desc

  def get_status():
    return self.status

  def update_status(new_status):
    self.status = new_status

  def get_creation_date():
    return self.created_at

  def get_updated_date():
    return self.updated_at

  def set_updated_date(new_date):
    self.updated_at = new_date


