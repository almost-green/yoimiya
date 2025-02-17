import re
inputStr = "hello 123 world 456"
replacedStr = re.sub("\d+", "222", inputStr)
print(replacedStr)
replacedStr = re.sub("\d+", "222 ", inputStr,count=1)
print(replacedStr)
