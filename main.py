first_number = float(input('Enter a number: '))
operator = input('Enter an operation (+, - , /, *) : ')
second_number = float(input('Enter a number: '))
result = 0

if first_number != None and operator != None and second_number != None:
    if operator == '+':
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    elif operator == '/':
        result = first_number / second_number
    elif operator == '*':
        result = first_number * second_number
    else:
        result = "Something went wrong..."
else:
    result = "Something went wrong..."

print(result)
