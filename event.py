class Event:
  def __init__(self, name, explain):
    self.name = name
    self.exp = explain

class totalEvent:
  def __init__(self, name, explain,fields):
    self.name = name
    self.exp = explain
    self.fields = fields