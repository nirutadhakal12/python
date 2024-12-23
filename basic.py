# my_variable = 10
# total_count = 5
# user_name = "Niruta"
# print ("This is my my_variable:", my_variable)
# print ("This is my total_count:",total_count)
# print ("This is my user_name:",user_name)

# x,y,z=1,2,3
# print("valueof x:",x)
# print("valueof y:",y)
# print("valueof z:",z)

# result=5+4
# print("sum of 5+4:",result)
# result=5-4
# print("diff of 5-4:",result)
# result=5/4
# print("division of 5/4:",result)
# result=5*4
# print("product of 5*4:",result)
# result=5//4
# print("floor division of 5//4:",result)
# result=5%4
# print("Modulus of 5%4:",result)
# result=5**4
# print("Quotient of 5**4:",result)

# x=20
# y=20
# z=30
# print(x==y or y==z)
# print(x>=y and y<=z)
# print(x>=y or y<=z)
# print(not(x==y))

# x=["abc","cde"]
# y=["abc","cde"]
# z=x
# print(x is z)

# value="Niruta!"
# print("t" in value)
# print("l" not in value)

# x=10
# x=x+5
# # x+=5
# print(x)
# x=10
# x=x-5 
# x-=5
# print(x)

'''DATATYPE'''
# integer,float,string,complex
# w="abc"
# x=1
# y=1.27
# z=1+2j
# print(type(w))
# print(type(x))
# print(type(y))
# print(type(z))
# list
# a=[1,1.27,"abc",1+2j] 
# print(type(a))
# tuple
# b=(1,"abc",1.2)
# print(type(b))
# None data type
# c=None
# print(type(c))
# frozenset
# d=frozenset({"apple","banana","cherry"})
# print(type(d))
# set
# e={"apple","banana","cherry"}
# print(type(e))
# range
# f=range(6)
# print(type(f))
# dict
# g={"name":"Niruta","age":21}
# print(type(g))
# boolean
# h=True
# print(type(h))

# value_x=float(input("enter the first number"))
# value_y=float(input("enter the first number"))
# print(type(value_x))
# print(type(value_y))
# result=value_x+value_y
# print(result)

# value=input("Enter a number: ")
# if value.isdigit():
#   num=int(value)
#   print(f"Converted to integer:{num}")
# elif '.' in value:
#  num=float(value)
#  print(f"Converted to float:{num}")
# else:
#  print("Invalid number input")  

# a=input("enter the value of a:")
# b=input("enter the value of b:")
# if a > b:
#   print("a is greater than b")
# elif b>a :
#   print("a is greater than b")
# else:
#   print("a and b are equal")

# a = 1
# b = 4
# c=5
# a=input("enter the value of a:")
# b=input("enter the value of b:")
# c=input("enter the value of c:")
# if a>b  and b>c:
#   print("a is greater than b and b is greater than c")
# elif a == b and c==0:
#   print("a and b are equal and c is 0")
# elif a==b and b==c and a==b==c!=0:
#   print("a and b are equal and b and c are equal and no zer0")
# else:
#   print("condition not matched")

# x=20
# if x>0 and x<10:  
#  print("x is a positive single-digit number")
# elif x>=10:
#     print("x is a positive number,but not a single-digit")
# else:
#     print("x is Negative")

# while True:
#     num = int(input("Enter the number"))
#     if num == 3:
#         print("the number is")
#         break
#     print("num",num)
# print("outside the loop")    

# num= int(input("Enter the number"))
# for num in range(10):
#   if num == 4:
#      break
#   print("num",num)
# print("outside the loop")  

# num = int (input("Enter th number"))
# for num in range(10):
#    if num<5:
#       break
#    print("num",num)
# print("outside the loop")   

# sum = 0
# for x in range(1,31):
#    if x == 10: 
#       continue
#    sum += x
# print("Total sum",sum)   

# for x in range(5):
#     print("x",x)

#     for y in range(5):
#         print("y",y)   


# x = 1
# y = 2
# print("before swap x is",x)
# print("before swap y is",y)

# x,y = y,x
# print("after swap x is",x)
# print("after swap y is",y)

# x= 5
# y= 9
# print("before swap x is",x)
# print("before swap y is",y)
# z=x
# x=y
# y=z
# print("before swap x is",x)
# print("before swap y is",y)

# x=5
# print("x",x)
# y=10
# print("y",y)
# x = x + y
# y = x - y
# x = x - y
# print("x",x)
# print("y",y)

# 1
# 12
# 123
# 1234
# 12345

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j,end=" ")
#     print("\n")

# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print(j, end=" ")
#         j += 1
#     print("\n")
#     i += 1

