'''this is multiline comment
.we can write multiline'''
# import os
# print(os.listdir())
# print('''My name is Amar Nath prajapati,
# I am from jaunpur uttar pradesh,
# today I have to finish python course.''')

# variables and data types in python

# a='''My name is "Amar Nath" , I am from 'Jaunpur U.P.' '''
# print(a)
# d=None
# print(type(d))
# print(3>2)
# print(True and False)


# typecosting in python


# a="123"
# a=int(a)
# print(type(a))
# a=str(a)
# print(type(a))
# a=float(a)
# print(type(a))
# b="233dd53"
# b=int(b) #number can't converted in integer
# print(b+4)


# input function in python


# a=input("enter your name:")
# print(type(a))
# print(a)
# a=input("enter the number")
# a=int(a)
# print(type(a))
# print(a)
# a=34
# b=80
# print(a>b)

# a=input("enter the value of a:")
# b=input("enter the value of b:")
# a=int(a)
# b=int(b)
# avg=(a+b)/2
# print("the average is :",avg)
# a=input("enter the value of a:")
# a=int(a)
# sq=a*a
# print("the square is :",sq)
# print(name[-4:])
# print(name[-4:-2])


# name="Amar Nath"
# print(name[0:6:2])


# story="my name is \nAmar\tnath\\Chandan Prajapati"
# print(story)

# print(story.capitalize())
# print(story.replace("Amar nath","Chandan"))

# name=input("enter your name:")
# date=input("enter the date")
# # letter= ''' dear <%s>
# #             your are selected!
# #             <%s>'''%(name,date)
# letter= ''' dear <name>
#             your are selected!
#             <date>'''
# letter=letter.replace("<name>",name)
# letter=letter.replace("<date>",date)
# print(letter)

# list=[1,4,5,7,8]
# print(list)
# list[0]="Amar Nath"
# list[3]=True
# list.append(10)
# list.pop(1)
# print(list)

# f1=input("entet the number:")
# f2=input("entet the number:")
# f3=input("entet the number:")
# f4=input("entet the number:")
# f5=input("entet the number:")
# f6=input("entet the number:")
# f7=input("entet the number:")
# flist=[f1,f2,f3,f4,f5,f6,f7]
# flist.sort()
# print(flist)
# print(sum(flist))

# l=[1,23,45,3]
# print(sum(l))
# a=(7,0,8,0,0,9)
# print(a.count(0))

# d={"a":"123","b":1234,"c":"chandan"}
# print(d.items())
# updatedict={
#     "abc":"12345",
#     "a":"Amar Nath"
# }
# d.update(updatedict)
# print(d)

# s={1,23,4,53,24,6,3}
# s.add(45)
# s.add((1,2,4))
# s.pop()
# s.remove(23)
# print(s.intersection({1,4,53}))
# print(s)

# n1=input("enter the number")
# n1=int(n1)
# n2=input("enter the number")
# n2=int(n2)
# n3=input("enter the number")
# n3=int(n3)
# n4=input("enter the number")
# n4=int(n4)
# n5=input("enter the number")
# n5=int(n5)
# n6=input("enter the number")
# n6=int(n6)
# n7=input("enter the number")
# n7=int(n7)
# n8=input("enter the number")
# n8=int(n8)
# s={n1,n2,n3,n4,n5,n6,n7,n8}
# print(s)

# name1=input("enter your name")
# name2=input("enter your name")
# name3=input("enter your name")
# name4=input("enter your name")
# lang1=input("enter your lang1")
# lang2=input("enter your lang1")
# lang3=input("enter your lang1")
# lang4=input("enter your lang1")

# mydict={}
# updatemydict={
#     name1:lang1,
#     name2:lang2,
#     name3:lang3,
#     name4:lang4
# }
# mydict.update(updatemydict)
# print(mydict)

# a=[1,2,4]
# if(2 in a):
#     print("2 subset of a")
# elif(a<3):
#     print("a is less than 3")
# else:
#     print("a is a number")


