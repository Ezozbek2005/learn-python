# =======================
# Math Operations
# =======================
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# =======================
# String Utilities
# =======================
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# =======================
# Geometry (Circle)
# =======================
import math

def calculate_area(radius):
    return math.pi * radius * radius

def calculate_circumference(radius):
    return 2 * math.pi * radius

# =======================
# File Operations
# =======================
def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Error: File not found"

def write_file(file_path, content):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    return "File written successfully"

# =======================
# Test / Example Usage
# =======================
if __name__ == "__main__":
    # Math operations
    print("Add:", add(10, 5))
    print("Subtract:", subtract(10, 5))
    print("Multiply:", multiply(10, 5))
    print("Divide:", divide(10, 0))

    # String operations
    text = "hello world"
    print("Reverse:", reverse_string(text))
    print("Vowels count:", count_vowels(text))

    # Geometry
    radius = 7
    print("Circle area:", calculate_area(radius))
    print("Circle circumference:", calculate_circumference(radius))

    # File operations
    file_path = "example.txt"
    write_file(file_path, "This is a test file.")
    print("File content:", read_file(file_path))
