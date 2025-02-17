import json
data = { }
data['people'] = [ ]
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})

data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
json2 = json.dumps(data)
file=open('score.json','w',encoding='utf-8')
file.write((json2))
