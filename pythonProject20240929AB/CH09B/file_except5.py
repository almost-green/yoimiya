import os
class tryopenfile:
    def openfile(self, filePath):
        with open(filePath, 'w', encoding="utf8") as f:
            f.write("中文2")
        #self.handle = open(filePath, 'w')
       # self.handle.close()
    pass
if __name__ == "__main__":
    t = tryopenfile()
    filePath = 'test.txt'
#建立文件物件
#刪除文件
    print('success')