import requests

# First install requests module
# pip install requests

# Documentation
# https://requests.readthedocs.io/en/master/

# Requests.get will get a html code from webpage and return status of a website
r = requests.get('https://xkcd.com/353/', timeout=3)
# print(r)
# print(dir(r))

# Headers are required for some websites that have a no browser access protection
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
r = requests.get('https://xkcd.com/353/', headers=headers)
# # .text will return HTML code from a webpage
# print(r.text)
# print(r.content)

# # Image can be download with python requests module
# image = requests.get('https://imgs.xkcd.com/comics/python.png')
# with open('comic.png', 'wb') as f:
#     f.write(image.content)

print(r.status_code)
# 200 - success
# 300 - redirect
# 400 - client errors
# 500 - server errors

# .ok will return true if status code is less than 400
print(r.ok)

# Will return all headers from the webpage
print(r.headers)

