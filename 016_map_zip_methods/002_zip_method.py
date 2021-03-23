# zip() function combines two iterables and pairs values together
# Be careful zip() ends on the shortest iterable
data1 = [100, 200, 300, 400, 500, 600, 700, 800, 900]
data2 = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
combination = zip(data1, data2)

for x in combination:
    print(x)

print(list(combination))

# zip_longest() method will create pairs until longest iterable has items
data = [100, 200, 300, 400]
daily_data = list(zip(data, range(10)))
print(daily_data)

for (a, b) in zip(data1, data2):
    print(a)
    print(b)