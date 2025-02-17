class Cars3:
  tariff=0.2
  def __init__(self, color, seat):
    self.color = color
    self.seat = seat
  def drive(self):
    print('我這台車的顏色是',self.color)
    print('我這台車的座位是',self.seat)
Audi=Cars3("blue", 4)
Bentley=Cars3("red", 2)
print('查看關稅')
print('Audi tariff:',Audi.tariff)
print('Bentley tariff:',Bentley.tariff)
Cars3.tariff = 0.6
print('變更關稅')
print('Audi tariff:',Audi.tariff)
print('Bentley tariff:',Bentley.tariff)
