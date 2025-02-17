import csv
f=open("example1.csv","r")
for row in csv.reader(f):
    if(float(row[5])>100):
      print(row[0])
f.close()