# multiline_string="""
# singleline_string=""

# s="Hello World!"
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# print(s[5])
# print(s[6])
# print(s[7])
# print(s[8])
# print(s[9])
# print(s[10])
# print(s[11])

# var="invalid escape sequence"
# count_e=var.count("e")
# print(count_e)

# var="invalid escape sequence"
# print(len(var))
# count=0
# for x in range(len(var)):
#     if var[x]=="e":
#      count=count+1
# print(count)

# var="invalid escape sequence"
# a=0
# for x in var:
#     a=a+1
#     print(x,a)

'''Slicing'''
# s="Hello World!"
# print(s[6:11])
# print(s[6:11:2])
# print(s[5:0:-1]) 

# s="Hello World!"
# print(s[::-1])
# rev=s[::-1]
# org=s 
# if rev==org:
#     print("it is palindrome")
# s="Hello World"
# for char in s:
#      if char.lower()=="h":
#         print("The character is 'h' or 'H'.")
#      else:
#         print(f"The character is '{char}, not 'h' or 'H'. ")
# s[0]="h"  //this will raise a TypeError

# s="Hello"
# s="h"+s[1:]
# print(s)

'''String Method'''
# s="Hello World"
# s=s.replace("World","Python")
# print(s)
# print(s.lower())
# print(s.upper())
# print(s.title())

# s="  Hello World  "
# print(s.lstrip()) //.lstrip()->agadi ko space hatauxa
# print(s.rstrip()) //.rstrip()->paxadi ko space hatauxa
# print(s.strip()) //.strip()->dubai tira ko space hatauxa

# s="Hello World! I am Niruta Dhakal."
# print(s.split())  //.split->le xutauxa
# s=" "
# words=["Hello ","World ","I am Niruta."]
# print(s.join(words)) //.join->le jodxa
# s="hello"
# print(s.islower()) //yasle if cased character sub lower ma xa vane true print garxa nattra false print garxa

# a=10
# b=20
# s=f"The sum of {a} and {b} is {a+b}."
# print(s)

# s="hello, {}!"
# print(s.format("world"))

# s="###############hello###world#############"
# s=s.strip("#")
# print(s.replace("###"," "))

# a=" "+"hello"+"#"*3+"world"+" "
# a=f"{"#"*8}Hello###world{"#"*8}"
# a=a.replace(" ","################")

# output="###############hello###world#############"
# input="hello world"
# total_output_length=len(output)
# removing_left_side_length=len(output.rstrip("#"))
# left_side_value=total_output_length-removing_left_side_length
# removing_right_side_length=len(output.rstrip("#"))
# right_side_value=total_output_length-removing_right_side_length
# a="#"*left_side_value+"hello"+"#"*3+"world"+"#"*right_side_value
# print(a)

'''List'''
# numbers=[1,2,3,4,5,6,7,8,9,10]
# fruits=['apple','banana','cherry','orange','mango','grapes']
# mixed_list=[10,'apple',True,3.14]
# print(numbers[0:4])
# print(fruits[:4])
# print(mixed_list[2:])

'''change'''
# thislist=['apple','banana','cherry']
# thislist[1]='Pineapple'
# print(thislist)

# thislist=['apple','banana','cherry','orange','mango','grapes']
# print(thislist[1:3])
# thislist[1:3]=['Pineapple']
# print(thislist)

'''Insert'''
# thislist=['apple','banana','cherry']
# thislist.insert(2,'Pineapple')
# print(thislist)

'''append'''
# thislist=['apple','banana','cherry']
# thislist.append('Pineapple')
# print(thislist)

'''Extend List'''
# thislist=['apple','banana','cherry']
# tropical=['orange','mango','grapes']
# thislist.extend(tropical)
# print(thislist)

# mixed=[1,'apple','banana',2,3,7,'cherry',True,4,9,6]
# numbers =[x for x in mixed if isinstance(x, (int, float)) and not isinstance(x, bool)]
# odd_numbers = [x for x in numbers if x % 2 != 0]
# even_numbers = [x for x in numbers if x % 2 == 0]
# print("Odd numbers:", odd_numbers)
# print("Even number:",even_numbers)

# mixed = [1, 'apple', 'banana', 2, 3, 7, 'cherry', True, 4, 9, 6]

# odd_numbers = []
# even_numbers = []
# odd_strings=[]
# even_strings=[]

# for a in range(len(mixed)):
#     if type(mixed[a])==int:
#         if mixed[a] % 2 == 0:
#             print(a, "is even")
#             even_numbers.append(mixed[a])
#         else:
#             print(mixed[a], "is odds")
#             odd_numbers.append(mixed[a])

