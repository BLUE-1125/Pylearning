install.packages("tidyverse")
install.packages("ggrepel")
install.packages("arm")
install.packages("DataCombine")
install.packages("readxl")
install.packages("sf")
install.packages("rmapshaper")
install.packages("fuzzyjoin")
install.packages("patchwork")
install.packages("data.table")
library(arm)
library(tidyverse)
install.packages('tinytex')
tinytex::install_tinytex()
1+1
5*5
18/6
cost<-2.5
cost
name <- c("Town 1"," Town 2","Town 3","Town 4"," Town 5"," Town 6"," Town 7")
vaccinations <- c(3353, 834,72,2800,1442, 34,262
                  cost <- c(2.5,1.8,1.9,1.70,1.70,2.1,2.45)
                  vaccinations <- c(3353, 834,72,2800,1442, 34,262)
                  cost <- c(2.5,1.8,1.9,1.70,1.70,2.1,2.45)
                  name
                  vaccinations
                  cost
                  vaccinations * cost
                  total.cost <- cost*vaccinations
                  cost.town <- data.frame(name,total.cost
                                          total.cost <- cost*vaccinations
                                          total.cost <- cost*vaccinations
                                          cost.town <- data.frame(name,total.cost)
                                          cost.town
                                          cost.town[1,2]
                                          need <- c(2848, 331,64,2100,113, 12,85)
                                          need
                                          cost.town$value <- cost.town$total.cost / need
                                          cost.town
                                          cost.town$name <- as.factor(cost.town$name)
                                          levels(cost.town$name) <- c("Kartik","Pahada","Likhu","Narku","Dunai","Sahartara","Mukot")
                                          cost.town$name
                                          levels(cost.town$name)[1] <- "abc"
                                          levels(cost.town$name)[3:5] <- c("b", "c", "d")
                                          cost.town$nam
                                          cost.town$namen <-
                                            relevel(cost.town$name, ref=“Mukot”)
                                          cost.town$namen <- relevel(cost.town$name, ref=“Mukot"
cost.town$name <- factor(cost.town$name,
levels=c("Mukot", "Kartik Swami", "Pahada", "Saudi",
"Chandrapuri", "Bakola", "Sahartara"))
a = TRUE
typeof(a)
b = FALSE
typeof(b)
1+1
#【1】表示向量vector
#乘除运算
5*5
18/6
#当向量/矢量中有很多组件时，用c()
c(1,2,3)
#变量名<-数字
vaccinations<-3353
vaccinations
cost<-2.5
cost
#变量之间的运算
cost*vaccinations
#变量名不能出现数字，要注意大小写，可以用单引号，双引号都行
1cost
Cost
c('aa',"bb",'cc')
#可以转化为字符
as.character(c(1,2,3))
fname='John';lname='Smith'
paste(fname,lname)
#去给一个贫困国家例如尼泊尔的人民，给他们救济疫苗，有7个村庄，计算总救济费用，以及计算哪个村庄的人均救济费用最低
name<-('Town1','Town2','Town3','Town4','Town5','Town6','Town7')
name <- c("Town 1"," Town 2","Town 3","Town 4"," Town 5"," Town 6"," Town 7")
vaccinations <- c(3353, 834,72,2800,1442, 34,262)
cost <- c(2.5,1.8,1.9,1.70,1.70,2.1,2.45)
vaccinations
cost
vaccinations*cost
#计算总共的费用total cost
total.cost<-cost*vaccinations
#每个村庄各自的总费用cost.town
cost.town<-data.frame(name,total.cost)
cost.town
#data.fram()数据框架
#可以用bracket[],表示矢量中哪行哪列的数据
cost.town[1,2]
#假设下面的need告诉了我们实际上每个村庄所需的疫苗数
need<-c((2848, 331,64,2100,113, 12,85)
need <- c(2848, 331,64,2100,113, 12,85)
need
#计算每个村庄的人均救助花销
cost.town$value <- cost.town$total.cost / need
cost.town
#This adds a few new functions we haven’t addressed yet. The first is the use of the $ symbol in between the
name of the data frame we created earlier, cost.town, and the variable names value, which this command
creates, and total.cost, which we created earlier. 这里新学习了一个用$连接变量名和数据框架
#完善数据集 improve this dataset further
cost.town$name <- as.factor(cos.town$name)
cost.town$name <- as.factor(cost.town$name)
#把村庄名字单做一个因子变量，影响变量
levels(cost.town$name) <- c("b","c",d,"e,"f","a","g")
                                          levels(cost.town$name) <- c("b","c",'d',"e,"f","a","g")
levels(cost.town$name) <- c("b","c","d","g","e","a","f")
cost.town$name
#可以改变矢量里面的内容，edit a subset
levels(cost.town$name)[1] <- "hahah"
levels(cost.town$name)[3:5] <- c("xxx", "yyy", "zzz")
cost.town$name
#改变排列顺序
cost.town$name <- factor(cost.town$name,
levels=c("hahah", "c", "f", "xxx","yyy", "zzz", "a"))
#上面那句好像有问题呀，run不出来，老师说一般默认按照字母顺序排列
#判断逻辑
a = TRUE
typeof(a)
b = FALSE
typeof(b
）
#做比较，<,>,==
cost.town$value < 3
#round大概，以及可以定义大概到几位小数digits=xx
round(cost.town$value, digits=2）
#矩阵
A = matrix( c(2, 4, 3, 1, 5, 7)
nrow=2, # number of rows
ncol=3, # number of columns
byrow = TRUE)
#嗯？我写法没对？
save.image("my_saved_workspace.RData")
load("~/.RData")
load("~/.RData")
load("~/.RData")
load("~/.RData")
load("~/.RData")
load("C:/Users/Daisy/Documents/my_saved_workspace.RData")
setwd("~")