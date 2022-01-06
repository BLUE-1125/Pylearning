import math

print('常量 PI 的近似值为： {}。'.format(math.pi))

print('常量PI的近似值为：{!s}。'.format(math.pi))


print("123213{}".format("我"))

print('常量PI的近似值为{0:.5f}。'.format(math.pi))

table={'Google':1,'Runoob':2,"Taobao":3}
for name, number in table.items():
    print('{0:10s} ==> {1:10d}'.format(name,number))


print("number {}".format(10))

table={'Google':1,"Runoob":2,'Taobao':3}
print('Runoob:{0[Runoob:d]};Google:{0[Google:d};Taobao:{0[Taobao]:d}.format(table)')

table={'Google':1,'runoob':2,'Taobao':3}
print('runoob:{runoob:d};Google:{Google:d}；Taobao：{Taobao：d}.format(**table)')

print('常量PI的值近似为：%10.3f。'%math.pi)

str=input('请输入：')
print('你输入的内容是：',str)

f=open('test123.py','w')
f.write("a = 10\nprint(a+10)")
f.close()