#     elif type(mixed[a])==str: 
#         if (len(mixed[a]) % 2) == 0:
#             print(mixed[a], "is even string")
#             even_strings.append(mixed[a])
#         else:
#             print(mixed[a], "is odd string")
#             odd_strings.append(mixed[a])            

# print("Odd numbers:", odd_numbers)
# print("Even numbers:", even_numbers)
# print("Odd strings:", odd_strings)
# print("Even strings:", even_strings)

'''Looping and conditionals,len()'''
# fruits=['apple','banana','cherry']
# for fruit in fruits:
#     print(fruit)

# fruits=['apple','banana','cherry']
# index=0
# while index<len(fruits):
#     print(fruits[index])
#     index+=1

'''remove'''
# thislist=['apple','banana','cherry']
# thislist.remove('banana')
# print(thislist)

'''Pop'''
# thislist=['apple','banana','cherry']
# thislist.pop(2)
# print(thislist)

'''del'''
# thislist=['apple','banana','cherry']
# del thislist[0]
# print(thislist)

'''clear the list'''
# thislist=['apple','banana','cherry']
# thislist.clear()
# print(thislist)

# thislist=['apple','banana','cherry','banana','banana','apple','grapes']
# case1 output thislist=['cherry','grapes']
# case2 output thislist=['apple','banana','cherry','grapes']
# case3 output "apple"-count-2

'''case1 output thislist=['cherry','grapes']'''
# case1 = []
# for item in thislist:
#     if thislist.count(item) == 1:
#         case1.append(item)
# print("Case 1:", case1)

'''case2 output thislist=['apple','banana','cherry','grapes']'''
# case2 = []
# for item in thislist:
#     if item not in case2:
#         case2.append(item)
# print("Case 2:", case2)

'''case3 output "apple"-count-2'''
# apple_count = 0
# for item in thislist:
#     if item == 'apple':4
#         apple_count += 1
# print(f"Case 3: 'apple'-count-{apple_count}")

# fruits=['apple','banana','cherry','orange','mango','grapes']
# newlist=[]
# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
#         print(newlist)


# fruits=['apple','banana','cherry','orange','mango','grapes']
# newlist=[x for x in fruits if "a" in x]
# print(newlist)

# numbers=[1,2,3,4,5,6,7,8,9]
# even_list=[x**2 for x in numbers if x%2==0 ]
# print(even_list)

# numbers=[1,2,3,4,5,6,7,8,9]
# for x in numbers:
#     if x%2==0:
#         even_list.append(x**2)
# print(even_list)

# numbers=[1,2,3,4,5,6,7,8,9]
# newlist=[x if x%2==0 else "false" for x in numbers]
# print(newlist)

'''creating list of lists'''
# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(matrix)
# x=matrix[0]
# print(x)
# print(type(x))
# print(x[1])
# print(matrix[1][1])
# for x in matrix:
#     print(x)
#     break

# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# total=0
# for row in matrix:
#     for numbers in row:
#         total +=numbers
# print("The total sum is:",total)

'''.sort and sorted'''
# thislist=['apple','banana','cherry','kiwi','pineapple','mango']
# thislist.sort(reverse=True)
# print(thislist)
# new_list=sorted(thislist)
# print(new_list)

'''Copy'''
# thislist=['apple','banana','kiwi','pineapple','mango']
# list2=thislist.copy()
# list2.append('cherry')
# list2.sort()
# print("list2",list2)
# print("thislist",thislist)

'''List'''
# thislist=['apple','banana','kiwi','pineapple','mango']
# mylist=list(thislist)
# print(thislist)

'''slice operator'''
# numbers=[1,2,3,4]
# mylist=list[:]
# print(mylist)

'''Join two list'''
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)

# for x in list2:
#   list1.append(x)
# print(list1) 

# list1.extend(list2)
# print(list1)

'''Tuples are unchaneable or immutable'''
'''Tuple=used to store multiple items in a single variables  ()small brackets indicates tuple'''
# thistuple = ("apple", "banana", "cherry")
# print(thistuple)

'''Change Tuple values'''
# x=("apple","banana", "cherry")
# y=list(x)
# y[1]="kiwi"
# x=tuple(y)
# print(x)

'''Unpacking tuples  * indicates list'''
# fruits=("apple","banana", "blueberry","mango","kiwi")
# (*red,yellow,blue)=fruits 
# print(red)
# print(yellow)
# print(blue)

'''Multiply Tuples'''
# fruits=("apple","banana", "blueberry")
# mytuple=fruits*2
# print(mytuple)

'''set'''
# a={}
# print(type(a))

# a=set()
# print(a)

# my_set={"a","b","c","d"}
# print(my_set)

