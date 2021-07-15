from random import choice, randint
# -13
class  Die:
    def __init__(self,sides):
        self.sides = sides
    def roll_die(self):
        print(randint(1,self.sides))
number = Die(10)
number.roll_die()
number.roll_die()
number.roll_die()
number.roll_die()
number.roll_die()
number.roll_die()
number.roll_die()
number.roll_die()
number.roll_die()
number.roll_die()
#14

lottery = (2,5,7,3,8,"ssdf","rr",'sdaa','uuki','kknm')
lottery_up = choice(lottery)
print(f'Your number is {lottery_up} Congratulations on winning the prize')

#15
my_lottery = (2,5,7,3,8,"ssdf","rr",'sdaa','uuki','kknm')
x = 0
for i in my_lottery:
    lottery_up = choice(lottery)
    x += 1
    if lottery_up == "uuki":
        print(lottery_up,x)

