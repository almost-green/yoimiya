import csv
f=open('example.csv',"r",encoding='utf-8')
reader = csv.reader(f)
ofile = open('ttest.csv', "w",encoding='utf-8')
writer = csv.writer(ofile, delimiter='-', quotechar='"', lineterminator="\n")
for row in reader:
    writer.writerow(row)
f.close( )
ofile.close()
