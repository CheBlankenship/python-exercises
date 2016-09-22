print 'I am thinking of a number between 1 and 10.'

secret_num = '5'

while True:
    guess = str(raw_input('What is the number?'))
    if guess >= secret_num:
        print '%s is too high.' % guess
    guess = str(raw_input('Whaat is the number?'))
            elif guess <= secret_num:
                print '%s is too low.' % guess

if secret_num ==  secret_num:
    print 'Yes! You win!'
