import csv
f=open('example1.csv',"r",encoding='utf-8')
for row in csv.DictReader(f,['a','b','c','d','e','f']):
 if float(row['f'])>71 :
    print(row['f'])
 else:
    print("error")
f.close( )
