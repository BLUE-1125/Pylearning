class Person:
    height = 0
    weight = 0
    __gender = "unKnown"
    age = 0
    hobby = []

    def __init__(self,a,b,c,d,e):
        self.height = a
        self.weight = b
        self.__gender = c
        self.age = d
        self.hobby = e

    def isFitHealth(self):
        print("ok")



# daisy = Person()
# print(daisy.weight)

# 方式一
# daisy.age = 24
# daisy.height = 180
# daisy.weight = 100
# daisy.gender = "female"
# daisy.hobby = [
#     "eat",
#     "sleep",
#     "always delay"
# ]
# 方式二
daisy = Person(180,120,"famale",24,[])
daisy.isFitHealth()


class SonOfDaisy(Person):
    isLongHair = False
    def __init__(self,a,b,c,d,e,f):
        Person.__init__(self,a,b,c,d,e)
        self.isLongHair = f


son = SonOfDaisy(180,120,"famale",24,[],True)
  
print(son.isLongHair)
print(son.height)
