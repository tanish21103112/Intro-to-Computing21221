#ASSIGNMENT_4
                 #Question_1
print("\n         #Question_1")
def hanoi(n, fro, to, aux):
    if n == 0:
        return
    
    hanoi(n-1, fro, aux, to)
    print(f"Move Disk {n} from {fro} to {to}")
    hanoi(n-1, aux, to, fro)

#calling funtion for 3 disks
hanoi(3, 'A', 'C', 'B')
print("")


                  #Question_2
print("\n          #Question_2")
n = int(input("Enter number of rows in Pascal's Triangle: "))
#using_recursion_method
print("\n#using_recursion_method")
def pascal(n, originaln=n):
    if n == 0:
        return
    
    pascal(n-1,originaln)

    print('  '*(originaln-n), end='')

    #first number always 1
    entry = 1
    for i in range(1, n+1):

        print(entry, end ='   ')

        #Binomial Coefficient
        entry = entry * (n - i) // i
    print()
pascal(n)

#iterative_method
print("\n#iterative_method")
for line in range(1, n+1):

    print('  '*(n - line), end='')

    x = 1
    for i in range(1, line+1):

        print(x, end='   ')

        x = x * (line - i) // i
    print()
print("")

                   #Question_3
print("\n           Question_3")
n1=int(input("\nEnter Integer:"))
n2=int(input("Enter other Integer:"))
list1=list(divmod(n1,n2))
#a1=Quotient
q=list1[0]
#a2=Remainder
r=list1[1]
#printing the quotient and remainder
print(f"\nThe quotient when {n1} is divided by {n2} is {q}.")
print(f"The remainder when {n1} is divided by {n2} is {r}.")

print("\n(a)\n")
c1=callable(divmod(n1,n2))
if c1==True:
    print(f"Function is callable")
if c1==False:
    print(f"Function is Not-callable")

print("\n(b)\n")
#list of values
list_values=[q,r]
zero=False
if zero in list_values:
    zero=True
else:
    zero=False
if zero==True:
    print("All result values are NOT 'non-zero'")
elif zero==False:
    print("All result values are 'non-zero'")

print("\n(c)\n")
#new values of list
list_new=[q,r]
for i in range (4,7):
    list_new.append(i)
print(f"Append (4,5,6) in the values ({q},{r})")
list_values2=[]
#adding number > 4 from list_new to list_values2
for i in list_new:
    if i>4:
        list_values2.append(i)
#a new list list_values3 with same elements as list_values2 but in string form
list_values3=list(map(str,list_values2))
#Using join
v=",".join(list_values3)
print(f"Values greater than 4 is {v}")

print("\n(d)\n")
set_1={1,2}
set_1.clear()
#adding above result in set datatype
for el in list_values2:
    set_1.add(el)
print("Above result in set form is shown below:")
print(set_1)

print("\n(e)\n")
#Making set_1 immutable
frozenset(set_1)
print("The above set converted to immutable.")

print("\n(f)\n")
print(f"Max value from set is {max(set_1)}")
hash_value=hash(max(set_1))
print(f"Hash value of {max(set_1)} is {hash_value}")


                    #Question_4
print("\n         #Question_4")
class student:
    #using constructor to create class objects
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    #defining print function
    def pfun(self):
        print(f"Hello, My name is {self.name} and my "
              f"roll no. is {self.roll_no}")
    #calling destructor
    def __del__(self):
        print("Destructor Called")
#makin Tanish an object of student
Tanish=student("Tanish",21103112)
Tanish.pfun()
del Tanish


                    #Question_5
print("\n          #Question_5")
class employees:
    #Using constructor to for class objects
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def pfun(self):
        print(f"Employee Name is {self.name} and Salary is {self.salary} ")
emp1=employees("Mehak",40000)
emp2=employees("Ashok",50000)
emp3=employees("Viren",60000)
emp1.pfun()
emp2.pfun()
emp3.pfun()
#Updating salary of Mehak to 70000
print("\n(a)")
emp1.salary=70000
print("Mehak salary Updated to 70000")
emp1.pfun()
#Deleting Viren's data
print("\n(b)")
del emp3
print("Employee Viren data removed.")


                   #Question_6
print("\n           #Question_6")
print("\n FRIENDSHIP GAME")
#definig principle of game i.e. anagram
def anagram(word1,word2):
    #converting all letters to lowercase
    word1=word1.lower()
    word2=word2.lower()
    #form empty list to store letters of words
    list1=[]
    list2=[]
    for x in word1:
        list1.append(x)
    for x1 in word2:
        list2.append(x1)
    #sorting the list alphabetically
    list1.sort()
    list2.sort()
    if list1==list2:
        return True
    else:
        return False

player_1=str(input("\nEnter Player1 name:"))
player_2=str(input("Enter Player2 name:"))
#taking words spoken by written
word_player_1=str(input(f"\nEnter Word by {player_1}:"))
word_player_2=str(input(f"Enter Word by {player_2}:"))
#using anagram function
result=anagram(word_player_1,word_player_2)
#printing the final result
if result==True:
    print(f"\nFriendship of {player_1} and {player_2} is REAL")
elif result==False:
    print(f"\nFriendship of {player_1} and {player_2} is FAKE")