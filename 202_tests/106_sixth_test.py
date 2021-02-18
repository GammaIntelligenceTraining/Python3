test_list1 = [1, 2, 3, 4, 4, 5, 5, 5, 7, 8, 8, 8, 10, 10, 10]
max_count = 0
new_list = []

# print(test_list1.count(1))

for num in test_list1:
    if test_list1.count(num) > max_count:
        max_count = test_list1.count(num)


for num in test_list1:
    if test_list1.count(num) == max_count:
        new_list.append(num)
new_list = list(set(new_list))

print(new_list)