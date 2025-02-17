class Animal:
    def __init__(self):
        self.year = 10

    def run(self):
        print("他會移動")

class Cat1(Animal):
    def accelerate(self):
        print("他會跑步")

class Bird1(Animal):
    def fly(self):
        print("他會飛行")
class Animal2:
  def __init__(self):
    self.year = 10
  def run(self):
    print("動物會移動")
  def eat(self):
    print('他會吃東西')
class Cat2(Animal2):
  def accelerate(self):
    print("他會跑步")
class Bird2(Animal2):
  def fly(self):
    print("他會飛行")
  def run(self):
    print("鳥類的移動")
class Bird3(Animal2):
  def fly(self):
    print("他會飛行")
  def run(self):
    super().run()
    print("鳥類的移動")
cat_1 = Cat2()
cat_1.run()
print('執行子類別的同名方法')
bird_1=Bird2()
bird_1.run()
print('執行父類別的同名方法')
bird_2=Bird3()
bird_2.run()
print('執行父類別的其他方法')
bird_2.eat()