s = input().split(' ')
a = int(s[0])
b = int(s[1])
c = int(s[2])
result = ''
if (c==0 and (a==0 or b==0)) or (c==1 and (a!=0 and b!=0)):
    result += 'AND'
if (c==0 and(a==0 and b==0)) or (c==1 and(a!=0 and b!=0)):
    if len(result)>0:
        result += '\n'
    result += 'OR'
if (c==0 and ((a==0 and b==0) or (a!=0 and b!=0))) or \
(c==1 and ((a!=0 and b==0) or (a!=0 and b==0))):
    if len(result)>0:
        result += '\n'
    result += 'XOR'
if len(result)==0:
    result = 'IMPOSSIBLE'
print(result)