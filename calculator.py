import math



def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    return a / b

def cosine(x):
    return math.cos(math.radians(x))

def sine(x):
    return math.sin(math.radians(x))

def tangent(x):
    if x % 180 == 90:  # Undefined for 90, 270, etc.
        raise ValueError("Tangent is undefined for this input.")
    return math.tan(math.radians(x))
    
