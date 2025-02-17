import bs4
htmlFile = open('web1.html',encoding="utf8",errors='ignore')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
print(objSoup.string)
print("-"*70)
print(objSoup.strings)
print("-"*70)
for string in objSoup.strings:
    print(string)
print("--------------------------1------")
for string in objSoup.strings:
    print(repr(string))
print("--------------------------2------")
for string in objSoup.stripped_strings:
    print(repr(string))
print("---------------------------3-----")
