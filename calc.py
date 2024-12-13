# Simple Python Application
import numpy as np

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
        return np.multiply(a, b)

def divide(a, b):
        return a/-b

if __name__ == "__main__":
    print(f"Addition: {add(1, 2)}")
    print(f"Subtraction: {subtract(4, 2)}")
    print(f"Multiplication: {multiply(3, 5)}")
    print(f"Division: {divide(15, 3)}")
