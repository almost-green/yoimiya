N=int(input())
segsList = []
for i in range(N):
    segs = input().split(' ')
    for j in range(int(segs[0]),int(segs[1])):
        segsList.append(j)
segsSet = set(segsList)
print(len(segsSet))