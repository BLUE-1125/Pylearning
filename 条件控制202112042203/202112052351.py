#题目1：
string_a = 'hello_world_2022_2023'
#简单，如何得到一个队列/列表【‘hello','world','2022'】
# c=string_a[0:5]
# d=string_a[6:11]
# e=string_a[12:17]
# print(c)
# print(d)
# print(e)
# b=[c,d,e]
# print(b)

b=[string_a[0:5],string_a[6:11],string_a[12:17]]
print(b)


#较难,如何使用split的办法得到一个队列/列表【‘hello','world',2022】
#较难,如何使用split的办法得到一个队列/列表【‘hello','world_2022'】
print(string_a.split('_',3))

#题目2：
list_a = ['hello','world','2022']
#简单，如何得到字符串'hello_world_2022'
# print(list_a[0]+'_'+list_a[1]+'_'+list_a[2])

#较难,如何使用join方法得到字符串'hello_world_2022'

print('—'.join(list_a))


#题目3：
message = 'hi how are you hellow world,hello 2022'
word = 'hello'
#简单，判断message中是否包含word,包含就返回True,否则返回False
if word in message:
    print(True)
else:
    print(False)
#较难,计算里面w出现的次数
print(message.count('w'))




#题目4：
'''
输入一个姓名，判断是否姓范
'''
name = input('please input your name:')
if name[0]=='范':
    print('True')
else:
    print('False')




######################难度增加#######################################


#题目5：
'''
给定一个数a,判断一个数字是否为基数或者偶数
'''
number=int(input('please enter your number：'))
if number % 2==0:
    print('偶数')
else:
    print('奇数')


#题目6：
'''
使用循环做一个99乘法表
'''

#题目7：
'''
自制一个python文件的游戏（即不需要封装和做成GUI的形式），游戏内容是，剪刀石头布，判断输赢,需要两个人input,判断输赢
'''






