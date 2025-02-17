import re
hasPhoneNumber = re.compile(r'09\d{8}')
hasPID = re.compile(r'[a-zA-Z][12]\d{8}')
content = input("請輸入想檢查的內容:")
content = content.strip()
result = hasPhoneNumber.findall(content)
print("找到手機號碼", len(result), "組")
print("找到手機號碼", result)
print("隱藏手機號碼後的新內")
print("找到身分證字號", len(result), "組")
print("找到身分證字號", result)
print("隱藏身分證字號後的新內容:", hasPID.sub('-'*10, content))

