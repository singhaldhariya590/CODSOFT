import os
def add(a,b):    
   return a+b   
def subtract(a,b):   
   return a-b   
def multiply(a,b):   
   return a*b   
def divide(a,b):   
   return a/b   
operations_dict={
   "+":add,
   "-":subtract,
   "*":multiply,
   "/":divide
}

def my_calculator():
    num_1=float(input(" Please enter the first number: ")) 
    for symbol in operations_dict:
        print(symbol)

    continue_flag=True
    while continue_flag:
        operation_symbol=input("\n Pick an operation: ")
        num_2 = float(input(" Please enter the next number: "))
        calculator_function=operations_dict[operation_symbol]
        calculation_output=calculator_function(num_1,num_2)
        print(f" {num_1} {operation_symbol} {num_2} = {calculation_output}")

        calculation_continue=input(f" Enter 'y' to continue calculation with {calculation_output} or 'n' to start a new calculation or 'x' to exit: ").lower()
        if calculation_continue=='y':
            num_1=calculation_output
        elif calculation_continue=='n':
            continue_flag=False
            os.system('cls')  
            my_calculator() 
        else:
            continue_flag=False
            print(" Goodbye😄😄 !!")

my_calculator()