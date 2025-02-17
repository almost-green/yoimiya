import bs4
htmlFile = open('web1.html',encoding="utf8",errors='ignore')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
print(objSoup.p.next_element)
print("----------------------------1----")
print(objSoup.p.previous_element)
print("----------------------------2----")
print(objSoup.p.next_element.next_element)
print("------------------------------3--")
for element1 in objSoup.p.next_elements:
  if element1!='\n':
    print(repr(element1))