# thisset={'apple','banana','kiwi','pineapple','pineapple','apple'}
# print(thisset)

'''add set'''
# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)

'''update()'''
# thisset = {"apple", "banana", "cherry"}
# fruits = {"pineapple", "mango", "papaya"}
# thisset.update(fruits)
# print(thisset)

'''remove() and discard'''
# thisset={"apple", "banana", "cherry","grapes"}
# thisset.remove("banana")
# thisset.discard("grapes")
# print(thisset)

'''pop()'''
# thisset={"apple", "banana", "cherry","grapes"}
# x=thisset.pop()
# print(x)
# print(thisset)

'''Loop set'''
# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)

'''Union'''
# set1={"a","b","c","d"}
# set2={1,2,3,4}
# set3={"Josh","Niruta","Ishant"}
# set4={"apple", "banana", "cherry"}
# set5=set1.union(set2,set2,set3,set4)
# print(set5)

'''use | to join two set'''
# set1={"a","b","c","d"}
# set2={1,2,3,4}
# set3={"Josh","Niruta","Ishant"}
# set4={"apple", "banana", "cherry"}
# set5=set1|set2|set3|set4
# print(set5)

'''intersection()'''
# set3={"Josh","Niruta","Ishant","apple","banana",5}
# set4={"apple", "banana", "cherry","Ishant"}
# set1={1,2,3,4,5}
# set2=set3.intersection(set4)
# print(set2)

'''You can use the & operator instead of the intersection() method'''
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 & set2
# print(set3)

'''intersection_update()'''
# set1 = {"apple", "banana", "cherry","a"}
# set2 = {"google", "microsoft", "apple","a"}
# set3={"a","b","c","d"}
# set4={1,2,3,4,"a"}
# set1.intersection_update(set2,set3,set4)
# print(set1)

'''The values True and 1 are considered the same value. The same goes for False and 0'''
# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}
# set3 = set1.intersection(set2)
# print(set3)

'''Difference()'''
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set={"Josh","Niruta","Ishant","apple"}
# set3=set1.difference(set2,set)
# print(set3)

'''-'''
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = {"apple", "cherry"}
# set4 = { "microsoft", "apple"}
# set5=set1-set2-set3-set4
# print(set5)

'''difference_update'''
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.difference_update(set2)
# print(set1)

'''symmetric_difference()'''
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2)
# print(set3)

'''symmetric_difference for more than 2 sets==we use '^' this symbol'''
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = {"apple", "cherry"}
# set4 = { "microsoft", "apple"}
# set = set1^set2^set3^set4
# print(set)

'''disjoint'''
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set=set1.isdisjoint(set2)
# print(set)

'''subset'''
# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}
# w=y.issuperset(x)
# z = x.issubset(y)
# print(z)
# print(w)

'''x=((1,2),(2,3),(4,5),(6,7),(0,2),(3,2))
find the sum of each tuple and print the tuple which has highest sum
output: tuple (1,2) and sum is 3'''

# x = ((1, 2), (2, 3), (4, 5), (6, 7), (0, 2), (3, 2))
# max_sum = 0
# max_tuple = None
# for t in x:
#     current_sum = sum(t)
#     if current_sum > max_sum:
#         max_sum = current_sum
#         max_tuple = t
# print(f"Tuple with the highest sum is {max_tuple} and the sum is {max_sum}")

'''Dictionary'''
# # Empty dictionary
# empty_dict={}
# my_dict={
#     "name":"Niruta",
#     "age":30,
#     "city":"Bhaktapur"
# }
# my_dict["age"]=31
# print(my_dict)
# my_dict["gender"]="Female"
# print(my_dict)
# # print(my_dict["name"])
# print(my_dict.get("address","Changunarayan-8,bhaktapur"))
# # Dictionary with mixed key types
# mixed_dict={
#     1:"one",
#     "2":"two",
#     (1,2):"tuple"
# }

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x=car.keys()
# x=car.values()
# x=car.items()
# print(x)
# car["color"]="white"
# print(x)

# students = {
#   "name": "Niruta",
#   "rollno": 12,
#   "address": "Bkt"
# }
# for key, value in students.items():
#     if key=="rollno" and value==12:
#         students["rollno"]==1
# if students.get("phone_no")==None:
#     students["Phone_no"]="9749844152"      
# print(students.items())

'''Nested Dictionary'''   
# myfamily={}
# myfamily["child1"]={
#     "name":"Niruta",
#     "year":2002
# }
# myfamily["child2"]={
#     "name":"Joshna",
#     "year":2001
# }
# myfamily["child3"]={
#     "name":"Ishant",
#     "year":2000
# }
# myfamily["child4"]={
#     "name":"Niraj",
#     "year":2003
# }
# myfamily["chlid1"]["year"]="Bhaktapur"
# print(myfamily)

