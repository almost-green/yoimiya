import csv
f=open('example.csv',"r",encoding='utf-8')
csv1= csv.reader(f)
list1= list(csv1)
print(list1)
f.close()