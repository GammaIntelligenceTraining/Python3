while True:
    user_input = input('Please choose:\n1:Print\n0:Exit')
    if user_input == '1':
        print('All is good')
        continue
    elif user_input == '0':
        break
    else:
        pass
print('You have exited while loop.')
exit()