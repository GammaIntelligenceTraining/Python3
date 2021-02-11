condition = True
while condition:

    user_choice = input('Please choose:\n1. Check id code\n0. Exit\n--> ')
    # IF statement for user to choose option
    if user_choice == '1':

        condition2 = True
        while condition2:
            user_id = input('Please enter your national id: ')
            try:
                user_id = str(int(user_id))
                # Check if ID code length is 11 symbols
                if len(user_id) != 11:
                    if len(user_id) > 11:
                        print('ID code is too long')
                    elif len(user_id) < 11:
                        print('ID code is too short')
                    raise UserWarning
                else:
                    condition2 = False
            except:
                print('ERROR')
            else:
                # Create variables for parts of ID code
                gender_id = user_id[0]
                birth_year = user_id[1:3]
                birth_month = user_id[3:5]
                birth_day = user_id[5:7]
                birth_region = int(user_id[7:10])
                check_num = user_id[10]

                # IF statement to check gender and century of birth
                if gender_id == '1':
                    gender = 'Male'
                    birth_cent = '18'
                elif gender_id == '2':
                    gender = 'Female'
                    birth_cent = '18'
                elif gender_id == '3':
                    gender = 'Male'
                    birth_cent = '19'
                elif gender_id == '4':
                    gender = 'Female'
                    birth_cent = '19'
                elif gender_id == '5':
                    gender = 'Male'
                    birth_cent = '20'
                elif gender_id == '6':
                    gender = 'Female'
                    birth_cent = '20'
                else:
                    gender = 'unknown'
                    birth_cent = 'unknown'

                if birth_region in range(1, 11):
                    region = 'Kuressaare haigla'
                elif birth_region in range(11, 20):
                    region = 'Tartu Ülikooli Naistekliinik'
                elif birth_region in range(21, 151):
                    region = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
                else:
                    region = 'unknown'

                print('Your national id is: ' + user_id)
                print('You are ' + gender)
                print('Your date of birth is: ' + birth_day + '.' + birth_month + '.' + birth_cent + birth_year)
                print('You were born in ' + region)



    elif user_choice == '0':
        quit('Program has quit working')
    else:
        print('Choice out of range!')


