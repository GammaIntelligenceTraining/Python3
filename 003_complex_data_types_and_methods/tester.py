numbers = range(1, 100)
for num in numbers:
    if num % 5 == 0 and num % 3 == 0:
        print(num, 'FizzBuzz')
    elif num % 5 == 0:
        print(num, 'Fizz')
    elif num % 3 == 0:
        print(num, 'Buzz')