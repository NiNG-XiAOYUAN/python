"""
# 关键字实参
def describe_pet(pet_type,pet_name):
    '''显示宠物信息'''
    print(f"\ni have a {pet_type}.")
    print(f"my {pet_type}'s name is {pet_name}")
describe_pet('dog','ddd')
describe_pet(pet_type="ddd", pet_name="qqq")

"""
# 指定形参默认值
def describe_pet(pet_type , pet_name = "dog"):
    '''显示宠物信息'''
    print(f"\ni have a {pet_type}.")
    print(f"my {pet_type}'s name is {pet_name}")
describe_pet(pet_type  ='ddd')  

#################################################################
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
    full_name = fristname + lastname   
    return full_name.title()

#print('wang','long')

