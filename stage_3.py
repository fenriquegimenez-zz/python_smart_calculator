while True:
    try:
        n = input()
        if n == '/help':
            print('The program calculates the sum and the rest of numbers')
            continue
        elif n == '':
            continue
        elif n == '/exit':
            print('Bye!')
            break
        elif n[0] == '/' and n != '/exit' and n != '/help':
            print('Unknown command')
        print(eval(n))
    except Exception:
        print('Invalid expression')