import os

os.remove("test.doc")
os.remove("testnew.txt")






ob=open("test.txt","w")
ob.write("hello")
ob.write("python")
ob.close()

'''
print(ob.closed)
print(ob.mode)
print(ob.softspace)
print(ob.name)
'''


ob=open("test.txt","r")
data=ob.read()
print data
ob.close()


ob=open("test.doc","w")
ob.write("hello")
ob.write("python")
ob.close()



os.rename("test.txt","testnew.txt")

