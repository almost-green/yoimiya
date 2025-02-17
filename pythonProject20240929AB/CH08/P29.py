class MyCompany:
  def __init__(self, compname, income, headcount):
    self.name = compname
    self.revenue = income
    self.no_of_employees = headcount
  def productivity(self):
    return self.revenue/self.no_of_employees
print("人均生產力:", MyCompany('XYZ Bank', 1000,100).productivity())
Bank = MyCompany('ABC Bank', 5000,200)
print("人均生產力:", MyCompany.productivity(Bank))