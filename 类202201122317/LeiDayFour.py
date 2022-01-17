# class MyClass:
#     i=12345
#     def f(self):
#         return 'hello world'
# x=MyClass()
# print(x.i)
# print(x.f())

class Myclass:
    data=3
    def __init__(self,d):
        self.data=d
    def speak(self):
        print('我今年%d岁。'%(self.data))
x=Myclass(5)
x.speak()

class Complex:
    def __init__(self,realpart,imagpart):
        self.r=realpart
        self.i=imagpart
x=Complex(3.0,-4.5)
print(x.r,x.i)

class people:
    name='SB'
    age=6
    __weight =9
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.__weight = w
    def speak(self):
        print('%s说：我%d岁'%(self.name,self.age))

class student(people):
    grade='99'
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)
        self.grade=g
    def speak(self):
        print('%s说我今年%d岁了，在读%d年纪' %(self.name,self.age,self.grade))

x=student(5,6,7,8)
print(x.grade,x.name,x.age)
    # #覆写父类的方法
    # def speak(self):
    #     print('%s说我今年%d岁了，在读%d年纪，体重%d' %(self.name,self.age,self.grade,self.__weight__))
s=student('ken',60,89,678)
s.speak()

#多继承
class people:
    name='SB'
    age=6
    __weight =9
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.__weight = w
    def speak(self):
        print('%s说：我%d岁'%(self.name,self.age))

