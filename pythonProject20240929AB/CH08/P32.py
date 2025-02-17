class Cars2:
  def __init__(self, color, seat):
    self.color = color
    self.seat = seat
  def drive(self):
    print('我這台車的顏色是',self.color)
    print('我這台車的座位是',self.seat)
Audi=Cars2("blue", 4)
Bentley=Cars2("red", 2)
Audi.year=1990
Bentley.year=1980
print('Audi color:',Audi.color)
print('Audi seat:',Audi.seat)
print('Audi year:',Audi.year)
print('Bentley color:',Bentley.color)
print('Bentley seat:',Bentley.seat)
print('Bentley year:',Bentley.year)