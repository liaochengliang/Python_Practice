#!/usr/bin/python
# -*- coding: UTF-8 -*-


'''
#!/usr/bin/python
class stu:
	id=0
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def fun(self):
		print(self.a)
		print(self.b)
		print(self.id)
stu1=stu(1,2)
stu1.fun()
''' 
class Employee:
   '所有员工的基类'
   empCount = 0
 
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount
 
   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
 

