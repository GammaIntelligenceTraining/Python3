entry = 'Never odd or even'

if entry.lower().replace(' ', '') == entry.lower().replace(' ', '')[::-1]:
    print('It is a palendrome')
else:
    print('It is not a palendrome')

# entry = input('Please enter palendrome to check: ')
# entry = entry.lower().replace(' ', '').replace(',', '')
# print(entry)
# if entry[::-1] == entry:
#     print("OK")
# else:
#     print("NOK")