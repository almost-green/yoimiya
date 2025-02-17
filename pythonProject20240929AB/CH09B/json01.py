import json
json1 = {'python': 'good', 'pcschool': 100, 'python-class':True,'ICQ': None}
json2 = json.dumps(json1, ensure_ascii=False)
json3=json2.encode('utf8')
print(json2)
