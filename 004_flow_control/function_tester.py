def print_message(worker):
    message = 'Hello ' + worker[0] + ' ' + worker[1] + '. You are ' + worker[2] + ' years old.\n' \
           'Your salary is ' + str(worker[3]) + 'EUR. You are on ' + worker[4] + ' position'
    return message

worker_data = ['John', 'Smith', '37', 2000, 'Manager']

print(print_message(worker_data))