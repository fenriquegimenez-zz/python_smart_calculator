while True:
    try:
        n = input()
        commands = ('/help', '/exit')
        if n == '/help':
            print('The program calculates the sum and the rest of numbers')
            continue
        elif n == '':
            continue
        elif n == '/exit':
            print('Bye!')
            break
        elif n not in commands:
            print('Unknown command')
        print(eval(n))
    except Exception:
        print('Invalid expression')