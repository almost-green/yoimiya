list1=[1,2,3,3,4,6.6,'list1']
list2=[11,12,13,13,14,16.6,'list2']
print('list1 id記憶體位址，每個人的資訊都不同:',id(list1))
list3=list1.copy()
print('list3 id記憶體位址，每個人的資訊都不同:',id(list3))
list1.append(list2)
print(len(list1))
print(list1)
list3.extend(list2)
print(len(list3))
print(list3)
