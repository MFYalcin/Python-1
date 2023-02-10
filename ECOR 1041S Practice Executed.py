x = input('Please enter your password: ')
count = 1
while  x.lower() != 'python' and count < 3:
    print('Try again')
    count += 1
    x = input('Please enter your password: ')
    
if count == 3 and x.lower() != 'python':
    print('You are locked out!')
else:
    print('Welcome')