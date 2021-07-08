# 类    定义一大类对象都有通用行为
# 基于类创建对象时（‘’‘’实例化‘’‘’），每个对象都有通用行为

# 创建类 适用类
class Dog:
    """模拟小狗的尝试"""
    def __init__(self,name,age):  # 形参 self必不可少，在首位
        """"初始化 name age """
        self.name = name
        self.age = age 

    def sit(self):
        """蹲下命令"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """打滚命令"""
        print(f"{self.name} rolled over!")
my_dog = Dog('why',5)   #实例化
print(f"my dog's name is {my_dog.name} is {my_dog.age} years old.")
my_dog.sit()     #调用方法 ，下同
my_dog.roll_over()
your_dog = Dog('dfdf',55)
print(f"your dog's name is {your_dog.name} is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()

# lianxi 9-1 --3
class Restaurant:
    '''餐厅'''
    def __init__(self,restaurant_name,restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        #self.name = restaurant_name
       # self.type = restaurant_type
    
    def describe_restaurant(self):
        '''描述餐厅'''
        print(f"the restaurant name is {self.restaurant_name} \tthe type is {self.restaurant_type}")
    
    def open_restaurant(self):
        '''状态'''
        print(f"the restaurant {self.restaurant_name} is openning ")
restaurant_1 = Restaurant("sdsd","vbvb")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_2 = Restaurant("fgfg","aaaaa")
restaurant_2.describe_restaurant()

class User:
    '''用户星系'''
    def __init__(self,first_name,last_name,age):
        '''初始化星系'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def describe_user(self):
        '''描述'''
        print(f"the users information :\nfirstname : {self.first_name}\nlast_name : {self.last_name} ")
    def greet_user(self):
        '''问候'''
        print(f"hello {self.first_name}{self.last_name},welcome! \nyour age is {self.age}")
user_info = User("aaa","dddd",22)
user_info.describe_user()
user_info.greet_user()

#使用类 和实例
"""
class Car_1:
    '''模拟汽车的一个实例'''
    def __init__(self,make,model,year):   
        '''初始化信息'''
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        '''返回汽车信息'''
        long_name = f"{self.year} {self.make} {self.model} "
        return long_name.title()
my_car = Car_1("hongi","h9",2020)
print(my_car.get_descriptive_name())


## 属性指定默认值
class Car_2:
    '''模拟汽车的一个实例'''
    def __init__(self,make,model,year,):   
        '''初始化信息'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0  #一个默认的属性
    def get_descriptive_name(self):
        '''返回汽车信息'''
        long_name = f"{self.year} {self.make} {self.model} "
        return long_name.title()
    def read_odometer(self):
        '''公里数'''
        print(f"the car has road {self.odometer} meters ")

my_car = Car_2("hongi","h9",2020)
print(my_car.get_descriptive_name())
my_car.read_odometer()
# 修改属性的值

    # 直接修改
my_car.odometer = 33
my_car.read_odometer()
"""
    # 通过方法修改
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
    def read_odometer(self):
        '''公里数'''
        print(f"the car has road {self.odometer_start} meters ")
            
my_car3 = Car_3("hongi","h9",2020)
print(my_car3.get_descriptive_name())
my_car3.update_odometer(41_200)
my_car3.read_odometer()
my_car3.increment_odometer(315)
my_car3.read_odometer()

### 继承  子类继承父类 且有自己特殊属性
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


# 开始继承   
class Electriccar(Car_3):  # 括号里必须写父类名称 父类必须在当前文件中且位于子类之前
    '''car 中的电动车 子类父类关系'''
    def __init__(self, make, model, year):
        "初始化父类属性"
        super().__init__(make, model, year)   ##### ！！！！！！
my_ecar = Electriccar('changan','cs75',2019)
print(my_ecar.get_descriptive_name())
# 子类定义属性和方法

class Electriccar_1(Car_3):  # 括号里必须写父类名称 父类必须在当前文件中且位于子类之前
    '''car 中的电动车 子类父类关系'''
    def __init__(self, make, model, year):
        "初始化父类属性"
        "初始化电动车具有的属性"
        super().__init__(make, model, year)   ##### ！！！！！！
        self.battery_size = 76
    def describe_battery(self):
        "描写电池信息"
        print(f"this car has a {self.battery_size}-kwh battery. ")
my_ecar_1 = Electriccar_1('changan','cs75',2019)
print(my_ecar_1.get_descriptive_name())    
my_ecar_1.describe_battery()    

# 重写父类
# 比如当前我的电动汽车并没有。汽车类中的油箱这一个属性。所以我们可以考虑重写
class Electriccar_2(Car_3):  # 括号里必须写父类名称 父类必须在当前文件中且位于子类之前
    '''car 中的电动车 子类父类关系'''
    def __init__(self, make, model, year):
        "初始化父类属性"
        "初始化电动车具有的属性"
        super().__init__(make, model, year)   ##### ！！！！！！
        # self.battery_size = 76   原方法
        self.battery = Battery()   # 实例做属性时的写法
    def describe_battery(self):
        "描写电池信息"
        print(f"this car has a {self.battery_size}-kwh battery. ")
    def fill_gas_tank(self):
        "电动车没油箱"
        print("电动车没油箱")


## 将实例做为属性 
  # 创建类过程中，随类和方法的增加，
  # 有一些描写相同的可以提出来放在另一个类中
  # 作为某实例的属性
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














    







   


