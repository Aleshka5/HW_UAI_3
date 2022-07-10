def str_to_list(input_str):
    if ',' in input_str and '/' in input_str:
        print('Введены некорректные данные!')
    elif ',' in input_str:
        user_list = input_str.split(',')
    elif '/' in input_str:
        user_list = input_str.split('/')
    else:
        user_list = input_str.split(' ')
    user_list = [int(elem) for elem in user_list]

    return user_list

user_str1 = input(f'Введите элементы первого списка через разделитель (, /):')
user_str2 = input(f'Введите элементы второго списка через разделитель (, /):')

user_list1 = str_to_list(user_str1)
user_list2 = str_to_list(user_str2)

print(f'Введённый список 1: {user_list1}')
print(f'Введённый список 2: {user_list2}')

diff_nums = []
for number in user_list1:
    if number not in user_list2:
        diff_nums.append(number)
print(f'Элементы первого списка, которых нет во втором: {diff_nums}')
