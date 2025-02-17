class Cars4:
  tariff=0.2
  def __init__(self, color, seat):
    self.color = color
    self.seat = seat
  def drive(self):
    print('我這台車的顏色是',self.color)
    print('我這台車的座位是',self.seat)

Audi=Cars4("blue", 4)
Bentley=Cars4("red", 2)
print('查看關稅')
print('Cars4 tariff:',Cars4.tariff)
print('Object執行drive動作')
Audi.drive()
Bentley.drive()
print('Class執行drive動作，會有錯誤')
#Cars4.drive()
