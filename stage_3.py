while True:
    n = input()
    if n == '/help':
        print('The program calculates the sum of numbers')
        continue
    elif n == '':
        continue
    elif n == '/exit':
        print('Bye!')
        break
    nums = n.split()
    print(sum([int(i) for i in nums]))