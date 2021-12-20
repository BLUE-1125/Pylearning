# #输入9X9乘法表
#
# for x in range (1,10):
#     for y in range (1,x+1):
#         print(x,'*',y,'=',x*y,end='   ')
#     print()
#
#
# for x in range (1,5):
#     m=''
#     for y in range (1,x+1):
#         print(m+"*",end='')
#     print()
#
#
# for x in range (1,4):
#     z=''
#     for y in range (1,x+1):
#         print(z+"&",end='')
#     print()

for x in range (3,0,-1):
    z=''
    for y in range (1,x+1):
        print(z+"&",end='')
    print()

for x in range (9,0,-1):
    for y in range (x,0,-1):
        print(x,"*",y,"=",x*y,end='     ')
    print()
