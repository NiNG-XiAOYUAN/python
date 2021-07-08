# lianxi 8-6
def city_country(city,country):
    '''接收国家和城市'''
    #city = input("please enter a city's name: ")
    #country =  input("please enter a country's name: ")
    city_country_info = f' "{city.title()},{country.title()}" '
    return city_country_info
print(city_country('aaa','fff'))
print(city_country('kkk','ccc'))
print(city_country('hhh','yyy'))
'''
# 8-7                        3个最好都有
def make_album(names,sings,number = " "):     # 不能老是在函数里输入输出 
    """cfccccc"""
    if number:
        album_info = {"name":names ,"sing":sings,"number":number}
    else:
        album_info = {"name":names ,"sing":sings}
    return album_info

#    album_info = {"name":names ,"sing":sings,}             
#    if number:   #name_sing = make_album("sss","ggg","ccc") you {'name': 'sss', 'sing': 'ggg', 'number': 'ccc'}
#        album_info["number"] = number
#    return album_info
name_sing = make_album("sss","ggg","ggg")       # {'name': 'sss', 'sing': 'ggg', 'number': ' '}
print(name_sing)
'''
def make_album(names,sings,number = None):#原来没有调用可加          不能老是在函数里输入输出
    """cfccccc"""
#    if number:
#        album_info = {"name":names ,"sing":sings,"number":number}
#    album_info = {"name":names ,"sing":sings}
#    return album_info

    album_info = {"name":names ,"sing":sings,}           
    if number:
        album_info["number"] = number
    return album_info
name_sing = make_album("sss","ggg")         
print(name_sing)

# 8-8
active = True
while active:
    name_1 = input("输入名字：")
    print("enter 'Q' at any time to quit! ")
    if name_1 == "Q":
        break
    sing_1 = input("输入歌曲名字：")
    if sing_1 == "Q":
        break
    this = make_album(name_1,sing_1)
    print(this)




