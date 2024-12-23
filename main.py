from module import sum as sm, diff as df, div as dv, mul as ml, floor_division as fd,modulus as md

print("......calculator....")
num = int(input("enter the sum"))
if num == 1 :
     print("the sum is:", sm(int(input("enter first number")), (int(input("enter the second number")))))

num = int(input("enter the diff"))
if num == 2 :
     print("the sum is:", df(int(input("enter first number")), (int(input("enter the second number")))))

num = int(input("enter the div"))
if num == 3 :
     print("the sum is:", dv(int(input("enter first number")), (int(input("enter the second number")))))

num = int(input("enter the mul"))
if num == 4 :
     print("the sum is:", ml(int(input("enter first number")), (int(input("enter the second number")))))    

num = int(input("enter the fv"))
if num == 5 :
     print("the sum is:", fd(int(input("enter first number")), (int(input("enter the second number")))))

num = int(input("enter the mod"))
if num == 6 :
     print("the sum is:", md(int(input("enter first number")), (int(input("enter the second number")))))