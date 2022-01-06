s='hello, runoob'
str(s)
print(s)

'hello,runoob'
repr(s)
print(s)

a='1,2,3'
print(1,2,3)
print(str(a))

print(1/7)
print(str(1/7))

number = 1 / 7
stringNum = str(1/7)

print(number + 1)
print(stringNum + "1")

x=10 * 3.25
y=200*200
s='x的值为：'+repr(x)+', y的值为：'+ repr(y) + '...'
print(s)

hello='hello, runoob\n'
hellos=repr(hello)
print(hello)
print(hellos)


nextString = "hello"
newNextString = nextString.rjust(10,"x")
print(nextString)
print(newNextString)


# print("123123",end='*')
# print("234")
# for x in range(1,11):
#     print(repr(x).rjust(2),repr(x*x).rjust(3),repr(x*x*x).rjust((5)))

for y in range(1,11):
    first = str(y).ljust(2)
    second = str(y * y).ljust(3)
    third = str(y * y * y).ljust(4)
    print(first,end=" ")
    print(second,end = " ")
    print(third)


print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))

print('{}网址： “{}！”'.format('菜鸟教程','www.runoob.com'))
print('{0}和{1}'.format('google','runoob'))
print('{1}和{0}'.format('google','runoob'))
