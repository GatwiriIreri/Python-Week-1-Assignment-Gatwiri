# week 1 assignment

num1 = float(input('Enter the first number:'))
num2 = float(input('Enter the second number:'))

# the operations
operation = input('Enter an operation (+, -, *,/)')

if operation == '+':
    result = num1 + num2
    print(f'{num1} + {num2} = {result}')

elif operation == '-':
    result = num1 - num2
    print(f'{num1} - {num2} = {result}')

elif operation == '*':
    result = num1 * num2
    print(f'{num1} * {num2} = {result}')

elif operation == '/':
    result = num1 / num2
    print(f'{num1} / {num2} = {result}')

else:
    print('Invalid Operator')
