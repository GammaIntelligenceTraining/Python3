import os
import datetime


def user_menu():
    user_choice = input('Please choose:\n1.Sort files and update logs\n0.Exit\n')
    if user_choice == '1':

        # os.replace('needs_sorting/toast.png', 'toast.png')
        if os.path.exists('images') == False:
            os.mkdir('images')
        if os.path.exists('text_files') == False:
            os.makedirs('text_files')
        for file in os.listdir('needs_sorting'):
            # print(os.stat(f'needs_sorting\\{x}'))
            if os.path.splitext(file)[1] == '.jpg' or os.path.splitext(file)[1] == '.png':
                os.replace(f'needs_sorting\\{file}', f'images\\{file}')
            elif os.path.splitext(file)[1] == '.txt':
                os.replace(f'needs_sorting\\{file}', f'text_files\\{file}')
            else:
                print('error')
            # get_file_data([os.stat(f'needs_sorting\\{x}'), x])
        create_log_files()
        print('\nFinished sorting\n')
        user_menu()
    elif user_choice == '0':
        print('Good bye')
        exit()


def create_log_files():
    images_log = ''
    for image_file in os.listdir('images'):
        if image_file == 'images_log.txt':
            continue
        images_log += 'Filename: ' + image_file + '\nFile size: ' +\
                      str(os.stat(f'images\\{image_file}').st_size // 1000) + 'kb\n' + \
                      'Created: ' + str(datetime.datetime.fromtimestamp(os.stat(f'images\\{image_file}').st_ctime)) + \
                      '\n\n'

    with open('images\\images_log.txt', 'w', encoding='utf') as img_log_file:
        img_log_file.write(images_log)

    text_log = ''
    for text_file in os.listdir('text_files'):
        if text_file == 'text_files_log.txt':
            continue
        text_log += 'Filename: ' + text_file + '\nFile size: ' +\
                    str(os.stat(f'text_files\\{text_file}').st_size) + 'b\n' + 'Created: ' +\
                    str(datetime.datetime.fromtimestamp(os.stat(f'text_files\\{text_file}').st_ctime)) + \
                    '\n\n'
    with open('text_files\\text_files_log.txt', 'w', encoding='utf8') as txt_log:
        txt_log.write(text_log)
user_menu()
