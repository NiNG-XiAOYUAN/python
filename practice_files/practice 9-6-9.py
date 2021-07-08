
# 9-6
class Restaurant:
    '''餐厅'''
    def __init__(self,restaurant_name,restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.number_served = 0
        self.flavors = ["niunai","xiangjiao","pinguo","shuimitao"]

       # self.type = restaurant_type
    
    def describe_restaurant(self):
        '''描述餐厅'''
        print(f'''the restaurant name is {self.restaurant_name} \tthe type is {self.restaurant_type}
                  there are {self.number_served} people visited here''')
    
    def set_number_served(self):
        '''就餐人数'''
        set_numbers = int(input("input a set number "))
        self.number_served = set_numbers
    def open_restaurant(self):
        '''状态'''
        print(f"the restaurant {self.restaurant_name} is openning ")

    def increment_number_served(self,increment_number):
        '''人数积累'''
        if increment_number >= 0:
            self.number_served += increment_number
            print(f"you can totally invate {self.number_served} people ")
        else:
            print("you cant't input this number! ")

    def get_icecream(self):
        "显示冰淇凌口味列表"
        ice_list = []
        for icecream in self.flavors:   
            ice_list.append(icecream)
        print (ice_list)
IceCreamStand = Restaurant("wanglong","cream")
IceCreamStand.get_icecream()
# 9-7
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
        self.privileges = ["can add post","can delete post","can ban user"]
        self.privileges = Privileges()
    def show_privileges(self):
        "管理权限"
        alladmin = self.first_name + self.last_name
        adprivileges = []
        if alladmin == "wanglong":
            for ad in self.privileges:
                adprivileges.append(ad)
            print(f"""the admin {alladmin.title()} have following adprivileges:
                    \n{adprivileges }""")

admin = Admin("wang","long",22)
admin.show_privileges()




