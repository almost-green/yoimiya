#import random
import random as r
from random import random
#print(random.random())
#print(r.random())
#print(random())
def play():
    computer = r.randint(1,100)
    #print(computer)
    user = 0
    min = 1
    max = 100
    restart = 300
    while user != computer:
        user = int(input("請輸入" + str(min) + "到" +str(max) + "的整數:"))
        if user == computer:
            break
        if user < computer <= max:
             min = user
        if user > computer >= min:
            max = user
        if user == restart:
            break
    print("恭喜你猜對了!")
