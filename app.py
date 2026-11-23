#!/usr/bin/env python3
"""
Simple Python application for Drone CI testing
"""

def add_numbers(a, b):
    """Add two numbers and return the result"""
    return a + b

def multiply_numbers(a, b):
    """Multiply two numbers and return the result"""
    return a * b

def main():
    """Main function"""
    print("Simple Calculator App")
    print("5 + 3 =", add_numbers(5, 3))
    print("4 * 6 =", multiply_numbers(4, 6))
    print("Application executed successfully!")

if __name__ == "__main__":
    main()

def subtract_numbers(a, b):
    """Subtract two numbers and return the result"""
    return a - b

def divide_numbers(a, b):
    """Divide two numbers and return the result"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
