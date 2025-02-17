a=1
try:
  a = int(input("輸入正整數: "))
  if a <= 0:
    raise ValueError("That is not a positive number!")
except ValueError as ve:
  print(ve)
