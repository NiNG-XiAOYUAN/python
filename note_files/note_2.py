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
"""
'''
# 使实参成为可选
def get_name(frist_name,last_name,middle_name = ""):
    """返回全名"""
    if middle_name:  # python 将非空字符串解读为true
        fullname = frist_name + middle_name + last_name
    else:
        fullname = frist_name + last_name
    return fullname.title()
musician = get_name("wang","yulong","www")  
print(musician)
'''
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

    
    