# n=int(input("Enter the number of child"))
# for x in range(n):
#     name=input("Enter the name of child")
#     year=input("Enter the age of child")
#     myfamily[f"child{x}"]={
#     "name":"Niruta",
#     "year":2002
#     }
# print(myfamily)


# students={
# 1:{    
#     "name":"Niruta",
#     "age":22,
#     "marks":{
#         "english":75,
#         "maths":80,
#         "science":30
#     }
# },
# 2 : {
#     "name":"Joshna",
#     "age":23,
#     "marks":{
#         "english":65,
#         "maths":89,
#         "science":50
#     }
# },
# 3: {
#     "name":"Niraj",
#     "age":24,
#     "marks":{
#         "english":70,
#         "maths":87,
#         "science":31
#     }
# },
# 4: {
#     "name":"Ishant",
#     "age":22,
#     "marks":{
#         "english":70,
#         "maths":97,
#         "science":31
#     }
# },  
# }
# total=0
# top_student=None
# for keys, values in students.items():
#     if total > 
#     for subject, marks in values["marks"].items():
#         total += marks

#     print(f"Total marks for {values['name']} (ID {keys}): {total}")

# highest_score=0
# top_student=""

# for x,y in students.items():
#     total_sum=sum(y["marks"].values())
#     print(f"The student {y["name"]} has scored {total_sum}")

#     if total_sum>highest_score:
#         highest_score=total_sum
#         top_student=y["name"]

# print(f"The highest score is scored by {top_student} which is {highest_score}")

# def get_stats(numbers):
#     min_value=min(numbers)
#     max_value=max(numbers)
#     sum_value=sum(numbers)
#     return min_value,max_value,sum_value
# numbers=[1,2,3,4,5]
# result=get_stats(numbers)
# print(result)
# print(result[0])

# def get_stats(numbers):
#     return{
#     "min":min(numbers),
#     "max":max(numbers),
#     "sum":sum(numbers)
#     }
# numbers=[1,2,3,4,5]
# stats=get_stats(numbers)
# print("Minimum:",stats["min"])
# print("Maximum:",stats["max"])
# print("sum:",stats["sum"])

'''with parameter'''
# def subtraction(c,d):
#     result=c-d
#     return result
# x=subtraction(2,4)
# print(x)

'''without parameter'''
# def sub():
#     x=2
#     y=4
#     result=x-y
#     return result
# x=sub()   
# print(x)

'''with parameter without return'''
# def minus(e,f):
#     result=e-f
#     print("result",result)
# minus(2,2)

'''without parameter without return''' 
# def subtract():
#     a=2
#     b=4
#     result=a-b
#     print("result",result)
# subtract() 
 
'''Local Variable'''
# def my_function():
#     x=20
#     print("Inside function:",x)
# my_function()
# print("outside fuction:",x)

'''Global Variable'''
# y=20
# def my_function():
#     print("Inside function:",y)
# my_function()
# print("outside fuction:",y)

'''using global keyword'''
# y=20
# def update_global():
#     global y
#     y=y+5
#     print("Inside function:",y)
# update_global()
# print("outside fuction:",y)

'''create a function to find the number is odd or even'''
# def check_odd_or_even(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# num = 8
# result = check_odd_or_even(num)
# print("result",result)

'''create a function to check palindrome'''

# def is_palindrome(value):
#     value_str = str(value)
#     return value_str == value_str[::-1]
# word = "hahah"
# result = is_palindrome(word)
# if result:
#     print(f"'{word}' is a palindrome.")
# else:
#     print(f"'{word}' is not a palindrome.")

'''create a function to check arm strong'''
# def is_armstrong_number(number):

'''Arbitrary Arguments *args'''
# def my_function(*kids):
#     print("The younger clild is " +kids[0])
#     print("The middle clild is " +kids[1])
#     print("The middle clild is " +kids[2])
#     print("The eldest clild is " +kids[3])
# my_function("Niruta","Joshna","Ishant","Niraj")

'''Arbitrary keyword Arguments **kwargs'''
# def my_function(**kid):
#     print("Her Last Name is " +kid["name1"])
# my_function(fname="Niruta", name1="Dhakal")

'''Lambda Function'''

'''Add 10 to argument'''
# x=lambda a:a+10
# print(x(5))
'''Add argument a,b&c'''
# x=lambda a,b,c:a+b+c
# print(x(5,6,7))
'''Mulptily argument a with argument b'''
# x=lambda a,b:a*b
# print(x(5,6))

