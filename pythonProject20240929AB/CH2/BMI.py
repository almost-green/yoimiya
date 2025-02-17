name = input('請輸入你的名字')
h = float(input('請輸入你的身高'))
w = float(input('請輸入你的體重'))
if h>0 and w>0:
    bmi = w / (h**2)
    d = 'your BMI is'
    e = '您的身材體重過輕'
    f = '您的身材體重正常'
    g = '您的身材體重過重'
    i = '您的身材體重輕度肥胖'
    j = '您的身材體重中度肥胖'
    k = '您的身材體重重度肥胖'
    print(d, bmi)
    if bmi < 18.5:
        print(name+e)
    elif bmi >= 18.5 and bmi < 24:
        print(name+f)
    elif bmi >= 24 and bmi < 27:
        print(name+g)
    elif bmi >= 27 and bmi < 30:
        print(name + i)
    elif bmi >= 30 and bmi < 35:
        print(name+j)
    else:
        print(name+k)
else:
    print('請輸入正確的數值')

