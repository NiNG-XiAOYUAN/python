#type (3)#表示3的类型

#round(0.1+0.2,2)#内置四舍五入 2表 保留2位小数

#a=12.2e2   # 10的2次方

#math.pi              #调用math的pi属性   
3.141592653589793
#dir(math ) #查看math的函数

#math.pow(2,3)  # 指数运算2的3次方
8.0
#** 表示次方 2**3=8  * 表示乘   2*3=6
'''
nihao 1



'''
import math
f1=20
f2=10
alpha=math.pi/3
x_f=f1+f2*math.sin(alpha)
y_f=f2 * math .cos(alpha)
f=math.sqrt(x_f * x_f + y_f**2)
print('the result is ',round(f,2),'n')
# 学会 help 
'''
#a="python"
 #'what's your name'
  File "<stdin>", line 1
    'what's your name'
          ^
SyntaxError: invalid syntax
>>> "what's your name"
"what's your name"
>>> 'what\'s your name'
"what's your name"
'''