import random
start = input("請決定數字範圍開始值: ")
end = input("請決定數字範圍結束值")
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True: 
    count += 1  #count + 1 快寫法
    num = input('請輸入數字: ')
    num = int(num)
    if num == r: 
        print("恭喜你猜對了! ")
        print("總共猜", count, "次")
        break
    elif num > r: 
        print("猜錯了!再小點! ")   
    else:  
        print("猜錯了再大點! ")
    print("已猜", count, "次") #重複性太高是不好的 