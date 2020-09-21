while True:
    n = input()
    if n == '/help':
        print('The program calculates the sum and the rest of numbers')
        continue
    elif n == '':
        continue
    elif n == '/exit':
        print('Bye!')
        break
    print(eval(n))