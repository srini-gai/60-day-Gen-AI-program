'''def add(a,b) :
    return a+b 

print(add(5,6))'''

# Define a calculator function
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:   # avoid division by zero
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

'''print(calculator(10, 5, "add"))       # 15
print(calculator(10, 5, "subtract"))  # 5
print(calculator(10, 5, "multiply"))  # 50
print(calculator(10, 5, "divide"))    # 2.0'''

# User input
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
op = input("Enter operation (add/subtract/multiply/divide): ")

print("Result:", calculator(x, y, op))
