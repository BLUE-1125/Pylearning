# a=10
# b=10.0
c="hello,world"+"hello,world"
print(len(c))
# d=int("10")
# e=f=g=10
# print(e)
# print(f)
# print(g)
# print(c[0])
# print(c[0:5])
# print(c[1:])


#list []
# a=[0,1,2,3,4,5,6,7,8,9]
# c=10
# d=20
# # b=[c,d] #此处的c和d没有引号，是变量
# b=["c",'d','e','f']
# print(b)
# f=[1.0,2.0]
# print(f)
# print(b[0])
# print(b[1:3])
# print(len(b))
#
# h=[10,3.14,'hello']
# h[0]=20
# print(h)


#tuple() only read
# a=(0,1,2,3,4,5)
# print(a)
# b=(1,2.0,'hello')
# b[0]=10
# print(b[0])

#dic {}
a={
    'hello':"你好",
    "world":"世界",
    "color":["b",'p','y'],
    "color2":('b,''w','y'),
    "dic":{
        "pi":3.14,
        "more":{
            "a":10,
            "b":"hello",
        },
    },
    "tuple":(1,2,3)

}
print(a["dic"]["more"]["b"])
a["color"][1]="pw"
print(a)
print(a.keys())
print(a.values())


