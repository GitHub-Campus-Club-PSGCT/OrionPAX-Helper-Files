from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Union

app = FastAPI()

# Example math functions
def add(a: int, b: int) -> int:
    """Adds two integers together."""
    return a + b

def multiply(a: int, b: int) -> int:
    """Multiplies two integers together."""
    return a * b

def subtract(a: int, b: int) -> int:
    """Subtracts the second integer from the first."""
    return a - b

def divide(a: int, b: int) -> Union[int, float, str]:
    """Divides the first integer by the second.
    
    Returns a string if division by zero is attempted.
    """
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def exponentiate(base: int, exponent: int) -> int:
    """Raises the base to the power of the exponent."""
    return base ** exponent

def average(numbers: List[int]) -> float:
    """Calculates the average of a list of numbers."""
    return sum(numbers) / len(numbers)

def factorial(n: int) -> int:
    """Calculates the factorial of a number using recursion."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Pydantic model for handling input with two numbers
class MathOperation(BaseModel):
    a: int
    b: int

# Pydantic model for handling input with a list of numbers
class NumberList(BaseModel):
    numbers: List[int]

# Route to check if the server is running
@app.get("/")
def read_root():
    """Basic route to check if the API is up and running."""
    return {"message": "Welcome to the Math API"}

# Route to add two numbers
@app.post("/add")
def add_numbers(operation: MathOperation):
    """Adds two numbers provided in the request body."""
    result = add(operation.a, operation.b)
    return {"result": result}

# Route to multiply two numbers
@app.post("/multiply")
def multiply_numbers(operation: MathOperation):
    """Multiplies two numbers provided in the request body."""
    result = multiply(operation.a, operation.b)
    return {"result": result}

# Route to subtract two numbers
@app.post("/subtract")
def subtract_numbers(operation: MathOperation):
    """Subtracts the second number from the first number."""
    result = subtract(operation.a, operation.b)
    return {"result": result}

# Route to divide two numbers
@app.post("/divide")
def divide_numbers(operation: MathOperation):
    """Divides the first number by the second number."""
    result = divide(operation.a, operation.b)
    return {"result": result}

# Route to exponentiate a number
@app.post("/exponentiate")
def exponentiate_numbers(operation: MathOperation):
    """Raises the first number (base) to the power of the second number (exponent)."""
    result = exponentiate(operation.a, operation.b)
    return {"result": result}

# Route to calculate the average of a list of numbers
@app.post("/average")
def average_numbers(number_list: NumberList):
    """Calculates the average of a list of numbers."""
    result = average(number_list.numbers)
    return {"result": result}

# Route to calculate the factorial of a number
@app.post("/factorial")
def factorial_number(operation: MathOperation):
    """Calculates the factorial of a number.
    
    Note: Only the first number (`a`) is used; the second (`b`) is ignored.
    """
    result = factorial(operation.a)
    return {"result": result}

# Route to demonstrate a new function
@app.post("/new_function")
def new_function(operation: MathOperation):
    """Placeholder for any new function to be added in the future.
    
    Example: Subtracts the second number from the first.
    """
    result = subtract(operation.a, operation.b)
    return {"result": result}