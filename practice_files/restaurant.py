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

        ... 