# num1=int(input("enter the number:"))
# num2=int(input("enter the number:"))
# num3=int(input("enter the number:"))
# num4=int(input("enter the number:"))
# if(num1>num2):
#     f1=num1
# else:
#     f1=num2

# if(num3>num4):
#     f2=num3
# else:
#     f2=num4

# if(f1>f2):
#     print(str(f1)+"is greater")
# else:
#     print(str(f2)+"is greater")



# sub1=int(input("enter the number:"))
# sub2=int(input("enter the number:"))
# sub3=int(input("enter the number:"))
# per=(sub1 + sub2 + sub3)/3
# if(sub1>33 and sub2>33 and sub3>33 and per>40):
#     print("Pass")
# else:
#     print("fail")

# text = input("Enter the Text: ")
# if("make a lot of money " in text):
#     spam=True
# elif("buy now" in text):
#     spam=True
# elif("click this" in text):
#     spam=True
# elif("subscribe this" in text):
#     spam=True
# else:
#     spam=False
# if(spam):
#     print("This text is spam")
# else:
#     print("this text is not a spam")

# username=input("Enter the name: ")
# length= len(username)
# if(length>10):
#     print("Username contain more than 10 character")
# else:
#     print("Username contain less than 10 character")

# list=["Amar Nath","Chandan","Mithilesh","Pramod","Saurabh"]
# username=input("Enter the name: ")
# if(username in list):
#     print("Name is present in the list.")
# else:
#     print("Name is not present in the list.")

# marks=int(input("Enter the Marks:"))
# if(marks<=100 and marks>90):
#     print("Grade: Ex")
# elif(marks<=90 and marks>80):
#     print("Grade: A")
# elif(marks<=80 and marks>70):
#     print("Grade: B")
# elif(marks<=70 and marks>60):
#     print("Grade: C")
# elif(marks<=60 and marks>50):
#     print("Grade: D")
# elif(marks<50):
#     print("Grade: F")
# else:
#     print("Please enter suitble number.")

# post=input("Enter the post: ")
# text=str.upper(post)
# if("HARRY" in text):
#     print("this post is talk about Harry Sir")
# else:
#     print("This post is not contain the word 'Harry' ")


# i=1
# while(i<=50):
#     print(i)
#     i=i+1
# print("end while")

# list=["Amar Nath","Chandan","Mithilesh","Pramod","Saurabh"]
# i=0
# while (i<len(list)):
#     print(list[i])
#     i=i+1
# for i in list:
#     print(i)

# for i in range(1,100,2):
#     print(i)



# for  i in range(10):
#     if(i==5):
#        continue
#     print(i)
# else:
#     print("this is for loop with else statement")
# i=5
# if(i>10):
#     pass# is null statement in python
# print("this is pass statement ")

# i=4
# while(i>6):
#     pass
# print("we can use pass with while loop")

# num = int(input("Enter the number for table: "))
# for i in range(1,11):
#     # print(str(num)+"x"+str(i)+"="+str(num*i))
#     print(f"{num}x{i}={num*i}")

# l1=["Harry","Sohan","Sachin","Rahul"]
# for name in l1:
#     if(name.startswith("S")):
#         print("Hello "+name)

# num = int(input("Enter the number for table: "))
# i = 1
# while(i<=10):
#     print(f"{num}x{i}={num*i}")                       #05:51:38
#     i=i+1

# num=int(input("Enter the number: "))
# prime=True
# for  i in range(2,num):
#     if(num%i==0):
#         prime=False
# if prime:
#     print("This is a prime number")
# else:
#     print("This is not a prime number")

# num=int(input("Enter the number: "))
# sum=0
# i=1
# while(i<=num):
#     sum=sum+i                                           #05:56:25
#     i=i+1
# print(sum)


# num=int(input("Enter the number: "))
# fact=1
# i=1
# while(i<=num):
#     fact=fact*i                                              
#     i=i+1
# print(fact)

