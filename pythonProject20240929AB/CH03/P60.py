#更新字串指定位置內容-另一種方式
str1="This is Pytho.That is Java.This is SQLite"
print("字串1:",str1)
str1=str1[:5]+"--"+str1[7:]
print("字串2:",str1)