'''class and object'''
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def great(self):
#     print(f"hello my name is {self.name} and my age is {self.age}")
# p1 = Person("Josh", 22)
# p2 = Person("Niruta", 23)
# p3 = Person("Ishant", 24)
# p3.great()
# # print(p1.name)
# # print(p1.age)
# # print(p2.name)
# # print(p2.age)


# class rect_area:
#   def __init__(self ,length, breadth):
#     self.length=length
#     self.breadth=breadth
#   def area(self):
#     print("area:",self.length*self.breadth)  
# react_box=rect_area(10,20)
# react_window=rect_area(50,80)
# react_door=rect_area(100,20)
# react_box.area()
# react_window.area()
# react_door.area()


# class rect_area:
#   def __init__(self ,length, breadth):
#     self.length=length
#     self.breadth=breadth
#   def area(self):
#     result=self.length*self.breadth
#     return result
# react_box=rect_area(10,20)
# react_window=rect_area(50,80)
# react_door=rect_area(100,20)
# react_box_result=react_box.area()
# react_window_result=react_window.area()
# react_door_result=react_door.area()
# print(react_box_result)
# print(react_window_result)
# print(react_door_result)

'''Inheritance'''
'''Single Inheritance'''
# class Animal:
#   def speak(self):
#     return "Animal speaks"
# class Dog(Animal):
#   def bark(self):
#     return "Dog barks"
# my_dog=Dog()
# print(my_dog.speak())
# print(my_dog.bark())

'''Multiple Inheritance'''
# class A:
#   def method_A(self):
#     return "Method A"
# class B:
#   def method_B(self):
#     return "Method B"
# class C(A,B):
#   def method_C(self):
#     return "Method C"
# obj_C=C()
# print(obj_C.method_A())
# print(obj_C.method_B())
# print(obj_C.method_C())

'''Multilevel Inheritance'''
# class A:
#   def method_A(self):
#     return "Method A"
# class B(A):
#   def method_C(self):
#     return "Method B"
# class C(B):
#   def method_B(self):
#     return "Method C"
# obj_C=C()
# print(obj_C.method_A())

'''Super()'''
# class Rectangle:
#   def __init__(self,length,width):
#     self.length=length
#     self.width=width
#   def area(self):
#     return self.length*self.width
# class square(Rectangle):
#   def __init__(self,side_length):
#     super().__init__(side_length,side_length)
# s=Rectangle(5,3)
# square = square(4)
# print("Area of Rectangle:", s.area())
# print("Area of Square:", square.area())

'''Created custom exception'''
# class negative_error(Exception):
#   def __init__(self, message):
#     super().__init__(message)
# class zero_error(Exception):
#   def __init__(self, message):
#     super().__init__(message)
# x= int (input ("enter the age"))
# try:
#   if x<0:
#     raise negative_error("sorry, no number below zero")
#   elif x==0:
#     raise zero_error("sorry, age is zero")
# except negative_error as e:
#   print(e)
#   print('you have entered negative number')
#   x= int (input("Re-enter the age"))
#   print("the age is ",x)

'''raised raise exception to handle exception'''
# x= int (input ("enter the age"))
# try:
#   if x<0:
#     raise Exception("sorry, no number below zero")
#   elif x==0:
#     raise Exception("sorry, age is zero")
# except Exception as e:
#   print(e)
#   print('you have entered negative number')
#   x= int (input("Re-enter the age"))


'''  raised inbuilt Exception to handle different cases with same Except block'''
#   try:
#     x=int(input("enter the number for x"))
#     y=int(input("enter the number for y"))
#     result=x/y
#     print("result", result)
#   except Exception as e:
#     print(f"error{e}")
#     x=int(input("enter the number for x"))
#     y=int(input("enter the number for y"))
#     result=x/y
#     print("result", result)


'''raised inbuilt Exception to handle different cases with different Except block'''
'''zerodivisionerror'''
#   try:
#     x=int(input("enter the number for x"))
#     y=int(input("enter the number for y"))
#     result=x/y
#     print("result", result)
#   except ZeroDivisionError as e:
#     print("you have enter zero")
#     x=int(input("enter the number for x"))
#     y=int(input("enter the number for y"))
#     result=x/y
#     print("result", result)

'''typeerror'''
#   except TypeError as e:
#     print("you have enter zero")
#     x=int(input("enter the number for x"))
#     y=int(input("enter the number for y"))
#     result=x/y
#     print("result", result)

'''traceback'''
# import traceback
# def divide():
#   print("hello before try except")
#   try:
#     x= int(input("enter the number for x"))
#     y= int (input("enter the number for y"))
#     result=x/y
#     print(z)
#     print("result",result)
#   except Exception as e:
#     traceback.print_exc()
#     print(f"handle all exception{e}")
# divide()