# for i in range(4):
#     print("*"*i)

# n=3 
# for i in range(3):
#     print(" "*(n-i-1),end="")                             #important
#     print("*"*(2*i+1),end="")
#     print(" "*(n-i-1))

# n=3
# for i in range(n):
#     for j in range(n):
#         if(i==0 or i==n-1 or j==0 or j==n-1):
#             print("*",end="  ")                            #06:06:36
#         else:
#             print(" ",end="  ")
#     print()


# num = int(input("Enter the number for table: "))
# i = 10
# while(i>=1):
#     print(f"{num}x{i}={num*i}")                             #06:07:14      
#     i=i-1


# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# factorial = fact(5)
# print(factorial)


# def maximun(n1,n2,n3):
#     m=-1
#     if(n1>n2):
#         m=n1
#     else:
#         m=n2
#     if(m>n3):
#         return m
#     else:
#         return n3
# max=maximun(23000,323,2341)
# print("The maximun number is:"+str(max))


# def CTF(num):
#     f=(num*9)/5 + 32
#     return f
# fh=CTF(40)
# print("The answer is :" + str(fh))

# print("Hello!" ,end=" ")
# print("Hello!" ,end=" ")
# print("Hello!" ,end=" ")
# print("Hello!" ,end=" ")
# print("Hello!" ,end=" ")

# def sum(n):
#     if(n==0):
#          return 0                                      #06:45:15
#     else:
#          return n+sum(n-1)
# summ=sum(5)
# print("The sum of natural number is :" +str(summ))


# def pattern(n):
#     if(n==-1):
#         return 
#     else:
#         print("*",end=" ")
#         pattern(n-1)
#         print("*")
# pattern(3)

# n=6
# for i in range(n):
#     print("*"*(n-i))

# def inchtocm(n):
#      return n*2.54
# centimeter=inchtocm(66)                                  #06:48:00
# print(f"The answer is : {centimeter} centimeter")


# def replaceword(string,word):
#     new=string.replace(word, "")
#     return new.strip()
# this = "                     This is comment                "
# new1=replaceword(this,"This")
# print(new1)
# print(this)
# print(this.strip())


# def table(n):
#     for i in range(1,11):
#         print(f"{n}x{i}={n*i}")                    #06:52:10
# table(19)


# import random
# print(random.randint(1,5))


# f=open('sample.txt')
# data=f.readline()
# print(data,end="")
# data=f.readline()
# print(data)
# f.close()

# f=open("another.txt","w")
# f.write("I am from Jaunput U.P.")
# f.write("this is nice.")
# f.close()
# f.write("Harry sir is good teacher.")

# with open ("another.txt","r") as f:
#     print(f.read())
# with open ("another.txt","w") as f:
#     f.write("this is code with 'with' statement ")

# with open("poem.txt","r") as f:
#     a = f.read()
#     if("twinkle" in a):
#         print("word 'twinkle'is in the poem")
#     else:
#         print("word 'twinkle' is not in poem")



# scr=int(input("Enter the score: "))
# def game():
#     with open ("highscore.txt","r") as f:
#         a = f.read()
#         b=int(a)
#         if(b>scr):
#             return a
#         else:
#             return scr
# score= game()
# highscore=str(score)
# with open ("highscore.txt","w") as g:
#     g.write(highscore)


# for i in range(2,21):
#     with open (f"tables/Multiplication_Table_of_{i}.txt","w") as f:
#         for j in range(1,11):
#             f.write(f"{i}x{j}={i*j}\n")
#         if(j!=10):
#             f.write("\n")


# with open("replace_word.txt","r") as f:
#     a = f.read()
#     b= a.replace("donkey","######")
# with open("replace_word.txt","w") as g:
#     g.write(b)


# list = ["donkey","mote","kaddu"]

# with open("replace_word.txt","r") as f:
#     a = f.read()

