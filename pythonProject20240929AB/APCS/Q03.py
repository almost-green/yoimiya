S = input()
A = 0
B = 0
for i in range(len(S)):
    if 1%2 == 0:
        B += int(S[i])
    else:
        A += int(S[i])
print(abs(A-B))