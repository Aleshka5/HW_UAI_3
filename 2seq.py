user_list = input(f'Введите элементы списка через разделитель (, ; /):')
if ',' in user_list and ';' in user_list and '/' in user_list:
    print('Введены некорректные данные!')
elif ',' in user_list:
    user_list = user_list.split(',')
elif ';' in user_list:
    user_list = user_list.split(';')
elif '/' in user_list:
    user_list = user_list.split('/')
else:
    user_list = user_list.split(' ')

user_list = [int(elem) for elem in user_list]
print(f'Введённый список: {user_list}')

set_of_uniques_elements = set(user_list)
list_of_uniques_elements = []

for number in set_of_uniques_elements:
    if user_list.count(number) == 1:
        list_of_uniques_elements.append(number)

print(f'Все уникальные элементы списка: {list_of_uniques_elements}')
