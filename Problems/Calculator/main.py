# put your python code here
n1 = float(input())
n2 = float(input())
operation = input()

if operation in 'div,/,mod':
    if n2 == 0:
        print('Division by 0!')
    elif operation == '/':
        print(n1 / n2)
    elif operation == 'div':
        print(n1 // n2)
    else:
        print(n1 % n2)
elif operation == '+':
    print(n1 + n2)
elif operation == '-':
    print(n1 - n2)
elif operation == 'pow':
    print(n1 ** n2)
elif operation == '*':
    print(n1 * n2)
