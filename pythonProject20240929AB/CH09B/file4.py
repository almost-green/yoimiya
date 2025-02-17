f=open('data1.txt', 'r', encoding='UTF-8')
result = list( )
for line in f.readlines():
    line = line.strip()
    if not len(line) or line.startswith("#"):
        continue
    result.append(line)
#檔案讀取後的處理
result.sort()
print(result)
open('result-readlines.txt', 'w', encoding='UTF-8').write('%s' % '\n'.join(result))