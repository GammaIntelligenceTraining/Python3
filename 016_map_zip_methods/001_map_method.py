# map() method is used to iter through functions
def func(x):
    return x ** x

int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Long way
new_list = []
for x in int_list:
    new_list.append(func(x))

print(new_list)

# Using map()
print(map(func, int_list))
print(list(map(func, int_list)))


# List comprehension
print([func(x) for x in int_list])
print([func(x) for x in int_list if x % 2 == 0])



