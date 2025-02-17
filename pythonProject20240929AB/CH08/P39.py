class Cars5:
  tariff=0.2
  def __init__(self, color, seat):
    self.color = color
    self.seat = seat
  def drive(self):
    print('我這台車的顏色是',self.color)
    print('我這台車的座位是',self.seat)
  @classmethod
  def opendata(cls):
    print('查看關稅為:',cls.tariff)

Audi=Cars5("blue", 4)
Bentley=Cars5("red", 2)
print('Object執行opendata動作')
Audi.opendata()
Bentley.opendata()
print('Class執行opendata動作')
Cars5.opendata()