# for word in list:                                        #important
#     b= a.replace(word,"######")

#     with open("replace_word.txt","w") as g:
#         g.write(b)


# with open ("log.txt","r") as f:
#     a= f.read().lower()
#     if "python" in a:
#         print("python is present in log file")
#     else:
#         print("python is not present in log file")


# content = True
# i=1
# with open("log.txt","r") as f:
#     while(content):
#         content=f.readline()
#         if"python" in content:
#             print(f"python is present in line number {i}")         #important
#             print (content)
#         i=i+1



# with open("this.txt","r") as f:
#     f1= f.read()

# with open ("log.txt","r") as g:
#     g1=g.read()

# if f1==g1:
#     print("files are indentical")
# else:
#     print("files are not indentical")




# with open("this.txt","w") as g:
#     g.write("")



# import os
# with open ("sam.txt","r") as f:
#     content = f.read()
# with open("rename_by_python.txt","w") as f:
#     f.write(content)
# os.remove("sam.txt")


# class RailwaysForm: #declaration of class
#     def printdata(self):
#         print(f"Name is {self.name}")          #incapsulation
#         print(f"Train is {self.train}")

# Amarsapplication=RailwaysForm() #declaration of object
# Amarsapplication.name="Amar Nath"
# Amarsapplication.train="Godan"
# Amarsapplication.printdata()

# if(remote.isLeftPressed()):                   #abstraction
#     player.moverleft()



# class Employee():
#     company="Google"
#     salary=100
#     def __init__(self,name,salary,subunit):
#         print("Employee is Created")     #constructor
#         self.name=name
#         self.salary=salary
#         self.subunit=subunit
#     def getDetails(self):
#         print(f"The name of employee is {self.name}")
#         print(f"The salary of employee is {self.salary}")
#         print(f"The subunit of employee is {self.subunit}")

#     def getsalary(self,signature):
#         print(f"salary is {self.salary}\n{signature}")
    
#     @staticmethod               #decorator
#     def greet():
#         print("Good Morning,Sir")


# Amarnath=Employee()
# Chandan=Employee()           #Here Chandan is Instance
# print(Amarnath.company)
# print(Chandan.company)
# Employee.company="YouTube"       #Change through class attributes
# print(Amarnath.company)
# print(Chandan.company)
# Amarnath.salary=200
# print(Amarnath.salary)
# print(Chandan.salary)
# print(Chandan.Address)              #Throw Error

# Chandan.getsalary()                #   Employee.getsalary(Chandan)
# Chandan.salary=1000000
# Chandan.getsalary("Thanks!")

# Chandan.greet()



# Chandan=Employee("Amar Nath",100,"YouTube")                 
# Chandan.getDetails()


                                                #09:14:50
                            #     first line is printed by Constructor(__init__)
                            # Other three next line is printed by function  getDetails



# class Programmer:
#     company="Microsoft"   
#     def __init__(self,name,product):
#         self.name=name
#         self.product=product
#     def selfInfo(self):
#         print(f"The Name of Programmer is {self.name}")
#         print(f"The product of Progammer is {self.product}")
# Amar_Nath=Programmer("Amar Nath","Python")
# Chandan=Programmer("Chandan","Java Script")
# Amar_Nath.selfInfo()
# Chandan.selfInfo()


# import math
# class Calculator:
#     def __init__(self,num):
#         self.number=num
#     @staticmethod
#     def greet():
#         print("Hello")
#     def square(self):
#         print(f"The square of {self.number} is {self.number**2}")
#     def squareRoot(self):
#         print(f"The squareroot of {self.number} is {math.sqrt(self.number)}")
#     def cube(self):
#         print(f"The cube of {self.number} is {self.number**3}")

# a=Calculator(5)
# a.square()
# a.squareRoot()
# a.cube()
# a.greet()


# class Sample:
#     a="Amar"

# obj=Sample()
# obj.a="Chandan"
# Sample.a="Chandan"
# print(Sample.a)
# print(obj.a)



