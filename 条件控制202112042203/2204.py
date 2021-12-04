# a=10
# print(a)
# b=20
# print(b)
# c=30
# print(a,"+",b,"=",c)
# hour=10
# min=20
# second=30
# print('now time is',hour,':',min,':',second)

# day=100
# d1=3
# print(day,'天后将会下雨',d1,'天')


#键盘输入年龄，并且输出指定格式
# please input your age：25
# your age is 25

# a = input("please input your age:")
# print("your age is " + a)

# b=input('please enter your phone number:')
# print('your phone number is:' + b)

# 输入一条狗的年龄，输出他相当于人的多少岁
# 1 = 14
# 2 = 22
# >2 老狗
dogage=int(input('please enter your dog age:'))
print(dogage)
if dogage == 1:
    print('dogage',dogage,'like human 14')
elif dogage==2:
    print('dogage',dogage,'like human 22')
elif dogage > 2:
    print('olddog')
else:
    print('not support')
