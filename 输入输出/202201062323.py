# f=open('C:/Users/Daisy/Desktop/Pylearning/test1.txt','r')
# str=f.readline()
# print(str)
# f.close()
#
# f=open('C:/Users/Daisy/Desktop/Pylearning/test1.txt','r')
# str=f.readlines()
# print(str)
# f.close()
#
# f=open('C:/Users/Daisy/Desktop/Pylearning/test1.txt','r')
# for line in f:
#     print(line)
#
# print(123)
# print(456)
#
# print(234)
# print(456, end='2')
# print(567)

# f=open('C:/Users/Daisy/Desktop/Pylearning/test6.txt','w')
# c = f.write('hello,world \n 是的\n hi')
# print(c)
# f.close()

# import pickle
# data1={'a':[1,2.0,3,4+6j],
#        'b':('string',u'Unicode string'),
#        'c':None}
#
# selfref_list=[1,2,3]
# selfref_list.append(selfref_list)
# output=open('data1.pkl','wb')
# pickle.dump(data1,output)
# pickle.dump(selfref_list,output,-1)
# output.close()
#
#
# f=open('C:/Users/Daisy/Desktop/Pylearning/test7.txt','rb+')
# f.write(b'0123456789abcdef')

print('hello\nrunoob')
print(r'hello\nrunoob')
input("\n\n按下 enter 键后退出。")

