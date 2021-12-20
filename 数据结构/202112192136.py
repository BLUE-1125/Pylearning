# 题目：企业发放的奖金根据利润提成
# 。利润(I)低于或等于10万元时，奖金可提10%；
#      利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
#      20万到40万之间时，高于20万元的部分，可提成5%；
#      40万到60万之间时高于40万元的部分，可提成3%；
#      60万到100万之间时， 高于60万元的部分，可提成1.5%，
#      高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，
#      求应发放奖金总数？

#a=int(input('please input your your profit:'))

# if a in range (0,11):
#     print ('bonus是：',a * 0.1,'万')
# elif 10<a<20:
#     print('bonus是',10*0.1+(a-10)*0.075,'万')
# elif 20<a<=40:
#     print('bonus是',10*10%+10*0.075+(a-20)*0.05,'万')
# elif 40<a<=60:
#     print('bonus是',10*10%+10*0.075+20*0.05+(a-40)*0.03,'万')
# elif 60<a<=100:
#     print('bonus是',10*10%+10*0.075+20*0.05+20*0.03+(a-60)*0.015,'万')
# elif a>100:
#     print=('bonus是',10*10%+10*0.075+20*0.05+20*0.03+20*0.015+(a-100)*0.01)



#定义一个不需要返回值的函数，名为scoreCacu，参数名score,
#输入一个学生的分数，大于等于90分是a，大于等于60分是b，其他是c，并且输出制定格式，比如输入90时，打印出90分属于a
# def scoreCacu(score):
#     if score>=90:
#         print(score,'属于a')
#     elif 60<=score:
#         print(score,'属于b')
#     else:
#         print(score,'属于c')
#
# scoreCacu(56)

#输入三个乱序大小数字，装到一个list中，并且升序输出他们
# a=int(input('please enter your number:'))
# b=int(input('please enter your number:'))
# c=int(input('please enter your number:'))
# d=[a,b,c]
# d.sort()
# print(d)


a=0
b=[]
while a<3:
    number=int(input('please enter your numbers:'))
    b.append(number)
    a+=1
b.sort()
print(b)
