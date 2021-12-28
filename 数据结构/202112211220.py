# for x in range (1,10):
#     for y in range (10):
#         for z in range (0,10):
#             #print(x,y,z)
#             b=100*x+10*y+z
#             if b==x*x*x+y*y*y+z*z*z:
#                 print(b)



#让用户输入一个数，判断是否是水仙花数
# a=int(input('请输入您的三位数字:'))
# b=a//100
# c=(a-b*100)//10
# d=a-b*100-c*10
# #print(b,c,d)
# if a==b*b*b+c*c*c+d*d*d:
#     print('是水仙花数')
# else:
#     print('不是水仙花数')



#判断101-200之间有多少个素数（只要有一个能被其他数整除的，这个数就不是质数）
# zsNumber=0
# for a in range(101,201):
#     for y in range(2,a):
#
#         if a%y == 0:
#             break
#     else:
#         zsNumber+=1
# print(zsNumber)





#输入一行字符，分别统计出其中英文字母、空格、数字和其他字符的个数
# a=input('please enter your string:')
# engCount=0
# kgCount=0
# otherCount=0
# numberCount=0
# for x in a:
#     #print(x)
#     if x.isalpha():
#         engCount+=1
#     elif x.isdigit():
#         numberCount+=1
#     elif x==' ':
#         kgCount+=1
#     else:
#         otherCount+=1
# print('英文字符有',engCount,"个",'空格字符有:',kgCount,'个',"数字字符有：",numberCount,'个','其他字符:',otherCount,"个")

def stringCount(content):
    engCount=0
    kgCount=0
    otherCount=0
    numberCount=0
    for x in content:
        # print(x)
        if x.isalpha():
            engCount+=1
        elif x.isdigit():
            numberCount+=1
        elif x==' ':
            kgCount+=1
        else:
            otherCount+=1
    b ='英文字符有' + engCount + "个", '空格字符有:',kgCount,'个',"数字字符有：",numberCount,'个','其他字符:',otherCount,"个"
    return(b)

stringCount('y i , 7')


