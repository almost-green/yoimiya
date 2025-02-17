import bs4
htmlFile = open('web1.html',
                encoding="utf8",
                errors='ignore')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
print(objSoup.p.next_sibling)
print("-----------------------------1---")
print(objSoup.p.previous_sibling)
print("-----------------------------2---")
print(objSoup.p.next_sibling.next_sibling)
print("-----------------------------3---")
for sibling in objSoup.p.next_siblings:
  if sibling!='\n':
    print(repr(sibling))
