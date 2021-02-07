empty_string = ''
string_sample = "Hello world world"
string_sample2 = "first letteR is lowErcase"
string_sample3 = " extra whitespace string "
german_sample = "der Fluß"

print(string_sample)  # Will return string
print(string_sample[0])  # Will return first letter of string
print(string_sample[6])  # Will return 6th index of string
print(string_sample[-1])  # Will return last letter of string
print(string_sample[0:5])  # Will return letters from index 0 to index 4 included
print(string_sample[:5])  # Will return letters from beginning to index 4 included
print(string_sample[5:])  # Will return letters from index 5 to the end
print(string_sample[::-1])  # Will return all letters in backwards order

print(len(string_sample))  # Will return length of string

print("world" in string_sample)  # Will return True if given argument is part of the string, or False if not. (not in is opposite)

print(string_sample.upper())  # Will convert string to uppercase

print(string_sample.lower())  # Will convert string to lowercase

print(german_sample.lower())
print(german_sample.casefold())  # Will return lowercase string

print(string_sample2.capitalize())  # Will return string with first letter in uppercase

print(string_sample3.strip())  # Will remove extra whitespaces (begining and end of string)

print(string_sample.replace('world', 'people'))  # Will replace one part of the string with other

print(string_sample.split(' '))  # Converts to list with specified delimiter

print(string_sample.count('o'))  # Will return number of times specified value occurs in string as (INT)

print(string_sample.find('world'))  # Will return index of specified value (first time occurs)

