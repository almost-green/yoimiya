import csv
f=open('example.csv',"r",encoding='utf-8')
for row in csv.DictReader(f):
  if float(row['漲跌點數'])>9.34 :
     print(row['漲跌點數'])
f.close()