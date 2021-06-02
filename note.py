'''
student_name="wanglong"
print (f'Hello {student_name.upper()},would you like to learn some python today?')
# 实现字符串的输入，输出及字符串空格的删除。
famous_name="wanglong"
famois_novel="you can you up,no can no bb"
print (f'hello {famous_name.title()}once said,"{famois_novel.title()}"')
massage=f'hello{famous_name} once said,"{famois_novel}"'
print(massage)
famous_person=" wang long "
print(famous_person)
print(f"{famous_person.lstrip()}")
print(f"{famous_person.rstrip()}")
print(f"{famous_person.strip()}")
########################################################################
# 另一个作业。
name=['qw','er','ty','ui']
print(name[0].title())
print(f'你好 {name[0].title()},"你好"')
name.append('vvvv')
print(name)
name.insert(0,'hh')
print(name)
del name[1]
print(name)
#又是另一个作业。
visit=['aaa','bbb','ccc']
print(f'hello {visit[0].title()},can you join my party?')
print(f'hello {visit[1].title()},can you join my party?')
print(f'hello {visit[2].title()},can you join my party?')   
    #修改嘉宾名单。
remove_people="ccc"
visit.remove(remove_people)
print(f'bbb{remove_people.title()},can not coming,i will interver ddd join')
print("this is now paper")
visit.append("ddd")
print(visit)
#使用POP方法删除。默认最后一个
pop_people=visit.pop()
print(f'bbb{pop_people.title()},can not coming,i will interver ddd join')
pop_people=visit.pop()
print(f'bbb{pop_people.title()},can not coming,i will interver ddd join')
print(visit)
del visit[0]
print (visit)
# 使用送sort（）对列表永久排列 按字母顺序
car=['aa','dd','cc']
print(car.sort())
print(car)
print(car.sort(reverse=True))
print(car)
car .reverse()
print(car)
x=len(car)
print(x)
# 练习 3-8
want_place=['yunnan','cneimenggu','shanghai','chengdu','beijin']
print(want_place)
print(sorted(want_place))
print(want_place)
print(sorted(want_place,reverse=True))
print(want_place)
want_place.reverse()
print(want_place)
want_place.reverse()
print(want_place)
want_place.sort()
print(want_place)
want_place.sort(reverse=True)
print(want_place)
print(len(want_place))
# 索引列表没有的元素 会出错  看下面
want_place=['yunnan','cneimenggu','shanghai','chengdu','beijin']
print(f'这里一共有{len(want_place)}个元素，而我要索引第{len(want_place)}个 就会出错，解决办法如下')
print("liru:")
print("print(want_place[5]) huichucuo\n所以这样解决")
print ("print(want_place[-1])")
print("列表为空时，这种方法也不行，会出错\nke可以先将列表长度打印出来再解决问题")
# 用循环操作列表
print ("用循环操作列表，还是之前的列表")
want_place=['yunnan','cneimenggu','shanghai','chengdu','beijin']
for want_place in want_place:
    print(want_place)
    print(f'{want_place.title()},that was a great place!')
    print(f'i want to see you ,{want_place.title()}\n')
print("thank you ,everyone!")
print("另一个例子：")
favorite_animals=['cat','dog','sheep']
for animal in favorite_animals:
    print(f"A {animal} would make a great pet")
print("any of them are so cute")
#创建数值列表
print("# 创建数值列表")
for value in range(1,6):
    print(value)
for value in range(6):
    print(value)
print("使用range()生成的数  创建成为数字列表哦####")
number=list(range(1,6))
print(number)
print("还可指定步长 1-10 的偶数 range(2，11，2)")
number_1=list(range(2,11,2))
print (number_1)
print ("空列表存储某些数的平方 如下：")
squares=[]
squares_1=[]
for number_3 in range (0,12,2):
    square=number_3 **2
    squares_1.append(number_3)
    squares.append(square)
print(squares_1)
print (squares)
print ("也可这样")
exit
squares=[]
squares_2=[]
for number_3 in range (0,12,2):
    squares_2.append(number_3)
    squares.append(number_3 **2)
print(squares_2)
print (squares)
# 对数字类列表进行简单统计计算
digits=[1,1,2,5,5,3,4]
print(min(digits),max(digits),sum(digits))
# 列表解析 快速生成列表
print("如生成squares用 squares_3=[value**2] for valve in range(0,12,2)")
squares_3=[value**2 for value in range(0,12,2)]
print (squares_3)
# 练习
print("练习")
print(list(range(1,21)))
shu=list (range(1,1000001))
#print (shu)
#for i in shu:
 #   print (i)
print(min(shu))
print(max(shu))
print (sum(shu))
list_1=list(range(1,20,2))
print (list_1)
for i  in list_1:
    print (i)
exit
shuu=[]
#shu_2=[(value % 3 )==0 for value in range(3,31)]
for i in range(3,31):
    if i % 3==0:
        shuu.append(i)
print (shuu)
shus=[value**3 for value in range(1,11)]
for i in shus:
    print (i)
print (shus)    
exit 
shuuu=[]
shuuu_1=[]
for i in range(1,11):
    value=i**3
    print(i)
    shuuu_1.append(i)
    shuuu.append(value)
print (shuuu_1)
print (shuuu)
# 使用列表的一部分---切片
print("# 使用列表的一部分---切片")
print (shuuu_1)
print (shuuu_1[1:3])     #不包含第三个索引  和range相似
print (shuuu_1[0:3]) # 不标开头和结尾 默认 第一个或最后一个 
print (shuuu_1[:3])
#最后3个
print (shuuu_1[-3:])
#查看前三个

for ggg in shuuu_1[0:3]:
    print (ggg)
#复制列表
my_food=['qqq','aaa','zzz','www','hhh']

friend_food=my_food[1:2]  #两者互不影响       之后有个深度复制
my_food.append('ppp')
print(my_food)

friend_food.append('ooo')
print(friend_food)

   # ruguo
friend_food=my_food    # 会使两个结果相同应为他猛之间有关联
my_food.append('ppp')
print(my_food)     
print(friend_food)
# 练习
print(f'the frist three items in the list are:{my_food[0:3]}')
print(f'the frist three items in the list are:{my_food[1:4]}')
print(f'the frist three items in the list are:{my_food[2:5]}') 

# 元组   不可修改 字符 字符串必须 引起来
couple_1=('a','d','dff',1,5,)
for de in couple_1:
    print(de)
print ('lianxi')
couple_2=(1,2,3,4,5,)
for num in couple_2:
    print (num)
couple_2=(1,2,8,9,5)
for num in couple_2:
    print(num)
############################################################################
#  if  语句 
cars_1=['BMW','AUDI','TOTO','MAZDA']
for car in cars_1:
    if car =='BMW':
        print(car.lower())
    else:
        print (car.title())
aaa="sss"
if aaa!="sss":
    print ('error')
else:
    print ("success")
car ='BMW'
if car in cars_1:
    print ("true")
car="wwwww"
if car not in cars_1:
    print (f'the {car.title()} are not in the cars_1')

#  bool 表达式  只有ture false
car="sssssss"
print("is car=='sssssss'? i predict true")
print (car=="sssssss")
print ("\nis car=='audi?,i predict false")
print(car=='audi\n\n\n\n\n')

#练习
aq='audi'
aw='Audi'
age=12
agr=32
car_1='BMW'
cars_1=['BMW','AUDI','TOTO','MAZDA']
print(aq=='audi')
print (aw=='audi')
print (aw.lower()=='audi')
if age > 33:
    print ("yes")
if age < 33:
    print ("yes")
if agr == 32:
    print ("yes")
if age ==33:
    print ("yes")
if age > 33and agr <12:
    print ("yes")
if age > 10 or agr <12:
    print ("yes")
if car_1 in cars_1:
    print('yes')
if car_1  not in cars_1:
    print('yes')
# if-else 语句
age= 12
if age >= 12:
    print ("yes ")
else:
    print ("no ")
# if -elif-else  许多个条件
age=34
if age <=34:
    x=1
elif age==34:
    x=2
else:
    x=3
print(f"you can get {x} yuan")
 
# p57 lianxi 
aliens_color="green"
if aliens_color=="green":
    print("this player get five code")
else:
    print ("the player code is 0")
aliens_color_1="green"
if aliens_color_1 !="green":
    print("the player get five code")
else:
    print ("the player code is 10")

favorite_fruits=['apple','bnana','water','poper']
if "apple" in favorite_fruits:
    print ("\nyes")
if "bnana" in favorite_fruits:
    print ("yes")
if "water" in favorite_fruits:
    print ("yes")
if "apple" not in favorite_fruits:
    print ("yes")
if "shuihh" not in favorite_fruits:
    print ("yes")
for favorite_fruit in favorite_fruits:
    if favorite_fruit =="apple":   # 假如没有了apple
        print("this food is over")
    else:
        print (f"adding {favorite_fruit}")
print ("\nenjoy you food")

# 如果列表为空
requested_toppings=[]      # 列表不为空 返回true
if requested_toppings:           #此时列表为空或 相当于if后是false 
    for requested_topping in requested_toppings: #后面代码直接跳过 进入else
        print (f'you adding {requested_topping}')
    print ("you pizz was done")
else:
    print("\nASre you wang to order a pizz?") 
# 使用多个列表   解决用户点的东西  而我没有
available_toppings=['mushrooms','olives','green papper',
                      'pepperoni','pineapple','cheese']
requested_toppings=['mushrooms','cheese','french']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print (f'Adding {requested_topping}.')
    else:
        print(f"we don\'t have {requested_topping}")
print("\n Finish you pizza")

#lianxi
users_name=['wanglong','yangwei','liuyao','sunning','yanghui','admin']

for user_name in users_name:
    if user_name =="admin":
        print(f'Hello {user_name},would you like eat some apple?')
    else:
        print(f"\nHello {user_name},thank you for your logging in again.")
# 假如 列表没有任何用户  空列表
users_name=[]
if len(users_name) > 0:
    for user_name in users_name:
        if user_name =="admin":
            print(f'Hello {user_name},would you like eat some apple?')
        else:
             print(f"Hello {user_name},thank you for your logging in again.")
elif len(users_name) == 0:
        print("we need to find some users!")

# 确保用户名独一无二     简直完美！！！！！
current_users=['wanglong','yangwei','liuyao','sunning','yanghui','admin']
new_users=[input("输入名字")]
for new_user in new_users:
    if new_user.lower() in [current_user.lower() for current_user in  # 列表解析
                                     current_users]:
        print (f"the {new_user} has been used! Please enter another name.")
    elif new_user not in users_name:
        current_users.append (new_user)
print(current_users)

# 序数
list_2=list(range(1,10))
for number in list_2:
    if number ==1:
        print(f"\n {number} th")
    elif number ==2:
        print(f"\n{number} th")    
    elif number ==3:
        print(f"\n{number} th")   
    elif number ==4:
        print(f"\n{number} th")   
    elif number ==5:
        print(f"\n{number} th")  
    elif number ==6:
        print(f"\n{number} th")   
    elif number ==7:
        print(f"\n{number} th")   
    elif number ==8:
        print(f"\n{number} th")   
    else:
        number ==9
        print(f"\n{number} th")   
 ###################################################     
# 学习字典
people_1={'black':'2','white':3,'yellow':"five"}
print(people_1['yellow'])
print(people_1['black'])
# 读取black 获得的分数
print(f'the {people_1} get {people_1["black"]}.')     # weiwancheng ??????


alien_0={'color':"yellow","points":5}
print (alien_0)
alien_0["x_position"]=0   #添加键值对
alien_0["y_position"]=33
print(alien_0)                
                             # 键不可修改 修改值可以
print(alien_0)
alien_0["color"]="green"
print(alien_0)
#移动
print(f'original position is {alien_0["x_position"]} ]')
alien_0["speed"]="medium"
if alien_0["x_position"]=="medium":
    x_adding = 1
elif alien_0["x_position"] == "slow":
    x_adding = 2
else :
    x_adding = 3
alien_0["x_position"]=alien_0["x_position"]+x_adding
print(f"new position is {alien_0['x_position']}")   # 注意单双引号
# 如何删除键值对
print(alien_0)
del alien_0["points"]
print(alien_0)
# get（*,**） 访问值   解决不确定访问的键 并不存在而报错
# 找*  不存在则指定返回**   （没有* 不指定**  则返回 none）!!!!!!
print(alien_0)
 ##  print (alien_0["points"]) 没有points会出错
point_value = alien_0.get('points',"no points value assined")
print(point_value)
color_value = alien_0.get('color',"no color value assined")
print(color_value)

# lianxi   6-1
greatfriend = {'first_name':'wang','last_name':'long',
                           'age':'22','city':'nanjing'}
print(greatfriend)
# lianxi 6-2
greatfriend_number = {'aa':'12','bb':'34','cc':'25','dd':'98'}
print(greatfriend_number)
 # 老方法逐个打印
cihuibiao = {'number':'数字','float':'浮点数','complex':'复数',
                        'str':'字符串',r'\t':'制表符','\n':'换行'}
print(f' number:" {cihuibiao["number"]}"')
print(f' float:" {cihuibiao["float"]}"')
print(f' complex:" {cihuibiao["complex"]}"')
print(f' str:" {cihuibiao["str"]}"')
#print(f' r\t:" {cihuibiao["\t"]}"')
#print(f' r\n:" {cihuibiao["\n"]}"')

 #for 循环遍历打印
for key,value in cihuibiao.items():
# for a,b in ..... 也可以
    print(f'\nkey: {key}')
    print(f'\nvalue: {value}')

 #   keys() 方法遍历 所有键值
for name in cihuibiao.keys():#等于 for name in cihuibiao：
    print(name)

greatfriend_number = {'aa':'12','bb':'34',
                      'cc':'12','yulong':'w98',
                      'name':'wanglong',}
my_number = ['name','yulong']
for name_1 in greatfriend_number.keys():
    print(f'hi {name_1.title()}')         # 在朋友里 只打印 键
    if name_1 in my_number:       # 同时在我的里面 同时打印键值
        name = greatfriend_number[name_1].title()
        print(f'\t{name.title()},i see you love {name}！')

# 遍历字典 列表都是按插入顺序的
# 特定顺序 遍历字典 sorted（） 临时按字母顺序
favorite_laguages = {
    'jen':'python',
    'sarah':'c++',
    'edward':'ruby',
    'wang':'python',
}
for name in sorted(favorite_laguages.keys()):
    print(f'{name.title()},thank you for your poll!')

 #    values() 方法遍历 所有值  
greatfriend_number = {'aa':'12','bb':'34',
                      'cc':'12','yulong':'w98',
                      'name':'wanglong',}
    # 现 用此方法 只要统计有哪些语言  不要重复出现                  
for name_1 in greatfriend_number.values():
    print(f'hi {name_1.title()}') 
  #  此方法无法避免 当有许多相同的 value 所以用 集合set() ---元素独一无二
for name_1 in set(greatfriend_number.values()):  
    print(name_1.title())
# 花括号创建集合
language = {'python','c','java','vb','python'}
print(language)    # {'vb', 'python', 'c', 'java'}  元素独一无二        

# lianxi 6-5
river_nation = {'huanghe':'china','nile':'egypt','mixixi':'usa'}
for river in river_nation.keys():
    print (f'{river.title()}')
    print (f'{river_nation[river].title()}')
    print (f'The {river.title()} runs thought {river_nation[river].title()}')
# lianxi 6-4
river_nation_wantgo = {'huanghe':'china','nile':'egypt','mixixi':'usa'}
river_nation_nogo = {'mixixi':'usa'}
for place in river_nation_wantgo.keys():
    if place in river_nation_nogo :
        nation_nogo = river_nation_wantgo[place].title()
        print(f'The {place.title()} in {place.title()},has not go !')
# ###################  n 嵌套
################   列表存储字典
alien_1 = {'color':'green','points':'5'}
alien_2 = {'color':'yellow','points':'10'}
alien_3 = {'color':'red','points':'9'}
aliens = [alien_1,alien_2,alien_3]
for alien in aliens:
    print (alien )
#接下来创建一个特别多外星人的列表。
aliens_1 = []
for aliens_number in range(30):
    new_alien = {'color':'green','points':'5'}
    aliens_1.append(new_alien)
for aliens in aliens_1[:5]:
    print(aliens)
print(f'\ntotal number of aliens is {len(aliens_1)}')
# 更改前三个
for aliens in aliens_1[:3]:
    if aliens["color"] == "green":
        aliens["color"] = "yellow"
        aliens["speed"] = "medium"
        aliens["points"] = 10
    elif aliens["color"] == "yellow":
        aliens["color"] = "red"
        aliens["speed"] = "fast"
        aliens["points"] = 17
for aliens in aliens_1[:5]:
    print(aliens)
############   字典存储列表
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheeese'],
}
print(f"you have ordered a {pizza['crust']}-crust pizza!"
           "with the following toppings ")
for topping in pizza["toppings"]:
    print("\n"+ topping)

favorite_laguages_2 = {
    'jen':['python','vb'],
    'sarah':['c++'],
    'edward':['ruby','java'],
    'wang':['python'],
}

for name,languages in favorite_laguages_2.items():
    if len(languages) > 1:
        print (f"{name.title()} favorite language are:")
        for language in languages :
            print("\t" + f'{language.title()}' )
    elif len(languages) == 1:
        print (f"{name.title()} favorite language are:{language.title()}")
             
############   字典存储字典
many_users = {
    'wanglong':{
        'first':'wang',
        'last':'long_Q',
        'location':'nanjing',
    },
    "sunning":{
        'first':'sun',
        'last':'ning_w',
        'location':'yinchuan',
    },
}
for username,user_info in many_users.items():
    print(f'\nUser name : {username.title()}')
    full_name = f'{user_info["first"]}{user_info["last"]}'
    user_location = f'{user_info["location"]}'
    print(f'Full name is {full_name.title()}')
    print(f'Location is {user_location.title()}')

# liannxi 6-7
greatfriend_1 = {'first_name':'wang','last_name':'long',
                           'age':'22','city':'nanjing'}
greatfriend_2 = {'first_name':'chen','last_name':'cheng',
                           'age':'21','city':'yangzhou'}
greatfriend_3 = {'first_name':'wei','last_name':'wei',
                           'age':'23','city':'baoding'}
people_2 = [greatfriend_1,greatfriend_2,greatfriend_3]
for friend in people_2:
    print(friend)
#lianxi 6-8
pet_1 = {'type':'dog','master':'wanglong'}
pet_2 = {'type':'cat','master':'yangwei'}
pet_3 = {'type':'sheep','master':'sunning'}
pet_4 = {'type':'brid','master':'liuyao'}
pets = [pet_1,pet_2,pet_3,pet_4]
for pet in pets :
    print (pet)

# lianxi 6-9
favorite_places = {
    "wanglong":["chengdu"],
    "sunning":['nanjing','beijing'],
    "yangwei":['tianjing','sichuan','xizang'],
}
for people,places in favorite_places.items():
    print(f"The {people.title()} want go following places:")
            #= {favorite_places[people]}
    for place in places :
        print("\n" + f'{place.title()}')
#  lianxi 6-10
greatfriend_number = {'aa':[12,14,5],
                      'bb':[2,7,32],
                      'cc':[10,21,6,9],
                      'dd':[8,5,6,4,12],}
for name , numbers in greatfriend_number.items():
    if len(numbers) > 1:
        print(f"the {name.title()}'s favorite numbers are: ")
        for number in numbers:
            print ("\n" + f'{number}')

# lianxi 6-11
cities={
    'beijing':{
        'country':'china',
        'population':'14 million',
        'fact':'aaaaa',
    },
    'pari':{
        'country':'franch',
        'population':'10 million',
        'fact':'bbbb',
    },
    'dongjing':{
        'country':'japan',
        'population':'0.2 million',
        'fact':'cc',
    },
}
for city,citys_info in cities.items():
    print(f"There are some information about {city.title()}:")
    country_full = f'country: {citys_info["country"]}'
    population_1 = f'population: {citys_info["population"]}'
    fact_1 = f'fact: {citys_info["fact"]:}'
    print ("\n" +f'{country_full.title()}')
    print ("\n" + f'{population_1.title()}')
    print ("\n" + f'{fact_1.title()}')
    ##############################################################

# input（） 获取用户输入
message = input("please input some thing ")
print(message)
prompt = "please tell us what\'s your name,and we will give you some "
prompt += "\ngifts "
message_1 = input(prompt)
print (prompt)
# int（） 获取数值输入 或程序此时只允许输入数值 但由于input方法得到的是字符串 -转化
#********  将数值输入用于计算和比较前，务必将其转化为数值

age = input("how old are you? ")
print (type(age ))    # <class 'str'> 
age = int(input("how old are you? "))
print(type(age))        # <class 'int'>

#练习7-1 7-2 7-3
message_2 = input("what kind of the car would you buy? ")
print (message_2)

food_number = int(input("how many peopel totally? "))
if food_number > 8:
    print("there are no seats avalilable now ")
elif food_number <= 8:
    print ("there are have avalilable seats")

input_number = int(input("please input a number "))
if input_number % 10 == 0:
    print ("this number can divisible by ten! ")
elif input_number % 10 != 0:
    print ("this number can not divisible by ten ")


# while ################
current_number = 2
i = 0
while current_number <= 6:
    print(current_number)
    current_number += 1
    i += 1
print(f"程序循环了 {i} 次")

# 自定义退出的触发值
prompt = "\nTELL ME SOME THINGAND I WILL REPEAT IT BACK TO YOU。"
prompt += "\nENTER 'QUIT' TO END THE PROGRAM。"
message_3 = ""
while message_3 != "quit":
    message_3 = input(prompt )
    if message_3 != "quit":
        print(message_3)              

#标志  flag 用于判断整个程序是否处于活动状态。
prompt = "\nTELL ME SOME THINGAND I WILL REPEAT IT BACK TO YOU。"
prompt += "\nENTER 'QUIT' TO END THE PROGRAM。"
now_active = True  #创建一个标志
while now_active:
    message_3 = input(prompt)
    if message_3 == "quit":
        now_active = False    #满足任意条件都会停止可以用这样的。
    else:                   # 或用 elif 写多个条件
        print(message_3)

# 使用break 退出循环
prompt = "\nTELL ME SOME THINGAND I WILL REPEAT IT BACK TO YOU。"
prompt += "\nENTER 'QUIT' TO END THE PROGRAM。"
now_active = True  #创建一个标志
while now_active:
    message_3 = input(prompt)
    if message_3 == "quit":
        break                   # 和面的例子有点不一样。
    else:                   # 或用 elif 写多个条件
        print("if youo want to quit please input 'quit'")

# 使用 continue 
current_number = 0
while current_number < 15:
    current_number += 1
    if current_number % 2 != 0:
        continue
    print(current_number)

#current_number = 0
#while current_number < 15:
 #   if current_number % 2 != 0:
  #      current_number += 1
   #     continue
    #print(current_number)
# lianxi 7-4
prompt = "先选择您要搭配的配料: "
message = ""
order = ""
while True :
    message = input(prompt)
    if message != "quit":
        print(f" you have order the {message.title()}")
    elif message ==  'quit':
        print ("you have finished your order!")
        break


# lianxi 7-5
prompt = "please input your age: "
message = ""
active = True
while active:
    age = int(input(prompt))
    if age < 3:
        print("你的票价为0元 ")
        active = False
    elif age >= 3 and age <=12 :
        print("你的票价是十元。")
        active = False
    elif age > 12:
        print("你的票价是16元。")
        active = False
   
#法 2
prompt = "please input your age: "
message = ""

while True:
    age = int(input(prompt))
    if age < 3:
        print("你的票价为0元 ")        
    elif age >= 3 and age <=12 :
        print("你的票价是十元。")       
    elif age > 12:
        print("你的票价是16元。")
        break
    #if  message == 'quit':
     #   print("exit")
      #  break 


#!!!!!! while 循环处理列表 字典
#一个待验证的列表   一个已验证的  将待验证的验证完同时加入到 已经验证的列表
unconfirmed_uesrs = ['wanglong','yangwei','sunning']
confirmed_users = ['qqqqqqqqq']
while unconfirmed_uesrs:
    current_user = unconfirmed_uesrs.pop(0)
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
print("all confirmed users: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
# while 循环  用remove（）删除特定值
pets = ['dog','sheep','cat','dog','cat']
remove_value = "cat"
print(pets)
while remove_value in pets:
    pets.remove(remove_value)
print(pets)

# 使用用户输入填充字典。
responses = {}
response_active = True     # 设置一个标志。
while response_active:
    name = input("\nwhat's your name? ")
    response = input("\nwhere are you want to go? ")
    responses[name] = response
    repeat = input("\n能否接受下一个调查? (yes/ no) ")
    if repeat == "no":
        response_active = False
print ("\n---poll results---")
for name,response in responses.items():
    print(f"{name} would like go {response}.")
print(responses)

# liasnxi 7-8
sandwish_orders = ['aaaa','pastrami','bbb','pastrami','ccc',
                    'ddd','pastrami','eee','pastrami','wert',]
finished_sandwichs = []
print ("pastrami meiyouole")
while sandwish_orders:
    orders = sandwish_orders.pop()
    if orders == "pastrami":
        continue
    finished_sandwichs.append(orders)
    print(f"i made your {orders} sandwich")
print(finished_sandwichs)
# lianxi 7-10
dream_place_survey = {}
survey_active = True
while survey_active:
    name = input("\nwhat's your name? ")
    place = input("where would you go? ")
    dream_place_survey[name] = place
    repeat = input("\n能否接受下一个调查? (yes/ no)? ")
    if repeat == "no":
        survey_active = False
print ("this is the survey results: ")
for name,place in dream_place_survey.items():
    print(f"{name.title()} want to go {place.title()}")
'''
############################################################  函数
def hello_users():
    '''问候语'''
    print("hello world")
# 进阶    向函数传递信息
def hello_users(username):
    '''问候语'''
    print(f"hello，{username.title()} coning there! ")    
name = "wanglong"
hello_users('wanglong')   
hello_users(name)  
#lianxi 8-1
def display_message():
    '''学习内容'''
    print("本章学习函数")
display_message() 
#lianxi 8-2
def favorite_book(title):
    '''我的书'''
    print(f"One of my favorite books is {title.title()}")
favorite_book("gagafgafd  sd")   
# 传递实参 有位置实参，关键词实参
  #位置实参
def describe_pet(pet_type,pet_name):
    '''显示宠物信息'''
    print(f"\ni have a {pet_type}.")
    print(f"my {pet_type}'s name is {pet_name}")
describe_pet('dog','ddd')



