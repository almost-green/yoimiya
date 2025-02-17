import bs4
htmlFile = open('web1.html',
                encoding="utf8",
                errors='ignore')
objSoup = bs4.BeautifulSoup(htmlFile,
                            'lxml')
print("以下是列印一個h1元素: ")
objTag = objSoup.find('h1')
print(objTag.text)
print("以下是列印全部h1元素: ")
objTag = objSoup.find_all('h1')
for data in objTag:
  print(data.text)
objTag = objSoup.find_all('h2', limit=2)
print("以下是列印h2元素，只找兩個: ")
for data in objTag:
  print(data.text)