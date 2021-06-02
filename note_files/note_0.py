'''
# 字符串S 统计每个单词的字母数量  有空格
s = "life is short you need python"
d={}
for letter in s:
    if letter.isalpha():
        if letter in d:
            d[letter] += 1
        else:
            d[letter]=1
print(d)
#import this#
name=["aadv","avd","23ava","4av","5avd","6avd"]
message = f"my first bicycle was a {name[0].title()}"
print (message)
# mingzi 
name=["zhangjijie","wangylong","yamgwei"]
for i in name :
    print(i)
    print( i +"，你个大傻逼")
# 自己的列表
transport=['moto','air plan','trian']
for i in transport:
    print("i would like to own a " + i)

transport.append("ducati")
print(transport)
last_ownd=transport.pop()
print(f"最后买的一辆，摩托车为：{last_ownd.title()}")
print(transport)

# visit=()
visit=["yuanyuan","weiwei","yaoyao","meimei"]
for i in visit:
    print("亲爱的"+ i +",欢迎您下周三下午九点来我家参加派对")
print(visit[3],"不能参加宴会")
visit[3] = "ningning"
print(visit)
for i in visit:
    print("亲爱的"+ i +",欢迎您下周三下午九点来我家参加派对")

print ("现在有多余的座位，再邀请三个人参加宴会")
visit.insert(0,"mama" )
visit.insert(2,"baba")
visit.append("jiejie")

for i in visit:
    print ("亲爱的" + i + ",欢迎您下周五来我家参加宴会")

print(" 由于餐桌无法按时到达，现在只能邀请两位嘉宾，抱歉")
print (visit)

for i in range (len(visit)):
    if i > 1:
        visit.pop()
        #print       haibuhuui  ("非常抱歉，亲爱的"+visit[i]+"由于座位减少的原因，不能邀请您来参加我的宴会了，请谅解。")
print(visit)
   
   
visit.sort()    # 永久无法回复原来顺序
print(visit)
visit.sort(reverse=True)
print (visit)

print(sorted(visit))
print(visit)     

# 想去的地方
place=["yulongxueshan","lijiang","caoyuan","yanchanghui","laojunshan"]
print(place)
print(sorted(place))
print(place)
print(sorted(place,reverse=True))
print(place)
place.sort(reverse=True)
print (place)
 ''' 
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

moshushi= ["dawei","aidixun","mzha"]
for i in moshushi:
    print(f"{moshushi.title(),is}")