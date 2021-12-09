def compareNumber(nb1,nb2,nb3,nb4):
    if nb1-nb2>0:
        print('max is:',nb1)
    else:
        print('max is:', nb2)

def sayHello(words):
    print(words)

#定义函数求长方形面积
def squareArea():
    width=float(input('please enter your width:'))
    height=float(input('please enter your height:'))
    squareArea=width*height
    print(squareArea)


#squareArea()

#计算三角形面积定义
def triangleArea():
    bottom=float(input('please enter your bottom:'))
    height=float(input('please enter your height:'))
    triangleArea=(bottom*height)*0.5
    print(triangleArea)

#triangleArea()
