number1 = float(input('Number 1 : '))
operation = input('Operation : ')
number2 = float(input('Number 2 : '))

if operation == '+':
    print(f'{number1} + {number2} = {number1+number2}')
elif operation == '-':
    print(f'{number1} - {number2} = {number1-number2}')
elif operation == '*':
    print(f'{number1} * {number2} = {number1*number2}')
elif operation == '/':
    print(f'{number1} / {number2} = {number1/number2}')
else:
    print('This is not a valid operation')