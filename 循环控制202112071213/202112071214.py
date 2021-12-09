# 使用while来计算1到10的和
a=10
sum=0
counter=1
while counter<=a:
    sum=sum+counter
    counter+=1
    print("1到10的和为:",sum)

# 实现一个无限循环 无限输入一个数字并且打印出他
# for i in range (100):
    # print(i)

# while True:
#     sun = input("please input:")
#     print(sun)

# 使用forin循环输出list中每一个元素的长度
# ['sdf','asd2','asasd1','asdasd']

d=['sdf','asd2','asasd1','asdasd']
# for i in range(len(d)):
#     print(i)
for i in d:
    length = len(i)
    print(length)
    if length == 4:
        break;


# -如果发现长度为4直接就退出所有循环
d=['sdf','asd2','asasd1','asdasd']
for i in range(len(d)):
    if len(i)!=4:
        continue
        ptint(i)
        break

