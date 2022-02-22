# #求1-100所有偶数的和
# sum=0
# x=0
# while x < 101:
#     if x%2==0:
#         sum+=x
#     else:
#         pass
#     x+=1
# print(sum)


#输出100-999之间的水仙花数
#eg:153=1*1*1+5*5*5+3*3*3


# for x in range(100,1000):
#     a=x//100
#     b=(x-100*a)//10
#     c=x-100*a-10*b
#     if x==a*a*a+b*b*b+c*c*c:
#         print(x)

#要求输出1-50之间所有5的倍数
# a=1
# while a < 51:
#     if a % 5==0:
#         print(a)
#     a+=1
#
#
# for a in range(1,51):
#     if a%5==0:
#         print(a)
#     a+=1


x=[10,20,30,40,50,60,70,80]
print(x.index(10))
print(x[2])

print(x[0:4:2])
print(x[7:0:-2])
print(x[::-1])
print(x[6:0:-2])
print(x[6:0:-1])

