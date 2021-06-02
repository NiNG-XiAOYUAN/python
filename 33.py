
#创建字典
d = dict([("china","beijin"),("uk","ny"),("usa","ld")])
name = str(input("输入国家名称") )      #  用户输入名称                     
if name in d:                  #判断名称是否在字典中
    y=d.get (name )
    print(y )            # 输出对应value  
else:
    print("暂时没有收录这个国家")     # 不在则提示

    
