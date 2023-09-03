#Calculator
from calc_art import logo
# Add
def add(n1,n2):
  return n1 + n2
# Subtract
def subtract(n1,n2):
  return n1 - n2
# Multiply
def multiply(n1,n2):
  return n1 * n2
# Divide
def divide(n1,n2):
  return n1 / n2

operations = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide,
}
def calculator():
  print(logo)
  to_continue = 'y'
  num1 = float(input("What is the first number?: "))
  
  for operation in operations:
    print(operation)
    
  while to_continue == 'y':
    operation_symbol = input("Pick an operation above from the line above: ")
    if operation_symbol not in operations:
      print("Not a valid operation. Start over.")
      calculator()
    num2 = float(input("What is the second number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    to_continue = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start over. Type exit to leave the program. ")
    if to_continue == 'y':
      num1 = answer
    elif to_continue == 'n': 
      calculator()
    elif to_continue != 'y' and to_continue != 'n':
         break

calculator()
    