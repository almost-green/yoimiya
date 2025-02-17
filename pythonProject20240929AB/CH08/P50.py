class Animal3:
  def __init__(self):
    self.year = 10
  def run(self):
    print("動物會移動")
  def eat(self):
    print('他會吃東西')
class Bird4:
  def run(self):
    print("鳥類的移動")
class chicken1(Animal3,Bird4):
  pass
chicken_1 =chicken1()
chicken_1.run()
