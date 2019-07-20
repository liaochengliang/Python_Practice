# 列表：保存一组数据: [数据1，数据2，.....]
a=[1,2,3,"dewf","abcd"]
print(a[3])

# 使用random库:random.randint()产生随机数
import random
n=random.randint(1,24)
print(n)

# if语句，如：

import random
n=random.randint(1,24)
print(n)
if n>10:
    print(n+1)
elif n>5:
    print(n+2)
else:
    print(0)

# for语句  for 变量名 in 列表：
                #循环体
for tmp in a:
    print(tmp)

# input输入，如
name=input("请输入名字：")
print("你输入的名字为"+name)

# 使用int()函数将一个可以转成整数的字符串转成整数
num=int(input("请输入一个数"))
print(num*num)

#输入两个数，一个为金额一个为红包个数，随机分配红包金额，保存在列表中；
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

lst=["abc","bcd","csdf"]
with open("st.txt","w") as f:   #打开一个文件，返回一个f对象，如果文件不存在，则会自动创建
    for tmp in lst:
        f.write(tmp+"\n")
print("数据写入成功...")

1.获取网页地址
2.发送http请求，获取响应的html代码
3.分析数据（获取有用的数据），保存数据



#导入包
from urllib import request
import random
import re
#爬取的网页地址
url="https://www.qiushibaike.com/8hr/page/12/"
#了解http请求的过程，http协议（请求协议，响应协议）
#模拟http发送请求
#创建一个请求对象。使urllib包中的request包
req =request.Request(url)
#用一个列表保存几个浏览器引擎
agents =["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36","Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"]
#为了反反爬虫，随机取一个浏览器
userAgent=random.choice(agents)
#向请求对象中添加请求头：User-Agent
req.add_header("User-Agent",userAgent)
#发送请求,并将响应过来的http协议数据包，保存在res变量中
print("发送请求")
res=request.urlopen(req)
print("请求成功")
#获取响应回来的html字符串
html=res.read().decode("utf-8")
print(html)
print("数据分析中")
#数据分析，数据保存
#创建一个正则表达式对象（re.compile("",re.S)）
pattern=re.compile('<div\sclass="content">.*?</div>',re.S)
#通过正则表达式查找某个字符串中符合规则的字符串，返回一个列表
result=pattern.findall(html)
"""
with open("fxx.txt","w") as f:
    for tmp in result:
       f.write("*"*50)
       f.write("\n")
       tmp=tmp.replace('<>')
       f.write(tmp)
       f.write("\n")
       f.write("*"*100)#打印100个
       f.write("\n")
       f.write("\n")
"""  




                

