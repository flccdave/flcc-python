import os


list_of_files = os.listdir()
list_of_files.sort()
# print(list_of_files)

list_of_viable_files = []

# temp_file_name = list_of_files[2]
# print(temp_file_name)
# print('.txt' in temp_file_name)

for file_name in list_of_files:
    if '.txt' in file_name:
        list_of_viable_files.append(file_name)

print(list_of_viable_files)

print('Choose from the following files:')

for i, file_name in enumerate(list_of_viable_files):
    print(f'  {i+1} - {file_name}')

print()
choice = int(input('Which file number? '))
choice = choice - 1 # Subtract one because we added one above

file_name = list_of_viable_files[choice]
# print(file_name)



file = open(file_name, 'a')
proof = input('What is your hacker signature? ')
file.write(f'\n\n{proof} was here')




