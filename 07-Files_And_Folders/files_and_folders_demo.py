file_name = 'names.txt'
# file_name = input('Enter file name: ')

file = open(file_name, 'r')
# print(file.read())




# name = file.readline()
# print(name)

# name = file.readline()
# print(name)


names = file.readlines()
# print(names)

file.close()

file = open(file_name, 'w')

# names[10] = 'Kara\n'
names[0] = names[0].upper()

file.writelines(names)
file.close()

# for name in names:
#     temp_name = name[0:len(name)-1]
#     print(temp_name.upper())


# file.write('\nXenia')












file.close()