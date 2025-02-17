import re
s = "Tim's phone numbers are 12345-41521 and 78963-85214"
match = re.findall(r'\d', s)
if match:
  print(match)