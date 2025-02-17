a = input()
b = a.split(' ')
# print(b)
c = [int(x) for x in b]
c.sort()
#print(c)
d = [str(x) for x in c]
print(' '.join(d))
if c[2]>=c[0]+c[1]:
    print('no')
elif c[2]**2 == c[0]**2 + c[1]**2:
    print('Right')
elif c[2] ** 2 < c[0] ** 2 + c[1] ** 2:
    print('Acute')
elif c[2] ** 2 > c[0] ** 2 + c[1] ** 2:
    print('Obtuse')