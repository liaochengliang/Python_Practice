#!/usr/bin/python
# -*- coding:utf-8 -*-

lst=["abc","bcd","csdf"]
with open("st.txt","w") as f:   #打开一个文件，返回一个f对象，如果文件不存在，则会自动创建
    for tmp in lst:
        f.write(tmp+"\n")
print("数据写入成功...")
