# def hanShu1():
#     return(10)
#
# hanShu1()
#
#
# def hanShu2(a):
#     return a
#
# hanShu2(10)
#
#
#
# def hanShu3(a,b):
#     print(a + b)
#
#
# number1 = hanShu1()
#
# userInputNumber = int(input("please input:"))
#
# hanShu3(hanShu1(),hanShu2(userInputNumber))


# x=0
# while x<=99:
#     x+=1
#     print('这是第',x,'次循环')
# else:
#     print(101)

cicleCount = 0;
for x in range(100,200):
    cicleCount += 1
    print(cicleCount)
print(101)


def people(height,weight):
    standardWeight = (height-100)*0.9
    if standardWeight-10<=weight<=standardWeight+10:
        print('标准')
    elif weight<standardWeight-10:
        print("太瘦")
    else:
        print('太重')
people(160,45)
