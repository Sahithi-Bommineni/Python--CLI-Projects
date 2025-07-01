#Calculator
def get_number(number):
    while True:
        try:
            return float(input(f"enter number {number}: "))
        except:
            print("Invalid, Try again")
        
operand1 = get_number(1)
operand2 = get_number(2)
operator = input("enter operator(+,-,*,/,%): ")
result = 0
match operator:
    case '+':
        result = operand1 + operand2
    case '-':
        result = operand1 - operand2
    case '*':
        result = operand1 * operand2
    case '/':
        result = operand1/operand2
    case '%':
        result = operand1%operand2
    case default:
            print("invalid operator, try again")
print(result)