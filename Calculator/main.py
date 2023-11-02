def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1-n2

def mult(n1, n2):
    return n1*n2

def div(n1, n2):
    return n1/n2


n1 = int(input("Give a first number: "))
n2 = int(input("Give a second number: "))
oper = input("Give me a operation: ")
if oper == "+":
    print(add(n1, n2))
elif oper == "-":
    print(sub(n1, n2))
elif oper == "*":
    print(mult(n1, n2))
elif oper == "/":
    print(div(n1, n2))
else:
    print("Please check your input")