text = '''python與中文
1. 我們來試試看中文儲存能力。
2. 許這個字會有編碼衝突風險。
3. 犇這個字必須是utf8編碼才有。'''
print(text ,file=open('data1.txt','w',encoding='utf-8'))
#print(text ,file=open('data2.txt','w'))