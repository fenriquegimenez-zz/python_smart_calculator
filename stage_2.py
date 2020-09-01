# write your code here
n = input()

while n != '/exit':
    if ' ' in n:
        data = n.split()
        a = data[0]
        b = data[1]
        print(int(a) + int(b))
    else:
        print(n)
    print('Bye!')
    break
