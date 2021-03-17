import re

# Sample string
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa HaHaH
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
abc

ball mall hall wall tall
'''
sentence = 'Start a sentence and then bring it to an end bring'

pattern = re.compile(r'n$', re.M)
# matches = pattern.search(text_to_search)
# print(matches)

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)