# class Train:
#     def __init__(self,name,fare,seats):
#         self.name=name
#         self.fare=fare
#         self.seats=seats
#     def getstatus(self):
#         print(f"The name of the train is {self.name}")
#         print(f"The number of seats available in the Train are:{self.seats}")
#     def fareInfo(self):
#         print(f"The fare of the Train is {self.fare}Rs")
#     def bookTicket(self):
#         if(self.seats>0):
#             print(f"your ticket has been booked! your seat number is {self.seats}")
#             self.seats=self.seats-1
#         else:
#             print("Train is Full!")
#     def cancelTicket(self,number):
#         self.seats=self.seats+1
#         self.number=number                               #09:43:40
#         print("your ticket is cancled !")
#         print(f"Now Seat No. {self.number} is also available")
#         print(f"The number of seats available in the Train are:{self.seats}")

# intercity=Train("InterCity",100,100)
# intercity.getstatus()
# intercity.fareInfo()
# intercity.bookTicket()
# intercity.bookTicket()
# print("******************")
# intercity.cancelTicket(10)
# intercity.getstatus()





# class Employee:
#     company="Google"

#     def getDetails(self):
#         print("This is an employee")

# class Programmer(Employee):
#     language="Python"
#     company="YouTube"


#     def getLan(self):
#         print(f"The language is {self.language}")   #single Inheritance     
    
#     def getDetails(self):
#         print("This is a Programmer")

# Chandan=Employee()
# Amar=Programmer()
# Amar.getDetails()
# print(Amar.company)
# Chandan.getDetails()
# print(Chandan.company)
# # Amar.getLan()



# class Employee:
#     company="Visa"
#     eCode=120

# class Freelancer:
#     company="ABC"
#     level=0

#     def upradeLevel(self):
#         self.level=self.level+1       #multiple Inheritance


# class Programmer(Employee,Freelancer):
#     name="Amar Nath"

# Chandan=Programmer()
# #Employee has higher priority
# print(Chandan.company)   
# print(Chandan.eCode)
# print(Chandan.name)
# print(Chandan.level)
# Chandan.upradeLevel()
# print(Chandan.level)




# class Person:
#     country="India"

#     def __init__(self):
#         print("Initializing Person.....")
#     def takeBreath(self):
#         print("I am breathing.....")

# class Employee(Person):
#     company="Honda"
#     def __init__(self):
#         super().__init__()
#         print("Initializing Employee.....")

#     def takeBreath(self):
#         super().takeBreath()
#         print("I am Employee so I am breathing.....")

# class Programmer(Employee):
#     company="YouTube"
#     def __init__(self):
#         super().__init__()
#         print("Initializing Programmer.....")

#     def takeBreath(self):
#         super().takeBreath()
#         print("I am Programmer so I am breathing++.....")

# p=Person()
# e=Employee()
# pr=Programmer()
# print(p.country)
# print(e.country)
# print(pr.country)
# print(p.company)  #throw Error
# print(e.company)
# print(pr.company)    
# p.takeBreath()
# e.takeBreath()
# pr.takeBreath()




# class Employee:
#     company="Honda"
#     salary=100

#     def changeSalary(self,sal):
#         self.__class__.salary=sal
#     @classmethod
#     def changeSalary(cls,sal):
#         cls.salary=sal


# e=Employee()
# print(e.salary)
# e.changeSalary(455)
# print(e.salary)
# print(Employee.salary)



# class Employee:
#     company="Bharat Gas"
#     salary=5600
#     bonous=500

#     @property
#     def totalSalary(self):
#         return self.salary+self.bonous
#     @totalSalary.setter
#     def totalSalary(self,val):
#         self.bonous=val-self.salary

# e=Employee()
# print(e.totalSalary)
# e.totalSalary=5800
# print(e.salary)
# print(e.bonous)



