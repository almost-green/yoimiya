import os
sysDrv = os.environ["HOMEDRIVE"]
userHomeDrv = os.environ["HOMEPATH"]
try:
    os.chdir('/Users/User')
    os.chdir(sysDrv+userHomeDrv)
except:
    print('不能切換資料夾')
print(os.getcwd())