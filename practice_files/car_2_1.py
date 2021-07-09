
'''car 的一些其他相似类'''
'''下面的两个类与 car 类有依赖关系 但他们不可以在同一模块内 所以：'''
from car_2 import Car 

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

class Electriccar_3(Car):  # 括号里必须写父类名称 父类必须在当前文件中且位于子类之前
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
