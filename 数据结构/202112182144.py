# knights={'gallahad':'the pure','robin':'the brave'}
# for k,v in knights.items():
#     print(k,v)
#
# for i,v in enumerate(['tic','tac','toe']):
#     print(i,v)
#
# questions=['name','quest','favprite color']
# answers=['lancelot','the holy grail','blue']
# for q,a in zip (questions,answers):
#     print('what is your {0}? It is {1}.'.format(q,a))
#
# for i in reversed (range (1,10,2)):
#     print(i)
#
# basket=['apple','orange','apple','pear','orange','banana']
# for f in sorted(set(basket)):
#     print(f)

#有四个数字1,2,3,4,能组成多少个互不相同且无重复的三位数，各是多少
for x in range(1,5):
    for y in range (1,5):
        for z in range (1,5):
            # print(x,y,z)
            if (x!=y) & (x!=z) & (y!=z):
                print(x,y,z)


#用户输入一个数字，如果大于0,小于99，输出合适，否则计算超过这个区间多少
a=int(input('please enter your number:'))
print(a)
if a in range (0,100):
    print('合适')
elif a<0:
    print('超过:',0-a)
elif a>99:
    print('超过:',a-99)
