from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+":add, 
  "-": subtract, 
  "*": multiply, 
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What is the first number?: "))
  for sign in operations:
    print (sign)

  should_continue = True
  while should_continue:
    operation_sign = input("Pick an operation from above ")
    num2 = float(input("What is the next number?: "))
    calculation_function = operations[operation_sign]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_sign} {num2} = {answer}")

    b = input(f"Type 'y' to continue with {answer} or type 'n' to exit.")
    if b == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()


calculator()

