# class LeiClassFirst:
#     i = 123456;
#     def f(self):
#         return "hello,wold"
#
#
# x = LeiClassFirst()
# print(x.i)
# print(x.f())

# def f():
#     return "hello,world"
# i= 123456


# a = 10
# b = 20
# def caclu(a,b):
#     return  a + b
#
#
# print(caclu(a,b))


class CCCCC:

    numbera = 6
    numberb = 8



    def caclu(self):
       return self.numbera + self.numberb;


    def __init__(self,a,b):
        self.numbera = a
        self.numberb = b

x = CCCCC(10,20)
print(x.caclu())
