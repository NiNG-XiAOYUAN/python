"""一个用于表示汽车的类"""
class Car:
    '''模拟汽车的一个实例'''
    def __init__(self,make,model,year):   
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




