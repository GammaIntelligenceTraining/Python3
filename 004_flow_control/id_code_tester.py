id_code = input('Please enter your ID code: ')
# 1 2 3 4 5 6 7 8 9 1
# 3 4 5 6 7 8 9 1 2 3

chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
id_code_list = list(id_code)

counter = 0
result = 0
for num in chk1:
    result = result + chk1[counter] * int(id_code_list[counter])
    counter += 1
check_num = result % 11

if check_num == int(id_code[-1]):
    print('ID code is valid')
elif check_num == 10:
    counter = 0
    result = 0
    for num in chk2:
        result = result + chk2[counter] * int(id_code_list[counter])
        counter += 1
    check_num = result % 11
    if check_num == int(id_code[-1]):
        print('Code is valid')
    elif check_num >= 10:
        check_num = 0
    else:
        print('Code is not valid')
else:
    print('Code is not valid!!!!!!!')