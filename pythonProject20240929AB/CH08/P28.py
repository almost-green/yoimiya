class person:
  def __init__(self,firstname,lastname):
    self.first = firstname
    self.last = lastname
myname = person("Barack","Obama")
myname2 = person("George","Bush")
print(myname.last)
