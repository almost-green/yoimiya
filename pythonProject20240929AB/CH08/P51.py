class Animal4:
  def __init__(self):
    print("動物的初始化")
class Cat3(Animal4):
  def __init__(self):
    print("貓的初始化")
class Bird5(Animal4):
  def __init__(self):
    print("鳥的初始化1")
class Bird6(Animal4):
  def __init__(self):
    print("鳥的初始化2")
    super( ).__init__( )
cat_1x=Cat3()
print()
bird_1x=Bird5()
print()
bird_2x=Bird6()