'''File Handling'''
'''read'''
# f = open("demofile.txt", "r")
# print(f.read())
'''Readline'''
# # print(f.readline())
# # print(f.readline())
'''type'''
# # value=f.read()
# # print(type(value))
'''loop'''
# for x in f:
#     print(x)
'''close'''
# f.close()

# f = open("demofile.txt", "r")
# value=f.readlines()
# print("value",value)


'''read,write.append,close'''

# f = open("demofile.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# f = open("demofile.txt", "r")
# print(f.read())

# f = open("demofile.txt", "w")
# f.write("Now the file has more content!")
# f.close()

# f = open("demofile.txt", "r")
# print(f.read())
 
'''read()'''
# file_path='demofile.txt'
# with open(file_path,'r')as file:
#     content=file.read()
#     print(content)

# a=["hello\n","world\n"]
# f.writelines(a)
# f.writelines("hello\n")
# f.writelines("world\n")

'''Deete a file'''
# import os
# os.remove("demofile.txt")

'''Check if File exist:'''
# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")

'''Delete Folder'''
# import os
# os.rmdir("myfolder")


'''# # Data representing the students and their marks'''
# students = [
#     ["ram", 13, 57, 60, 70],
#     ["shyam", 10, 55, 70, 72],
#     ["hari", 11, 40, 80, 50],
#     ["abc", 12, 60, 85, 60],
#     ["xyz", 14, 70, 55, 77]
# ]

# # Open a file to store the results
# output_file = "student_totals.txt"
# with open(output_file, "w") as file:
#     file.write("Name, Age, Total Marks\n")
    
#     # Calculate and write the total marks for each student
#     for student in students:
#         name = student[0]
#         age = student[1]
#         marks = student[2:]
#         total_marks = sum(marks)
        
#         # Write the result to the file and print it
#         file.write(f"{name}, {age}, {total_marks}\n")
#         print(f"{name}: Total Marks = {total_marks}")

# print(f"Results have been saved to '{output_file}'.")
  

# import csv
# data =[
#     ['Alice', 30, 'London'],
#     ['Bob', 25, 'Paris'],
#     ['Charlie', 35, 'Berlin']
# ]

# file_path = 'output.csv'
# with open(file_path, mode='w', newline='') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(['Name', 'age', 'city'])
#     for row in data:
#         csv_writer.writerow(row)


# import csv
# data =[
#     ['Alice', 30, 'London'],
#     ['Bob', 25, 'Paris'],
#     ['Charlie', 35, 'Berlin']
# ]
 
# with open("input.csv", mode='w', newline='') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(['Name', 'age', 'city'])
#     while True:
#         if input("enter 1 for exit else any key")=='1':\
#         break
#         name = input("enter the name:")
#         age = int(input("enter the age"))
#         city = input("enter the city")

#         ra = [name, age, city]
#         csv_writer.writerow(ra)

# print("Data has been written to 'input.csv'")
        
# while True:
#     name = input("Enter the name: ")
#     age = int(input("Enter the age: "))
#     city = input("Enter the city: ")
#     data.append([name, age, city])
#     continue_input = input("Do you want to add another entry? (yes/no): ").lower()
#     if continue_input != 'yes':
#         break

# print("the Data is :")
# for entry in data:
#     print(entry)


# import csv
# file_path = 'data.csv'
# with open(file_path, mode ='r') as file:
#     csv_reader = csv.reader(file)
#     header = next(csv_reader)
#     for row in csv_reader:
#      print(row)


# import csv
# file_path = 'data.csv'
# with open(file_path, mode ='r') as file:
#     csv_reader = csv.DictReader(file)
#     header = next(csv_reader)
#     for row in csv_reader:
#      print(row['Name'], row['age'], row['city'])

# import csv

# data =[
#     {'Name': 'Alice', 'Age': 30, 'City': 'London'},
#     {'Name': 'Bob', 'Age': 20, 'City': 'Paris'},
#     {'Name': 'Ali', 'Age': 25, 'City': 'KTM'}
# ]

# file_path = 'output.csv'
# fieldnames = ['Name', 'Age', 'City'] 

# with open(file_path, mode='w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     for row in data:
#         writer.writerow(row)

# import matplotlib.pyplot as plt
# x = [1,2,3,4,5]
# y = [2,3,5,7,11]

# x1 = [6,7,8,9,10]
# y1 = [2,3,5,7,11]

# plt.plot(x,y, marker= 'o', linestyle= '--', color ='b', label='prime_numbers')
# plt.plot(x1,y1, marker = 'o',linestyle = '-' ,color = 'r',label = ' Numbers' )

