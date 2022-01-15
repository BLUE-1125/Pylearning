class people:
    name = 'default'

    __pName = ''
    def __init__(self,a):
        print("初始化people")
        self.name = a
        self.__pName = "asdasd"

    def eat(self):
        print('i can eat')


    def __pEat(selfsel):
        print('private eat')


a = people('daisy')

class otherPeople:
    nickName = 'defalt nickName'
    def __init__(self):
        print("初始化otherPeople")

    def playGames(self):
        print('i can play games!')
b = otherPeople()


class sonOfPeople(people):
    def __init__(self):
        people.__init__(self,'son of daisy')
        print("初始化sonOfPeople")

    def eat(self):
        # people.eat(self)
        print('son can eat also!')
c = sonOfPeople()
print(c.name)
c.eat()



class sonOfPeopleAndOtherPeople(people,otherPeople):
    def __init__(self):
        people.__init__(self,"both son of peoeple")
        otherPeople.__init__(self)
        print('初始化sonOfPeopleAndOtherPeople')

d = sonOfPeopleAndOtherPeople()

d.eat()
d.playGames()
print(d.name)
print(d.nickName)


class vector:
    def  __init__(self,a,b):
        self.at = a
        self.bt = b

    def __str__(self):
        print('hahahah')
        return 'vector (%d,%d)' % (self.at,self.bt)

    def __add__(self, other):
        print('xixixix')
        return vector (self.at + other.at, self.bt + other.bt)
    # v1=vector(2,10)
    # v2=vector(5,-2)
    # print(v1+v2)

v1 = vector(1,2)
v2 = vector(2,3)
print(v1.at)
print(v1.bt)
print(v1 + v2)


class askdhajksdb:
    def __init__(self):
        print("!@33")

    def __add__(self, other):
        print("add")

    def __truediv__(self, other):
        print("!23")
x = askdhajksdb()
y = askdhajksdb()
x + y
x / y


class AAA:
    height = 0
    def __init__(self,h):
        self.height = h

x = AAA(8)
