for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

''' Smart Code
for number in range(1, 101):
    output = ""
    output += "Fizz" if number % 3 == 0 else ""
    output += "Buzz" if number % 5 == 0 else ""
    print(output if output else number)
'''