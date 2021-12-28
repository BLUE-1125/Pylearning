#计算1-100之间的和
# sum=0
# for x in range(1,101):
#     sum += x
# print(sum)


# x = 1
# sum=0
# while x <= 100:
#     sum+=x
#     x+=1
# print(sum)



#输出偶数的99乘法表
# for a in range(1,9):
#     for b in range (2,a+1):
#         if a%2==0 and b%2==0:
#             print(a,'*',b,'=',a*b,end=' ')
#     print()
#
#

for a in range(2,9,2):
    for b in range(2,a + 1,2):
        print(a,"乘以",b,"等于",a*b,end=' ')
    print()


# a = 10
# b = 20
# print(a)
# print("a")
# print("*")
# print(a + b)
# print("a + b")
# print(a * b)
# print("a * b")
