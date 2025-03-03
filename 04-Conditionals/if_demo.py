print('start')

age = int(input('What is your age? '))

# if age > 45:
# if age > 45 and age < 100:

if 45 < age < 100:
    print('----------------------')
    print('Congrats on being old.')
    print('----------------------')

elif age >= 100:
    print('Dang! You\'re REAL old')

elif age < 45:
    print('Dang! You\'re young!')

else:
    print('You are the perfect age!')

print('end')