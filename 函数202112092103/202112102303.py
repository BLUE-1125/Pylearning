# a=10
# print(id(a))
# a=20
# print(id(a))
# b=[1,2,3,'hello']
# print(id(b))
# b[0]=3
# print(id(b))

# def changeme(a):
#     a.append([1,2,3,4])
#     print("inside:",a)
#
# mylist = [10,20,30]
# changeme(mylist)
# print("outside:",mylist)

# def hehe(a,*b):
#     print(a)
#     print(b)
#
# hehe(2,5)
# hehe(2,5,6)
# hehe(2,5,6,7)

# def print1(a,b):
#     print(a,b)
#
# print1(1,2)
# print1(b=1,a=2)

# def print2 (a,b=10):
#     print(a,b)
#
# print2(1)
# print2(1,2)
# print2(b=20,a=100)

# def print3 (a,*b):
#     print(a,b)
#
# print3(1)
# print3(1,2)
# print3(1,2,5)

# def print4 (*a):
#     print(a)
#
# print4()
# print4(1)
# print4(1,3)

def print5(**a):
    print(a)

print5(a=1)
print5(a=1,b=2)
print5(a=1,b=2,c=3)

