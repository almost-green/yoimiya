class Cars6:
  tariff=0.2
  def __init__(self, color, seat):
    self.color = color
    self.seat = seat
  @classmethod
  def Bus(cls):
    return cls("black", 6)
  @classmethod
  def Taxi(cls):
    return cls("yellow", 4)

Audi = Cars6("blue", 4)
bus1 = Cars6.Bus()
texi1 = Cars6.Taxi()
print('Audi color:',Audi.color)
print('Audi seat:',Audi.seat)
print('bus1 color:',bus1.color)
print('bus1 seat:',bus1.seat)
print('texi1 color:',texi1.color)
print('texi1 seat:',texi1.seat)
