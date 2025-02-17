import  re
s="Python was conceived in the late 1980s by Guido van Rossum"
#match=re.findall(r'[a-t]',s)
#match=re.findall(r'[a-t]{2}',s)
#match=re.findall(r'[a-t]{3,6}',s)
match=re.findall(r'[a-t]{4,}',s)
print(len(match))
if match:
  print(match)
