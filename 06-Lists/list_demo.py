# INSERTING AND REMOVING FROM A LIST

grocery_list = ['Apples', 'Bananas', 'Coconut', 'Durian', 'Eggplant', 'Bananas']
print(grocery_list)

print()

grocery_list.append('Boo Berry Crunch')
# grocery_list.sort()
print(grocery_list)

print()

grocery_list.insert(0, 'Coffee')
print(grocery_list)

# while 'Bananas' in grocery_list:
#     grocery_list.remove('Bananas')

print(grocery_list)

print(grocery_list.count('Bananas'))

pared_down_list = set(grocery_list)
print(pared_down_list)

# print('Bananas' in grocery_list) # TRUE or FALSE























# list_of_grades = [90, 100, 21, 96, 88]
# print(list_of_grades)

# list_of_grades.append(79)
# print(list_of_grades)

# # list_of_grades.sort()
# # print(list_of_grades)

# print(f'The second grade is {list_of_grades[1]}');

# #                       [90,       100,     21,        96,       88,      79]

# # list_of_student_names = ['Annie', 'Brett', 'Charlie', 'Damien', 'Erlich', 'Francios']
# # print(list_of_student_names[4])

# for grade in list_of_grades:
#     print(f'Grade: {grade}')