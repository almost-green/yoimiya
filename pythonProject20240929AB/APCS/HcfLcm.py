a = int(input('請輸入第一個整數:'))
b = int(input('請輸入第二個整數:'))
if (a>b):
    a, b = b, a
print(a,b)
hcf = 1
for x in range(a, 0, -1):
    if a%x == 0 and b%x == 0:
        hcf = x
        break
print('最大公因數:',hcf)
lcm = b
while lcm%b != 0 or lcm%a != 0:
    lcm +=1
print('最小公倍數:',lcm)