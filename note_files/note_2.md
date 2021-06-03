
# 关键字实参
def describe_pet(pet_type,pet_name):
    '''显示宠物信息'''
    print(f"\ni have a {pet_type}.")
    print(f"my {pet_type}'s name is {pet_name}")
describe_pet('dog','ddd')
describe_pet(pet_type="ddd", pet_name="qqq")


# 指定形参默认值
def describe_pet(pet_type , pet_name = "dog"):
    '''显示宠物信息'''
    print(f"\ni have a {pet_type}.")
    print(f"my {pet_type}'s name is {pet_name}")
describe_pet(pet_type  ='ddd')  

def describe_pet(pet_type , pet_name = "dog"):                  #
    '''显示宠物信息'''                                         #
    print(f"\ni have a {pet_type}.")                         #
    print(f"my {pet_type}'s name is {pet_name}")          #
# describe_pet("ddd")                                   # "ddd"默认关联到位置实参 
                    # 所以将没有默认值的放到第一个
######################################################
def make_shirt(size ,fonts = "i love python" ):
    '''指定尺码和样式'''
    print(f'\n your fonts is {fonts} and the size is {size}')
make_shirt ("12","ddd")
make_shirt (size='22',fonts='sss')
make_shirt ("大")
make_shirt ('中',fonts="i'love'python")
def describe_city (city , nation = "china"):
    '''默认一个国家的三个城市'''
    print (f"\n{city.title()} is in {nation.title()}")
describe_city("nanjing")
describe_city(city= "nanjing")
describe_city("shanghai")
describe_city("beijing",nation= "usa")


# 返回值    returu 语句
def got_name(fristname,lastname):
    '''返回全名'''
    full_name = fristname + lastname   #fullname = f"{fristname}{lastname}"
    return full_name.title()
musician = got_name("wang","yulong")     # 函数里没有print   return w将 full_name.title() 返回给调用函数的代码行  
                                         # 相当于 full_name.title() = got_name("wang","yulong") 
print(musician)
                        # print('wang','long')

import turtle
   
turtle.pensize(4)
turtle.pencolor('red')
    
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
    
turtle.mainloop()            

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))

"""
猜数字游戏

Version: 0.1
Author: 骆昊
"""
import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')

