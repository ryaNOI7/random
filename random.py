import random
r = random.randint(1, 100)
while True: 
    num = input('請輸入數字: ')
    num = int(num)
    if num == r: 
        print("恭喜你猜對了: ")
        break
    elif num > r: 
        print("猜錯了!再小點! ")
    else:  
        print("猜錯了再大點! ")