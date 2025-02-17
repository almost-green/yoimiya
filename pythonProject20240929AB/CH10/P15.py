import bs4
htmlFile = open('/content/drive/MyDrive/Colab/web1.html',encoding="utf8",errors='ignore')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
objTag = objSoup.find_all(class_='class1')
for data in objTag:
  print(data)
  print(data.text)