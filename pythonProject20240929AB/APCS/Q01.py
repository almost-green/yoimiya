n = int(input())
a = input()
b = a.split(' ')
c = [int(x) for x in b]
c.sort()
d = [str(x) for x in c]
print(' '.join(d))
result = 'best case'
for x in c:
    if x<60:
        result = x
    else:
        break
print(result)

result = 'worst case'
for x in c:
    if x>=60:
        result = x
        break
print(result)
#
# less60 = []
# for x in c:
#     if x < 0:
#         less60.append(x)
# print(less60)