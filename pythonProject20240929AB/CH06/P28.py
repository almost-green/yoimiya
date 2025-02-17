print("匿名函數可用於條件分析表達上")
findmin=(lambda x, y: x if x < y else y)
print(findmin(10, 20))
print(findmin(40,30))
