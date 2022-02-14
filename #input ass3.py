#Question 1
a=str(input("Enter any string of your choice: "))
list=a.split() 
dict={} 
if list.__len__()==1:   
    for i in list[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
else:
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
print("\n")


#Question 2
def Next_Date():
    list1 = [1, 3, 5, 7, 8]

    list2 = [4, 6, 9, 11]

    list3 = [2]

    list4 = [12]

    while (True): 

        day = int(input("ENTER THE DAY: "))

        if (1 <= day <= 31):

            break

        else:

            print("Please Enter a valid day")

    while (True):  

        month = int(input("ENTER THE MONTH OF THE YEAR: "))

        if (1 <= month <= 12):

            break

        else:

            print("Please Enter a valid month")

    while (True):  

        year = int(input("ENTER THE YEAR: "))

        if (1800 <= year <= 2025):

            break

        else:

            print("Please Enter year from 1800 to 2025 only")

    if month in list1:

        if (day == 31):

            day = 1

            month = month + 1

            print(day, "/", month, "/", year)

        elif (day < 31):

            day += 1

            print(day, "/", month, "/", year)

        else:

            print("INVALID DATE TRY AGAIN")

            Next_Date()



    elif month in list2:

        if (day == 30):

            day = 1

            month = month + 1

            print(day, "/", month, "/", year)

        elif (day < 30):

            day += 1

            print(day, "/", month, "/", year)

        else:

            print("INVALID DATE TRY AGAIN")

            Next_Date()

    elif month in list3:

        if (year % 4 == 0):

            if (day == 29):

                day = 1

                month = month + 1

                print(day, "/", month, "/", year)

            elif (day < 29):

                day += 1

                print(day, "/", month, "/", year)

            else:

                print("INVALID DATE TRY AGAIN")

                Next_Date()

        else:

            if (day == 28):

                day = 1

                month += 1

                print(day, "/", month, "/", year)

            elif (day < 28):

                day += 1

                print(day, "/", month, "/", year)

            else:

                print("INVALID DATE TRY AGAIN")

                Next_Date()

    elif month in list4:

        if (day == 31):

            day = 1

            month = 1

            year += 1

            print(day, "/", month, "/", year)

        elif (day < 31):

            day += 1;

            print(day, "/", month, "/", year)

        else:

            print("INVALID DATE TRY AGAIN")

            Next_Date()



    else:

        print("INVALID DATE TRY AGAIN")

        Next_Date()


Next_Date()

print("\n")




#Question3
input_list = input('Enter elements of a list: ')
user_list = input_list.split()
print('list: ', input_list)
for i in range(len(user_list)):
    user_list[i] = int(user_list[i])
squared_list =[(user_list[i], user_list[i]**2) for i in range(len(user_list))]
print(squared_list)





#Question 4
def input_point():
    p = int(input("Enter Grade Point: "))
    if p>10 or p<4:
        print("Enter between 4-10!! Try Again")
        point = input_point()
    return p
grade=input_point()
if(grade==4):
    print("Your Grade is 'D' and poor performance")
elif(grade==5):
    print("Your Grade is 'C' and Below Average performance")
elif(grade==6):
    print("Your Grade is 'C+' and Average performance")
elif(grade==7):
    print("Your Grade is 'B' and Good performance")
elif(grade==8):
    print("Your Grade is 'B+' and Very Good performance")
elif(grade==9):
    print("Your Grade is 'A' and Excellent performance")
else:
    print("Your Grade is 'A+' and outstanding performance")
print("\n")



#Question 5
x = 6
for i in range(x):

    for j in range(i):
        print(' ', end='')
    for j in range(2*(x-i)-1):
        print(chr(65 + j), end='') 
    print()
print("\n")



#Question 6
sid = int(input("Enter SID: "))
name = input("Enter Name: ")
students = {sid:name}
while (1):
    choice = input("Do you want to enter another student entry(Y or N):").upper()
    if choice == 'Y':
        sid = int(input("Enter SID: "))
        name = input("Enter Name: ")
        students[sid] = name
    elif choice== 'N':
        break
    else:
        print('Enter valid word!!')

print("students details stored in the dictionary is:",students)

print("Sort dictionary using student names is :",{k:v for k,v in sorted(students.items(), key= lambda x:x[1])})

print("Sort dictionary using SID is :",{k:v for k,v in sorted(students.items())})

sid = int(input("Search Name with SID (Enter sid): "))
print("The name of student is :",students[sid])



#Question 7
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
no_of_terms=int(input("Enter the number of terms in series "))
if no_of_terms <= 0:     # Check if the number of terms is valid
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   sum=0
   for i in range(no_of_terms):
       print(recur_fibo(i))
       sum=sum+recur_fibo(i)
avg=float(sum/no_of_terms)
print("Avg is:",avg)



#Question 8
Set1 = {1,2,3,4,5}
Set2 = {2,4,6,8}
Set3 = {1,5,9,13,17}
# part a
Set_Union = Set1.union(Set2)
Set_Intersection = Set1.intersection(Set2)
Part_A_Set = Set_Union - Set_Intersection
print("a part :", Part_A_Set)

# part b
Part_B_Set = Set1.union(Set2.union(Set3)) - Set1.intersection(Set2) - Set2.intersection(Set3) - Set3.intersection(Set1)
print("b part :", Part_B_Set)

# part c
Part_C_Set=((Set1.intersection(Set2)).union((Set1.intersection(Set3)).union(Set2.intersection(Set3))))-(Set1.intersection(Set2.intersection(Set3)))
print("c part :",Part_C_Set)

# part d
Part_D_Set = set()
for i in range(1, 11):
    if i not in Set1:
        Part_D_Set.add(i)
print("d part :", Part_D_Set)

# part e
Part_E_Set = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        Part_E_Set.add(i)
print("e part is", Part_E_Set)


