i=10
def checkfun2( ):
  global i # 代表指定i為函數外的資料
  i=i+10
  print('函數內：',i)
  return
checkfun2( )
print('函數外：',i)
