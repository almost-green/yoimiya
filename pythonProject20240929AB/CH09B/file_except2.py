import os
class tryopenfile:
    def openfile(self, filePath):
        self.handle = open(filePath, 'w')
       # self.handle.close()
    pass
if __name__ == "__main__":
    t = tryopenfile()
    filePath = 'test.txt'
    t.openfile(filePath)
    try:
        os.remove(filePath)
    except PermissionError:
        print("程序無法存取檔案，因為正由另一個程序使用中")
#建立文件物件
#刪除文件
    else:
        print('success')