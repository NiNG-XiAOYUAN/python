
float(2)
2.0
id(3  )
1788231313776
>>> a=2
>>> b=5
>>> 5%2    取余数
1
>>> divmod(5,2)      #被除数，除数   /  商  余数
(2, 1)
>>> 5//2
2                    商
>>>  help(id)
 
SyntaxError: unexpected indent



>>> 0.1+0.2
0.30000000000000004
>>>  round(0.1+0.2)
 
SyntaxError: unexpected indent
>>> round(0.1+0.2)
0
>>> round(0.1+0.2,2)
0.3
>>> import math     #  调用 math
>>> dir(math)      #  查看 math的 属性和方法
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 
'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 
'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor',
 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm',
  'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians',
 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

>>> math.pi
3.141592653589793
>>> math.pow(2,3)       # 指数运算2的3次方
8.0
>>> help(math.pow)
Help on built-in function pow in module math:

pow(x, y, /)
    Return x**y (x to the power of y).
''
>>> import decimal

>>> a=decimal.Decimal('0.1')
>>> a=decimal.Decimal('0.2')
>>> a
Decimal('0.2')
>>> a=decimal.Decimal('0.1')
>>> b=decimal.Decimal('0.2')
>>> a
Decimal('0.1')
>>> b
Decimal('0.2')
>>> a+b
Decimal('0.3')

四则运算
>>> 2**10         #     '**'表示 次方    ‘*’ 表 乘1024
>>> 2**10*0.1  
102.4
>>> 2*100000*0.1
20000.0


  #   ASCII 码
SyntaxError: unexpected indent
>>> ord('a')
97
>>> bin('97')
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    bin('97')

>>> a='python'
>>> m='python'
>>> n='book'
>>> m+n
'pythonbook'
>>> m+5
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>               #  不同类型 不可
    m+5
TypeError: can only concatenate str (not "int") to str



>>> m*3
'pythonpythonpython'
>>> len(m)
6
>>> name=('你好')
>>> len(m)
6

>>> "p" in m               # p 在m de 字符串中
True
>>> r="python book"        #index 从零开始
>>> len(r)                           # r 字符长度  个数
11
>>> r[0]  r[-1]

>>> r[0]
'p'
>>> r[-1]
'k'
>>> r[1:9]                                  # qiepian
'ython bo'
>>> r[1:9:2]                                    #index     cong 0 start
'yhnb'
>>>  r[1:9:2]                          #  从1 开始到9  步长为2 

>>> r[::-1]                         # 步长为负数   从右到左 -1 开始
'koob nohtyp'
>>> r[-10:8:2]                      # 步为正 2   先遇见-10位 到8 
'yhnb'
>>> r[8:-10:-2]                     #  先遇见8 
'o ot'
>>> # dir() 查看对象的属性和方法
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


 # index  使用

 s="python lesson"
 s.index("n")                  #第一次找到 n 的index

 s.index("n")                 # 第一次找到 n 的index
5
 s.index("n",6)                 # 从第六位找
12
 s.index("n")                     #第一次找到 n 的index
SyntaxError: invalid syntax

 s.index("on")
4
a="I LOVE PYTHOB"
 a.split (" ")                   # you 空格 相当于按空格拆开
['I', 'LOVE', 'PYTHOB']
                                   # 得到上面按的叫列表
>>> lst=a.split (" ")
>>> lst
['I', 'LOVE', 'PYTHOB']
>>> "-",join(lst)                    # jiang -插入 链接各元素
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    "-",join(lst)                        # jiang -插入 链接各元素
NameError: name 'join' is not defined
>>>  "-",join(lst)  # jiang -插入 链接各元素
 


                                                     # 格式化输出
>>> # format

>>> "i like {0} and {1}" .format("php","money")
'i like php and money'
>>> "i like {0:10} and {1；>15}" .format("php","money")

>>> "i like {0:^10} and {1:>15}" .format("php","money")
'i like    php     and           money'
>>> "she is {0:4d} years old and {1:.1f}m in height".format (28,1.68)
'she is   28 years old and 1.7m in height'
>>> 
>>>                                                           #  列表
>>> lst=[]
>>> type(lst)
<class 'list'>

>>> a_lst=[2,3,4,5,'python',[]]
>>> b_lst=[3,2,4,5,'python',[]]

>>> id(a_lst)
1788236605824
>>> lst=['a','b','c','d']
>>> lst[0]
'a'
>>> lst[-1]
'd'
>>> lst[1:3]                             # 不包括 3     切片
['b', 'c']
>>> lst[:3]
['a', 'b', 'c']

>>> lst[:: -1]
['d', 'c', 'b', 'a']
>>> lst[:: 2]
['a', 'c']
>>> lst[1]=100
>>> lst
['a', 100, 'c', 'd']
>>> lst2=[1,2,3]
>>> lst+lst2
['a', 100, 'c', 'd', 1, 2, 3]
>>> lst*2
['a', 100, 'c', 'd', 'a', 100, 'c', 'd']
>>> len(lst)
4

>>> 'a' in lst
True
>>> lst=[1,2,3,4]
>>> lst[2]
3
>>> lst[2]=300               # 令index=2 的位置改为 300
>>> lst
[1, 2, 300, 4]

                                           # append 追加项目
          lst.append('php')
>>> lst
[1, 2, 300, 4, 'php']

>>>                      # insert
>>> lst.insert(0,10)
>>> lst
[10, 1, 2, 300, 4, 'php']

>>> # extend
>>> lst2=['a','b']
>>> lst.extend(lst2)
>>> lst
[10, 1, 2, 300, 4, 'php', 'a', 'b']
>>> lst.extend('book')
>>> lst
[10, 1, 2, 300, 4, 'php', 'a', 'b', 'b', 'o', 'o', 'k']


                        # 移除  pop remove
>>> lst.pop()
'k'
>>> lst
[10, 1, 2, 300, 4, 'php', 'a', 'b', 'b', 'o', 'o']
>>> lst.pop(0)
10

>>> lst.remove('b')
>>> lst
[1, 2, 300, 4, 'php', 'a', 'b', 'o', 'o']
>>> lst2
['a', 'b']
>>> lst.clear()
>>> lst
[]
>>>                             # sort 排序
>>> lst2=[2,4,6,1,9,2]
>>> lst2.sort()
>>> lst2
[1, 2, 2, 4, 6, 9]

>>>                              # fanxu
>>> lst2
[1, 2, 2, 4, 6, 9]
>>> lst2.reverse()
>>> lst2
[9, 6, 4, 2, 2, 1]
>>> lst2.append(3)
>>> lst2
[9, 6, 4, 2, 2, 1, 3]
>>> sorted(lst2)
[1, 2, 2, 3, 4, 6, 9]
>>> lst2
[9, 6, 4, 2, 2, 1, 3]
>>> lst(reverse(lst2))
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    lst(reverse(lst2))
NameError: name 'reverse' is not defined
>>> 
>>> 
>>> s="python"
>>> lst=list(s)
>>> lst
['p', 'y', 't', 'h', 'o', 'n']
>>> # 组成字符串

>>> "_".join(lst)
'p_y_t_h_o_n'
>>> str(lst)
"['p', 'y', 't', 'h', 'o', 'n']"
"[]"

massage="one og"