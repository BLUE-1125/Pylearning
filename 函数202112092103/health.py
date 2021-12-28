#定义一个函数让用户输入身高，体重，判断用户是偏胖，偏瘦还是标准

def customer(height,weight):
    rule=weight/(height*height)
    if 18.5<=rule<=23.9:
        print('标准')
    elif rule>23.9:
        print('偏重')
    else:
        print('偏瘦')

# customer(160,45)
# customer(176,63)

def heartSpeed(a):
    if 60<=a<=100:
        print('心跳正常')
    elif a>100:
        print('心动过速')
    else:
        print('心动过缓')

# heartSpeed(120)
# heartSpeed(80)


def diastolicBloodPressure(b):
    if 60<=b<=90:
        print('正常')
    elif b>90:
        print('高血压')
    else:
        print('低血压')

# diastolicBloodPressure(100)
# diastolicBloodPressure(70)
# #diastolicBloodPressure()舒张压

def systolicPressure(c):
    if 90<=c<=140:
        print('正常')
    elif c<90:
        print('低血压')
    else:
        print('高血压')
# #systolicPressure() 收缩压
# systolicPressure(150)
# systolicPressure(80)


