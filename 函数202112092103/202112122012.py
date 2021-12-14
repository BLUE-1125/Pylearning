# # def sum(a,b):
# #     total=a+b
# #     print(total)
# #
# # sum(2,3)
#
# #定义一个函数，求和。如果求和>5返回字符串more，反之返回less，并把返回的结果打印出来
# # def sum(a,b):
# #     total=a+b
# #     if total>5:
# #         return ('more')
# #     else:
# #         return ('less')
# #
# # c=sum(4,6)
# # print(c)
#
# # sum1=lambda a,b:a+b
# # k=sum1(2 ,3)
# # print(k)
#
# # def collatz(number):
# #     if number%2==0:
# #         print(number//2)
# #     else:
# #         print(3*number+1)
# #
# # collatz(5)
# # collatz(8)
#
#
# def calculate(a,*b):
#     print(a)
#     print(b)
#     return b
# x = calculate(1,2,3,4,5,6,7,8,)
#
# def area(a):
#     total=3.14*a*a
#     return total
#
#
# b=1
# c=[]
#
# while b<=10:
#     print(b)
#     if b%2==0:
#         print("is")
#         g=area(b)
#         c.append(g)
#
#     else:
#         print('not')
#     b += 1
# print(c)
#
#
#
#
#
#
# # def cacluate(*a):
# #     return a
# #
# # receive = cacluate(1,2,3,4)
# # print(receive)
#
# print(5%6)

b = 1
ll = []
while b <= 10:
    print(b)
    if(b % 2 == 0):
        area = 3.14 * b * b
        ll.append(area)
    b+=1

print(ll)

lll = []
for x in range(1,11):
    print(x)
    if x % 2 == 0:
        aa = 3.14 * x * x
        lll.append(aa)

print(lll)

def areaFunction(start,end):
    result = []

    # return 2233
    # return 10
    for x in range(start,end + 1):
        if x % 2 == 0:
            aaa = 3.14 * x * x
            result.append(aaa)
    return result

resutlt = areaFunction(1,10)
print(resutlt)
