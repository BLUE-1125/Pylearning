
a='alex'
b=a.capitalize()
print(a)
print(b)


name = " aleX"
m=name.strip()

print(m)

print(name.startswith(" a"))
print(name.endswith('X'))

if name[1:3]=='al':
    print("true")
else:
    print("false")

if name[len(name)-1]=='X':
    print('Yes')

rrr = name.replace("X","p")
print(rrr)
# #将name变量对应的'x'替换成’p'
# name1=list(name)
# name1[4]='p'
# print(name1)
# name=''.join(name1)
# print(name)

#e 将name变量对应得值根据'l'分割
x = name.split('l')
print(x)

#f请问上一题e分割后得到的值是什么类型
#list

#g将name变量对应的值变大写
y=name.upper()
print(y)

#h将name变量对应的值变小写
u=name.lower()
print(u)

#i.请输出name变量对应的值的第二个字符
print(name[2-1])

#j.请输出name变量对应的前三个字符
print(name[0:3])

#k.请输出name变量对应的后两个字符
#print(name[3:])

#l.请输出name变量中的e所在的索引位置
#print(name.find('e'))

#m 获取子序列，仅不包含最后一个字符
# d=name[0:4]
# print(d)
# print(name[len(name)-2:len(name)])
#
# print(name[0:len(name)-1])

# li='sadqasfqwefgwg'
# x = '_'.join(li)
# print(x)
#
#
# def sumcac(a,b):
#     total=a+b
#     return total
#
#
#
#
# x = sumcac(3,6)
# print(x)
#
#
# #设计一个函数计算用户输入的内容有几个十进制数，几个大小写字母，并且返回“大小写字母有x个，数字有x个”
# # 如调用函数传入参数"hello1hl2356!你好"后，输出大写字母0个，小写字母7个，数字5个，
#
#
# def abc():
#     x=input('please enter your string:')
#     # print(x)
#     upperCount=0
#     lowerCount=0
#     numCount=0
#     for i in x:
#         # print(i)
#
#         if i.isdecimal():
#             # print('isdecimal')
#             numCount+=1
#
#         if i.isupper():
#             # print('isupper')
#             upperCount+=1
#
#         if i.islower():
#             # print('islower')
#             lowerCount+=1
#
#
#     # print(numCount)
#     # print(upperCount)
#     # print(lowerCount)
#     #print('decimal：',numCount,'upperalphabet:',upperCount,'loweralphabet:',lowerCount)
#
#     return ('decimal：',numCount,'upperalphabet:',upperCount,'loweralphabet:',lowerCount)
#
#
# yyy=abc()
# print(yyy)


a=input('please enter your name and address and hobby:',)
print(a)
b=a.split('，')
print(b)
print('姓名：',b[0],'地点：',b[1],'爱好:',b[2])
