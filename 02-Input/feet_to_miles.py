# How many feet are there? 6000
# There are 1 miles with 720 feet left over.

feet = int(input('How many feet are there? '))

# print(f'You entered: {feet}')

miles = feet // 5280
leftover_feet = feet % 5280

# print(miles)
# print(leftover_feet)

print(f'There are {miles} miles with {leftover_feet} feet left over.')