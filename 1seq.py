length = int(input('Введите длину списка:'))
user_list = []
for i in range(length):
    user_input = int(input(f'Введите {i} элемент списка:'))
    user_list.append(user_input)
user_list.sort()
print(f'Введённый список: {user_list}')