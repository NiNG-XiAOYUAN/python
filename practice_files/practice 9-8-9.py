class User:
    '''用户星系'''
    def __init__(self,first_name,last_name,age):
        '''初始化星系'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 1
    
    def describe_user(self):
        '''描述'''
        print(f"the users information :\nfirstname : {self.first_name}\nlast_name : {self.last_name} ")
    def greet_user(self):
        '''问候'''
        print(f"""hello {self.first_name.title()}{self.last_name},welcome!
                \nyour age is {self.age}""")
    def increment_login_attempts(self,increment_attempts):
        '''login_attempts加1'''
        self.login_attempts += increment_attempts
    def reset_login_attempts(self):
        '''reset login attempts'''
        self.login_attempts = 0
    def attempts(self):
        print(f"you have loging {self.login_attempts} times")

class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        # self.privileges = ["can add post","can delete post","can ban user"]
        self.privileges = Privileges()

class Privileges:
    def __init__(self):
        "初始化属性"
    def show_privileges(self, adprivileges = ["can add post","can delete post","can ban user"]):
        "管理权限"
        adcprivileges = []
        for ad in adprivileges:
            adcprivileges.append(ad)
        print(f"""the admin  have following adprivileges:
                    \n{adprivileges }""")
admin = Admin("wang","long",22)
admin.privileges.show_privileges()

#9-9
class Car_3:
    '''模拟汽车的一个实例'''
    def __init__(self,make,model,year,):   
        '''初始化信息'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_start = 45  #一个默认的属性
    def get_descriptive_name(self):
        '''返回汽车信息'''
        long_name = f"{self.year} {self.make} {self.model} "
        return long_name.title()
    def read_odometer(self):
        '''公里数'''
        print(f"the car has road {self.odometer_start} meters ")    
    def update_odometer(self,mileage):
        '''指定里程表数
            禁止任何人回调
        '''
        if mileage >= self.odometer_start:
            self.odometer_start = mileage
        else:
            print(" you can't roll back an odometer! ")    
    def increment_odometer(self,miles):
        '''递增公里数'''
        if miles >= 0:     # 这样不写 会篡改 减小公里数！！！！
            self.odometer_start += miles     
        else:
            print("you can't change the odometer in an negative! ")    
    def fill_gas_tank(self):
        "汽车油箱容量"
        capacity = 32
        print(f"this car has a {capacity}L gas tank! ")

class Battery:
    "电瓶的相关信息"
    def __init__(self,battery_size = 78):
        self.battery_size = battery_size
    def describe_battery(self):
        "打印电瓶容量信息"
        print(f"this car has a {self.battery_size}--Kwh battery. ") 
    def get_range(self):
        "行驶续航里程"
        if self.battery_size ==  78:
            allrange = 260
        elif self.battery_size == 100:
            allrange = 315
        print(f"this car can go about {allrange} miles on a gull charge ")
    def upgrade_battery(self):
        """容量"""
        if self.battery_size != 100:
            self.battery_size = 100 


class Electriccar_3(Car_3):  # 括号里必须写父类名称 父类必须在当前文件中且位于子类之前
    '''car 中的电动车 子类父类关系'''
    def __init__(self, make, model, year):
        "初始化父类属性"
        "初始化电动车具有的属性"
        super().__init__(make, model, year)   ##### ！！！！！！
        # self.battery_size = 76   原方法
        self.battery = Battery()   # 实例做属性时的写法
    
    def fill_gas_tank(self):
        "电动车没油箱"
        print("电动车没油箱")
my_ecar_2 = Electriccar_3('changan','cs75',2019)
my_ecar_2.battery.describe_battery()
my_ecar_2.battery.get_range()
my_ecar_2.battery.upgrade_battery()
my_ecar_2.battery.get_range()















