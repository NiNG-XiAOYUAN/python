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
def describe_pet(pet_type , pet_name = "dog"):
    '''显示宠物信息'''
    print(f"\ni have a {pet_type}.")
    print(f"my {pet_type}'s name is {pet_name}")
describe_pet("ddd")   # "ddd"默认关联到位置实参 