# plt. xlabel('x Axis')
# plt. ylabel('y Axis')
# plt.title('Prime numbers plot')

# plt.legend()
# plt.show()

# import mymodule as my
# my.mul(1,2)
# my.sum(1,2)
# my.diff(1,2)

# from mymodule import sum as sm , diff as df
# sm(1,8)
# df(2,9)

# import module
# module.fd(1,2)
# module.mod(2,6)

# import pandas as pd
# data={'Name':['Alice','Bob','charlie'],
#       'Age':[25,30,35],
#       'city':['New york','Bkt','ktm']
#       }
# df=pd.DataFrame(data)
# print(df)

# df=pd.read_csv('data.csv')
# print(df.head())

# import pandas as pd
# df = pd.read_csv('data.csv')

# new_df = df.dropna()

# df.fillna(130, inplace = True)

# df["Calories"].fillna(130, inplace = True)
# print(df.to_string())
'''Convert Into a Correct Format'''
# import pandas as pd

# df = pd.read_csv('data.csv')

# df['Date'] = pd.to_datetime(df['Date'],format="mixed")

# print(df.to_string())

# import pandas as pd

# df = pd.read_csv('data.csv')

# df.loc[7,'Duration'] = 45

# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.loc[x, "Duration"] = 120

# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.drop(x, inplace = True)

# print(df.duplicated())

# df.drop_duplicates(inplace = True)
# print(df.to_string())

'''Map'''
# numbers=[1,2,3,4,5]
# squared=list(map(lambda x:x**2,numbers))
# print(squared)
'''without using lambda'''
# def squared(x):
#    return x**2
# numbers=[1,2,3,4,5]
# squared = list(map(squared, numbers))
# print(squared)
'''Filter'''
# numbers=[1,2,3,4,5,6,7,8,9,10]
# odd_numbers=list(filter(lambda x:x%2!=0,numbers))
# print(odd_numbers)

# numbers=[1,2,3,4,5,6,7,8,9,10]
# def even_numbers(x):
#     if x%2==0:
#       return x
# even_number=list(filter(even_numbers,numbers))
# print(even_number)

'''reduce()'''
# from functools import reduce
# numbers=[1,2,3,4,5]
# sum=reduce(lambda x,y:x+y,numbers)
# print(sum)

# numbers=[3,8,1,6,2]
# max_num=reduce(lambda x,y:x if x>y else y,numbers)
# print(max_num)

# words=["Hello", " ","World", "!"]
# sentence=reduce(lambda x,y:x+y,words)
# print(sentence)

# numbers=[1,2,3,4,5]
# product=reduce(lambda x,y:x*y,numbers,1)
# print(product)

'''os library'''
# import os
# current_dir=os.getcwd()
# files=os.listdir(current_dir)
# print(files)
'''random library'''
# import random
# random_number=random.randint(1,10)
# my_list=[1,2,3,4,5]
# random.shuffle(my_list)
# print(random_number)

'''math library'''
# import math
# sqrt_value=math.sqrt(25)
# factorial_value=math.factorial(5)
# print(sqrt_value)
# print(factorial_value)



import sqlite3

conn = sqlite3.connect('data.db')
c= conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, email TEXT)')
conn.commit()
conn.close()

conn = sqlite3.connect('data.db')
c= conn.cursor()
name=input('Enter the name')
age= int(input('Enter the age'))
email=input('Enter the email')
c.execute('INSERT INTO users(name,age,email) VALUES(?,?,?)', (name, age, email))
conn.commit()
conn.close()


# conn = sqlite3.connect('data.db')
# c= conn.cursor()
# c.execute('SELECT* FROM users')
# rows = c.fetchall()
# print(rows)
# conn.close()
# for row in rows:
#     print(row)


# conn = sqlite3.connect('data.db')
# c= conn.cursor()
# name=input("enter the new name")
# user_id=int(input("Enter the id"))
# c.execute('UPDATE users SET name=? WHERE id=?',(name, user_id))
# conn.commit()
# conn.close()


# conn = sqlite3.connect('data.db')
# c= conn.cursor()
# name=input("enter the new name")
# user_id=int(input("Enter the id"))
# age=int(input("enter the new age"))
# email=input("enter the new email")
# c.execute('UPDATE users SET name=?,age=?, email=? WHERE id=?',(name, user_id, age, email))
# conn.commit()
# conn.close()

# conn = sqlite3.connect('data.db')
# c= conn.cursor()
# user_id=int(input("Enter the id"))
# c.execute('DELETE FROM users WHERE id=?',(user_id,))
# conn.commit()
# conn.close()