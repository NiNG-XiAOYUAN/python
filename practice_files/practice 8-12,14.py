def topping_things(*topping):
    '''接收用户所输入的一切信息。'''
    print(f'you are ordered {topping} ')
toppings = topping_things('nn','dffb','tyy')
toppings = topping_things('asas','zxzx','rdy')


def users_profile(frist,last,**another_info):
    '''手机用户的姓和名以及其他信息。'''
    another_info['fname'] = frist
    another_info['lname'] = last
    return another_info 
user_profile = users_profile(frist = 'wang',last = 'long',age = 18,location = 'nnnn')
print(user_profile)

def cars_info(Manufacturer,type,**others_info):
    '''接收制造商和类型的两个必要型号。并接受其他任意信息。'''
    others_info["manufactuer"] = Manufacturer
    others_info['type'] = type
    return others_info
car_info = cars_info('bmw','x5',color = 'red',fijia = 'hhhh')
print(car_info)