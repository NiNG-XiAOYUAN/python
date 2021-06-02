'''
字符串 大小写反转
'''
word = input("please input a word :")
new_lst = []
for i in word:
    if i.islower():

        new_lst.append(i.upper())
    else:
        new_lst.append(i.lower())
new_word = " ". join(new_lst)
print(word,"==>",new_word)
    