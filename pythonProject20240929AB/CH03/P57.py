#更新字串指定位置內容
str1="This is Pytho.That is Java.This is SQLite"
print("字串1:",str1)
#假設你要取代第一個is也就是[5:7]，取代為--
print(str1[5:7])
str1[5:7]="--" #將會產生錯誤
print("字串2:",str1)
