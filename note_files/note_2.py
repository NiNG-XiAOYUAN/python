"""
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


# 函数返回简单值    returu 语句
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

# 猜数字游戏

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


# 使实参成为可选
def get_name(frist_name,last_name,middle_name = ""):
    '''返回全名'''
    if middle_name:  # python 将非空字符串解读为true
        fullname = frist_name + middle_name + last_name
    else:
        fullname = frist_name + last_name
    return fullname.title()
musician = get_name("wang","yulong","www")  
print(musician)

# 函数返回字典（复杂）
def build_person(fristname,lastname,middlename = " "):   # 条件测试中none 相当于 false
    '''返回列表型信息'''                                                # 任何情况函数都会存储姓名，age相当于附加备注 可选
    if middlename:
        name_info = {"frist":fristname,"middlename":middlename,"last":lastname}
    else:
        name_info  = {"frist":fristname,"last":lastname}
    return name_info
aaa = build_person("wang","yulong")
print(aaa)
aaa = build_person(fristname="wang",lastname="yulong",middlename="eee")
print(aaa)
aaa = build_person("wang","yulong","uuu")
print(aaa)

while True:
    print("\nplease inter your name: ")
    print("(enter 'q' at any time to quit )")
    fristname = input ("fristname: ")

    if fristname ==  "q":
        break
    add = input("do you have middlename?(yes/no)")
    if add != "no":
        middlename = input ("middlename: ") 
        if middlename ==  "q":
            break      
        lastname = input ("lastname: ")
        if lastname ==  "q":
            break
        adding = build_person(fristname,lastname,middlename)   # 3个 直接用buid_person
        print(f'hello {adding }')
    else:
        lastname = input ("lastname: ")
        if lastname ==  "q":
            break
        adding = build_person(fristname,lastname)         #2个 提前 新建一个两个的函数 我不可能给人家加名字吧（如果用原来的）！！！   没弄呢
        print(f'hello {adding }')

# 向函数传递列表
def greet_users(names):
    '''列表调用函数 逐个打印问候'''
    for name in names:
        print(f"hello {name.title()}")
         
usernames = ['www','ttt','bbb']
greet_users(usernames)
"""
# 函数中修改列表
# 未打印的打印 并放到已经打印的 原来变空

def print_designs(unprinted_designs,complete_designs):
    """daying"""
    while  unprinted_designs:   #for addings in unprinted_designs: print (unprinted_designsqqq) 会多个['nihao'] 不符合题意
        addings = unprinted_designs.pop()
        print(f"we will complete {addings.title()}!")
        complete_designs.append(addings)
def complete_print(complete_design):
    print(f'the following things has pritned')
    for complete_design in complete_designsqqq:
        print (complete_design)

unprinted_designsqqq = ["nihao",'wohao','dajiahao']
complete_designsqqq = []
print_designs(unprinted_designsqqq,complete_designsqqq) #保留原材料 创建副本 print_designs(unprinted_designsqqq[:],complete_designsqqq)
complete_print(complete_designsqqq)
print (unprinted_designsqqq)
# 8-9
msg_txt = ['sd','nm','hk','uk']
def show_message(msgs):
    '''消息'''
    for msgs in msg_txt:
        print(f"toppings: {msgs.title()} ")
show_message(msg_txt)
print("fa 2")
sent_messages = []
def send_messages(msg_txt_1,sent_messages_1):
    '''ffff'''
    while msg_txt_1:
        addings = msg_txt_1.pop(0)
        sent_messages_1.append(addings)
    for adding in sent_messages:
        print (adding.title())
send_messages(msg_txt[:],sent_messages)
print(sent_messages)
print(msg_txt)
# 向函数传递任意数量的实参
def make_pizza(*toppings):   # * 创建空元组 所以可解释why输出为touple
    '''接受未知数量实参'''
    print(toppings)
make_pizza("ffffffff")
make_pizza('bgbg','dfdf','xcxc')
# 优化
def make_pizza(*toppings):  
    '''接受未知数量实参'''
    print('\nMaking a pizza with the following toppings: ')
    for topping in toppings:
        print(f'-{topping}')
make_pizza("ffffffff")
make_pizza('bgbg','dfdf','xcxc')
# 函数 结合使用位置实参和任意数量实参 
def make_pizza(size,*toppings):  
    '''只做披萨'''
    print(f'\nMaking a {size}-inch pizza with the following toppings: ')
    for topping in toppings:
        print(f'-{topping}')
make_pizza(14,"ffffffff")
make_pizza(8,'bgbg','dfdf','xcxc')

# 函数 使用任意数量关键字实参  不知道函数接受的是什么样的信息
def  buid_profiles(frist,last,**users_info):
    '''创建一个字典，其中包含我们知道的有关用户的一切。'''
    users_info['fname'] = frist
    users_info['lname'] = last
    return users_info
user_info = buid_profiles('sss','ddd',location = 'sdv',field = 'bnbn')
print (user_info)

#函数与模块。
# 参考pizza.py making_pizzas.py
'''
import pizza    #我们提前有一个pizza.py文件,必须与本文件所在同一目录。才能成功调用。
pizza.make_pizza(15,"dhfvdf")
'''
# 导入特定的函数
# 参考pizza.py making_pizzas.py
from pizza_1 import make_pizza  #例如pizza.py 文件中有两个以上函数。指定导入某一函数。
make_pizza(15,"piiiivdf")       # 注意上面(line 221)与这里的区别。

#使用 as 给函数指定别名  # 函数与程序中有冲突名字 或为了便于记
from pizza_1 import make_pizza as mmp
mmp(15,"ggggvdf")
#使用 as 给函数指定别名
import pizza as p
p.make_pizza(14,"dhfghjhvdf")
# 调用模块中 所有函数
from pizza import *