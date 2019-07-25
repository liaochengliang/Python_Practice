#!/usr/bin/python
# -*- coding:utf-8 -*-


# 输入两个数，一个为金额一个为红包个数，随机分配红包金额，保存在列表中；
import random
money=float(input("请输入金额："))
num=int(input("请输入红包个数："))
m=money*100
lst=[random.randint(1,m-(num-1))]
for temp in range(1,num-1):
    m=m-lst[temp-1]
    lst.append(random.randint(1,m-(num-temp-1)))
lst.append(m-lst[num-2])
for temp in range(0,num):
    lst[temp]=lst[temp]/100
print(lst)

# 方法2

import random
money=float(input("请输入金额："))
num=int(input("请输入红包个数："))
m=int(money*100)
lst=[0]
lst=lst+random.sample(range(1,m),num-1)
lst.sort()
for i in range(0,num-1):
    lst[i]=lst[i+1]-lst[i]
lst[num-1]=m-lst[num-1]
for i in range(0,num):
    lst[i]=lst[i]/100
print(lst)
input()