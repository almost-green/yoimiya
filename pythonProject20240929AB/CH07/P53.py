import re
str1="abcd abcdd abcb abc abcddd"
print(re.findall(r"abcd?",str1))
print(re.findall(r"abcd*",str1))
print(re.findall(r"abcd+",str1))
