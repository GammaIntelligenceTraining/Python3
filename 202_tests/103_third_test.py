side_a, side_b, side_c = input('Please enter three sides of triangle separated by coma: ').split(', ')

if float(side_c) ** 2 == float(side_a) ** 2 + float(side_b) ** 2:
    print('Triangle is RIGHT')
else:
    print('Triangle is NOT RIGHT')
