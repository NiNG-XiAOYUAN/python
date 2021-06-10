# 类    定义一大类对象都有通用行为
# 基于类创建对象时（‘’‘’实例化‘’‘’），每个对象都有通用行为

# 创建类 适用类
from typing import AsyncGenerator


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

class teacher:
    '''sd'''
    def __init__(self,name,job):
        '''df'''
        self.name = name
        self.job = job

    def zuoye(self):
        


