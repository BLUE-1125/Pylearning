# 新建四个类
# 第一个类的名字叫人类，有眼镜，鼻子，耳朵三个变量，还有睡觉这个函数
# 第二个类是自己的父亲的名字继承人类 但是父亲有一个新的函数叫抽烟，第二个类是母亲的名字继承人类，有一个新的函数叫赚钱 第三个类是自己的名字继承自自己的父亲和母亲
# 有一个新函数功能叫唱歌和一个函数功能叫弹钢琴

class Human:
    eye=0
    nose=0
    ear=0
    def __init__(self):
        print('init')
    def sleep(self):
        return '0'
X=Human()
print(X.eye)


class Father(Human):

    def __init__(self):
        Human.__init__(self)
    def sigreate(self):
        print('i can smoke')
F=Father()
print(F.eye)


class Mother(Human):
    def __init__(self):
        Human.__init__(self)
    def earnMoney(self):
        return '0'
M=Mother()
# sss = M.earnMoney()
# print(sss)
print(M.earnMoney())

class Daisy(Father,Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
    def singing(self):
        print('i can sing')
    def piano(self):
        print('i can play the piano')
D=Daisy()
D.piano()




