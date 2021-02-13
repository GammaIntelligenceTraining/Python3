def id_check(id_code, chk_list):
    counter = 0
    result = 0
    for num in chk_list:
        result += int(id_code[counter]) * num
        counter += 1
    return result % 11

id_code = list(input('Please enter your id: '))

chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

if id_check(id_code, chk1) == 10:
    result = id_check(id_code, chk2)
    if result == int(id_code[10]):
        print('ID code is valid')
    else:
        print('ID code is invalid')
elif id_check(id_code, chk1) == int(id_code[10]):
    print('ID code is valid')



print(id_check(id_code, chk1))