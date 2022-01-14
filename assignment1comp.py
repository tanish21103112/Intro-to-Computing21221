#Question 1
number1=int(input('Enter First number:'))
number2=int(input('Enter Second number:'))
number3=int(input('Enter Third number:'))
average=(number1+number2+number3)/3
print('average of three numbers:',average)

#Question 2
standard_deduction = 10000
depend_deduction = 3000
gross=int(input("Enter your gross income ="))
no_of_dependents=int(input("Enter your no of dependents ="))
taxable_income= float(gross-standard_deduction-(depend_deduction*no_of_dependents))
tax = float(taxable_income*0.2)
print("Your income tax is =" , tax)


#Question 3
SID=int(input('Enter your SID:'))
Name=input('Enter your name:')
Gender=input('Enter your Gender:')
Course_name=input('Enter Course name:')
CGPA=float(input('Enter your CGPA:'))
Student=[SID,Name,Gender,Course_name,CGPA]
print(Student)


#Question 4
#S refers to student
S1=int(input('Marks of student 1='))
S2=int(input('Marks of student 2='))
S3=int(input('Marks of student 3='))
S4=int(input('Marks of student 4='))
S5=int(input('Marks of student 5='))
Marks=[S1,S2,S3,S4,S5]
print('Marks before sorting:',Marks)
Marks.sort()
print('Marks after sorting;',Marks)

#Question 5(a)
color=['Red','Green','White','Black','Pink','Yellow']
print(color)
color.pop(3)
print('list after removing 4th element:',color)

#Question 5(b)
color=['Red','Green','White','Black','Pink','Yellow']
print(color)
color[3:5]=['Purple']
print('list after replacing 4th and 5th element with Purple;',color)



