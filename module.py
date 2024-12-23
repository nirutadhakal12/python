def sum(a,b):
    result=a+b
    print("reult",result)
    return result
def diff(a,b):
    result=a-b
    print("reult",result)
    return result
def mul(a,b):
    result=a*b
    print("result",result)
    return result
def div(a,b):
    result=a/b
    print("result",result)
    return result
def floor_division(a,b):
    result=a//b
    print("result",result)
    return result
def modulus(a,b):
    result=a%b
    print("result",result)
    return result
def factorial(n):
    result=1
    for i in range(1,n+1):
        result *=i
    print("result",result)
    return result