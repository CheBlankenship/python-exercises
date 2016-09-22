print 'I am thinking of a number between 1 and 10.'

secret_num = '5'

guess = str(raw_input('What is the number?'))
while guess >= secret_num:
    print '%s is too low.' % (guess)
    str(raw_input('What is the number?'))
    guess <= secret_num
    print '%s is too high.' % (guess)
    break
if guess == secret_num:
    print 'Yes! You win!'
