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





