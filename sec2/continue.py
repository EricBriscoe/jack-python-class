name = ''

while True:
    if name != 'Jack': 
        print('Who are you?')
        name = input('Enter Name: ')

    if name != 'Jack':
        continue

    print("Hello, Jack. What is the password? (It's 'fish'.)")
    password = input('Enter Password: ')

    if password == 'fish':
        break

print('Access Granted!')
