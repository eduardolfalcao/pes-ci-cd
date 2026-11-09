# Simple Python Application
import numpy as np

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
        return np.multiply(a, b)

def divide(a, b):
        return a/b

if __name__ == "__main__":
    print(f"Test Addition: {add(1, 2)}")
    print(f"Test Subtraction: {subtract(4, 2)}")
    print(f"Test Multiplication: {multiply(3, 5)}")
    print(f"Test Division: {divide(15, 3)}")
