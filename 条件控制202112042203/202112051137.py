# 输入一个整数，判断他是否可以同时被2和3整除,如果成被2和3整除，那么继续判断他能否被4整除
number=int(input('please enter your number:'))
if number % 2 == 0:
    if number % 3 == 0:
        print("both ok")
        if number % 4 == 0:
            print("can 2 3 4")
        else:
            print("can 23 not 4")
    else:
        print("can 2 not can 3")
else:
    print("not can 2 ")
    if number % 3 == 0:
        print("can 3 not can2")
    else:
        print("not can 2 not can 3")

