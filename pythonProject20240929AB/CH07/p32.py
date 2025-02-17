score=105
try:
  if score>100 or score <0:
    raise OverflowError
except OverflowError:
  print("成績數值錯誤")
print("after exception....")
