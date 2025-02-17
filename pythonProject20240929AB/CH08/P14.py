class Cars:
  def __init__(self, color, seat):
    self.color = color
    self.seat = seat
  def drive(self):
    print('我這台車的顏色是',self.color)
    print('我這台車的座位是',self.seat)
Audi=Cars("blue", 4)
print(Audi.color)
print(Audi.seat)
Audi.drive()
Audi.color = "red"
Audi.seat = 2
print(Audi.color)
print(Audi.seat)
