# Python simple calculator

#adds two numbers
def add(x, y):
    return x + y

#subtracts two numbers
def subtract(x, y):
    return x - y

#multiplies two numbers
def multiply(x, y):
    return x * y

#divides two numbers
def divide(x, y):
    return x / y


print("Select an operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    #takes input from the user
    choice = input("Enter your choice(1/2/3/4): ")

    # checks if the choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        input1 = float(input("Enter first number: "))
        input2 = float(input("Enter second number: "))

        if choice == '1':
            print(input1, "+", input2, "=", add(input1, input2))

        elif choice == '2':
            print(input1, "-", input2, "=", subtract(input1, input2))

        elif choice == '3':
            print(input1, "*", input2, "=", multiply(input1, input2))

        elif choice == '4':
            print(input1, "/", input2, "=", divide(input1, input2))
        
        # checks if the user wants another calculation and breaks the while loop if the answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
