import bs4
htmlFile = open('web1.html',encoding="utf8",errors='ignore')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
objTag = objSoup.find_all(['h2','h3','h4'])
for data in objTag:
  print(data)
  print(data.text)