#9-10
from restaurant import Restaurant
#9-11
from admin import User,Admin
 #from moudle_name import * 导入所有（数量一共就两个）
#9-12
from car_2 import Car
import car_2_1
'''
Restaurant_1 = Restaurant("china","www")
Restaurant_1.get_icecream()

admin_1 = Admin("arwges","werhghw",23)
admin_1.privileges.show_privileges()
'''
my_ecar_2 = car_2_1.Electriccar_3('changan','cs75',2019)
print(my_ecar_2.battery.get_range())
print(my_ecar_2.get_descriptive_name())
print(my_ecar_2.fill_gas_tank())

my_ecar_3 = Car('changan','cs85',2020)
print(my_ecar_3.get_descriptive_name())
print(my_ecar_3.fill_gas_tank())



