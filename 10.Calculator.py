# Calculator

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operands = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    loop = True
    num1 = float(input("Enter first number: "))

    for symbol in operands:
        print(symbol)
    operation_symbol = input("Type the symbol from the above operation symbols you want to perform: ")

    num2 = float(input("Enter second number: "))

    calculation_operation = operands[operation_symbol]
    final_output = calculation_operation(num1, num2)

    while loop:
        continue_calc = input("Do you want to continue the calculation?. Type 'y' to continue or 'n' for new "
                              "calculation: ").lower()
        if continue_calc == 'y':
            operation_symbol = input("Type the symbol from the above operation symbols you want to perform: ")
            new_num = float(input("Enter next number: "))
            calculation_operation = operands[operation_symbol]
            final_output = calculation_operation(final_output, new_num)
        else:
            loop = False
            print(f"Your answer is: {final_output}")
            calculator()


calculator()
