#猜数游戏
import random
num= random.randint(1,100)
while True :
    num_input=input("please input a number")
    if not num_input.isdigit():
        print("please input a integer.")
    elif int(num_input) < 0 or  int(num_input) >= 100 :
        print("can only input number in one to one hunder")
    else:
        if num == int(num_input):
            print("your clever")
            break
        elif num > int(num_input):
        
            print("it\`s smoll")
        else:
            print("it\`s bigger")