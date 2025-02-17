import bs4
htmlFile = open('web1.html',encoding="utf8",errors='ignore')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
objTag = objSoup.find_all('div',{'class':{'class1','class2'}})
for data in objTag:
  print(data)
  print(data.text)