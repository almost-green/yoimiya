# a = int(input())
# b = int(input())
# c = 1
# i = 1
# while i <= b:
#     c = c*a
#     i = i+1
# print(c)


#while 階乘
# a = int(input())
# b = 1
# i = 0
# b = b*a -> b = b*(a-0)
# b = b*(a-1)...
# while i<=(a-2):
#     b = b*(a-i)
#     i = i+1


a = int(input())
b = int(input())
c = 1
i = 0
# 8 / 2 = 4 -->1
# 4 / 2 = 2 -->2
# 2 / 2 = 1 -->3
while b !=1:
    b = b//a
    c = c+1
print(c)