#Ques 1
str1="Python is a case sensitive language"

#parta
print('length of the str1:',len(str1))


#part b
line1=str1[-1::-1]
print(line1)

#part c
line2=str1[10:26]
print(line2)

#part d
line3=str1.replace("a case sensitive", "object oriented")
print(line3)

#part e
line4=str1.find("a")
print(line4)

#part f
line5=str1.replace(" ", "")
print(line5)


#Ques 2
Name='Tanish Kalra'
SID=21103112
CGPA=8.5
Dep_name='CSE'
str2='Hey, %s here!\n My sid is %d\n I am from %s department and my cgpa is %s' %(Name,SID,Dep_name,CGPA)
print(str2)


#Ques 3
a=56
b=10

#parta
q=a&b
print('a&b=',q)

#partb
w=a|b
print('a|b=',w)

#partc
e=a^b
print('a^b=',e)

#part d
r=a<<2
print("Part d, i:", r)
t=b<<2
print("Part d, ii:", t)

#part e
y=a>>2
print("Part e, i:", y)
u=b>>4
print("Part e, ii:", u)




#Ques 4
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
 
if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3
 
print("The largest number is",largest)


#Ques 5
str5=input("Enter any line or paragraph : \n")
namecount=str5.count("name")
if namecount>= 1 :
 print("Yes")
else:
 print("No")


#Ques 6
a=int(input("Enter first side:"))
b=int(input("Enter second side:"))
c=int(input("Enter third side:"))
if a>=b+c :
 print("NO")
elif b>=a+c :
 print("NO")
elif c>=a+c :
 print("NO")
else :
 print("YES")
