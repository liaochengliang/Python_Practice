#!/usr/bin/python
# -*- coding:utf-8 -*-


# 导入包

from urllib import request
import random
import re
# 爬取的网页地址
url = "https://www.qiushibaike.com/8hr/page/15/"
# 了解http请求的过程，http协议（请求协议，响应协议）
# 模拟http发送请求
# 创建一个请求对象。使urllib包中的request包
req = request.Request(url)
# 用一个列表保存几个浏览器引擎
agents = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36","Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"]
# 为了反反爬虫，随机取一个浏览器
userAgent=random.choice(agents)
# 向请求对象中添加请求头：User-Agent
req.add_header("User-Agent",userAgent)
# 发送请求,并将响应过来的http协议数据包，保存在res变量中
print("发送请求")
res=request.urlopen(req)
print("请求成功")
# 获取响应回来的html字符串
html= res.read().decode("utf-8")

print("数据分析中")

# 数据分析，数据保存
# 创建一个正则表达式对象（re.compile("",re.S)）
pattern=re.compile('<div\sclass="content">.*?</div>',re.S)
# 通过正则表达式查找某个字符串中符合规则的字符串，返回一个列表
result=pattern.findall(html)
with open("c.txt","w",encoding="utf-8") as f:
    for tmp in result:
      f.write("*"*50)
      f.write("\n")
      tmp = tmp.replace('<div class="content">',"").replace("<span>","").replace("<\span>","")
      tmp = tmp.replace('</div',"").replace("\n","").replace("<br/>","").replace("</span>>","").replace('</span><span class="contentForAll">',"")
      f.write(tmp)
      f.write("\n")
      f.write("*"*100)#打印100个
      f.write("\n")
      f.write("\n")
print("保存成功！")


