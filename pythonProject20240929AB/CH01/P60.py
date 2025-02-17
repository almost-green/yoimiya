print('原本變數宣告方式')
a=10
b=3.14
c='測試'
print(a,b,c)
#a=10,b=3.14,c='test' #SyntaxError: can't assign to literal
a,b,c=10,3.14,'test' #Python的多個指定
print(a,b,c)
