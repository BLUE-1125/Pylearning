# 20211205
 print混合输出
 input输入指定输入的格式
 条件控制语句if和elseif和else

# 202112051205
if语句的嵌套

#202112052352
字符串的操作
split:按照规则对字符串拆分
split（规则，拆分成几段）
拆分成几段写-1=全部拆分=不写
拆分成几段写0=不拆分

join：按照规则拼接成字符串
规则字符串.join(操作对象（list，tuple等（今天只是学了list））

input函数的使用
定义接收对象：比如a=input（），那么input输入的数据就由a来接收
input如果不指定类型，那么会默认为string
还有就是条件判断语句if else

#202112092339
1.定义函数（无参函数/有参函数）
2.在其他文件中引用def的方式：import py文件名（文件名不能全部数字）——文件名.(要引用出来的东西)
3.循环语句 for...in: , while... :
4.可变/不可变的数据类型 
可变：list，dic
不可变：tuple，string，number
可变的是在原地址修改    eg：b=[1,2,3], 改为 b[4,2,3]两次是在同一地址
不可变的是新建一个地址，eg：a=10，a=20,两次的a并不是同一个地址

#2021112102322
学习了必须参数，关键字参数，默认参数，不定长参数（即加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。加了两个星号 ** 的参数会以字典的形式导入。）