# class Number:
    # def __init__(self,num):
    #     self.num=num
    
    # def __add__(self,num2):
    #     print("Lets add")
    #     return self.num+num2.num

    # def __mul__(self,num2):
    #     print("Lets Multiply")
    #     return self.num*num2.num
        
#     def __str__(self):
#         return(f"Decimal Number:{self.num}")

#     def __len__(self):
#         return 1

# n1=Number(4)
# n2=Number(6)
# sum=n1+n2
# print(sum)
# mul=n1*n2
# print(mul)
# print(n1)
# print(len(n1))



# class C2dvector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
#     def __str__(self):
#         return f"{self.i}i+{self.j}j"

# class C3dvector(C2dvector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k
#     def __str__(self):
#         return f"{self.i}i+{self.j}j+{self.k}k"


# v1=C2dvector(1,2)
# print(v1)
# v2=C3dvector(3,4,5)
# print(v2)



# class Animals:
#     pass 
# class Pets(Animals):
#     pass
# class Dog(Pets):                                 #11:04:15
#     @staticmethod                                #multilevel Inheritance
#     def bark():
#         print("Bow Bow!")

# d1=Dog()
# d1.bark()



# class Employee:
#     salary=1000
#     increment=1.5

#     @property
#     def salaryAfterIncremnt(self):
#         return self.salary*self.increment
    
#     @salaryAfterIncremnt.setter
#     def salaryAfterIncremnt(self,valsal):
#         self.increment=valsal/self.salary

        
# e=Employee()
# print(e.salary)
# print(e.increment)
# print(e.salaryAfterIncremnt)
# e.salaryAfterIncremnt=3000
# print(e.salary)
# print(e.increment)
# print(e.salaryAfterIncremnt)



# class Complex:
#     def __init__(self,r,i):
#         self.real=r
#         self.img=i

#     def __add__(self,c):
#         return Complex(self.real+c.real,self.img+c.img)
    
#     def __str__(self):
#         return f"{self.real}+{self.img}i"

    # def __mul__(self,num2):
    #     print("Lets Multiply")
    #     return self.num*num2.num

# c1=Complex(1,2)
# c2=Complex(3,4)

# print(c1+c2)
# mul=c1*c2
# print(mul)
        

# class Vector:
#     def __init__(self,vec):
#         self.vec=vec
#     def __str__(self):
#         index = 0
#         str1=""
#         for i in self.vec:
#             str1 += f"{i}a{index} +"
#             index=index+1
#         return str1[:-1]
                                                    
    # def __add__(self,vec2):
    #     newlist=[]
    #     if(len(self.vec)==len(vec2.vec)):
    #         for i in range(len(self.vec)):
    #             newlist.append(self.vec[i]+vec2.vec[i])
    #         return Vector( newlist)
    #     else:
    #         return("Addition Failed! The lenght of given two vector is not same.")
        
    # def __mul__(self,vec2):                                  
    #     sum=0                                                #     11:36:35
    #     if(len(self.vec)==len(vec2.vec)):
    #         for i in range(len(self.vec)):
    #             sum+= self.vec[i]*vec2.vec[i]
    #         return sum
    #     else:
    #         return("Multiplication Failed! The lenght of given two vector is not same.")

#     def __len__(self):
#         return len(self.vec)

# v1=Vector([1,2,3,7])
# v2=Vector([4,5,6])
# print(v1+v2)
# print(v1*v2)
# print(len(v1))
# print(len(v2))

# class Vector:
#     def __init__(self,i,j,k):
#         self.i=i
#         self.j=j
#         self.k=k
#     def __str__(self):
#         return f"{self.i}i+{self.j}j+{self.k}k"

# v=Vector(7,8,10)
# print(v)

# 1:37:37
# a = input("Enter the Number: ") 
# a=int(a)
# sqr=a*a                                                
# print("The square of given number is",sqr )

# 3:19:30
# tup=(7,0,8,0,0,9)                                     
# print(tup.count(0))