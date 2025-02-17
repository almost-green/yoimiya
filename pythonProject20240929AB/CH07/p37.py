class ValueTooSmall(Exception):
   pass
class ValueTooLarge(Exception):
   pass
number = 10
try:
  i_num = int(input("請輸入一個整數: "))
  if i_num < number:
    raise ValueTooSmall
  elif i_num > number:
    raise ValueTooLarge
except ValueTooSmall:
    print("這個數字太小")
except ValueTooLarge:
    print("這個數字太大")
print("結束")
