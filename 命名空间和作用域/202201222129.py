#全局变量和局部变量
total=0
def sum(arg1,arg2):
    total=arg1+arg2
    print('函数内是局部变量：',total)
    return total
sum(10,20)
print('函数外是全局变量：',total)


#global和nonlocal关键字
num=1
def fun1():
    global num
    print(num)
    num=123
    print(num)
fun1()
print(num)

def outer():
    num=10
    def inner():
        nonlocal num
        num=100
        print(num)
    inner()
    print(num)
outer()



a=10
def test():
    global a
    a=a+1
    print(a)
test()

a=10
def test(a):
    a=a+1
    print(a)
test(a)

