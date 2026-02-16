def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def devide(a, b):
    if b == 0:
        raise ValueError("error devide by zero")
    return a/b