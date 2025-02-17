import bs4
htmlFile = open('web1.html',encoding="utf8",errors='ignore')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
for child in  objSoup.body.children:
    print(child)
print("--------------------------------")
for i,child in enumerate(objSoup.body.children):
    print(i,child)
print("--------------------------------")
