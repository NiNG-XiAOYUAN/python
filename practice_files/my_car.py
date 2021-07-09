from car import Car,Electriccar_3

my_newcar = Car("sss","ddd",2014)
print(my_newcar.get_descriptive_name())
my_newcar.increment_odometer = 45
my_newcar.read_odometer()

my_newcar_e = Electriccar_3("ssers","dfddd",44014)
print(my_newcar_e.battery.get_range())
my_newcar_e.fill_gas_tank()

# 导入整个模块 import car
# 所有类 用语法 module_name.classname  仔细比较与上面的区别
# 如 my_newcar_e = car.Electriccar_3("ssers","dfddd",44014)

# 导入模块中所有类
'''不推荐'''