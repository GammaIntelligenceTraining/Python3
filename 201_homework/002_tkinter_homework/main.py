from tkinter import *

window = Tk()

window.title('ID code validator')
window.geometry('600x200')
window.configure(bg='#FFFFFF')

def check_id():
    id_code = id_entry.get()
    try:
        int(id_code)
        if len(id_code) != 11:
            raise UserWarning
    except UserWarning:
        if len(id_code) < 11:
            print_result.set('Code is too short')
        elif len(id_code) > 11:
            print_result.set('Code is too long')
    except:
        print_result.set('Code you entered is not numeric')
    else:
        result_str = ''
        if var.get() == 1:
            result_str = get_data_by_id(id_code) + id_validator(id_code)
        elif var.get() == 0:
            result_str = get_data_by_id(id_code)

        print_result.set(result_str)


def id_validator(idcode):
    # Check numbers
    chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

    # For loop to check first row of numbers
    chk_result = 0
    for x in range(0, 10):
        chk_result += int(idcode[x]) * chk1[x]

    # For loop to check second row of numbers if first try failed
    if chk_result % 11 != int(idcode[-1]) and chk_result % 11 == 10:
        chk_result = 0
        for x in range(0, 10):
            chk_result += int(idcode[x]) * chk2[x]

    # Print validation result
    if chk_result % 11 == int(idcode[-1]):
        return '\nYour ID is valid'
    else:
        return '\nYour ID is NOT valid'


def get_data_by_id(idcode):

    # Create variables for each type of data from ID
    gender_num = idcode[0]
    by_num = idcode[1:3]
    bm_num = idcode[3:5]
    bd_num = idcode[5:7]
    birth_region = idcode[7:10]
    chk_num = idcode[10]

    # Get gender and birth century
    if gender_num == '1':
        cent_id = '18'
        gend_id = 'Male'
    elif gender_num == '2':
        cent_id = '18'
        gend_id = 'Female'
    elif gender_num == '3':
        cent_id = '19'
        gend_id = 'Male'
    elif gender_num == '4':
        cent_id = '19'
        gend_id = 'Female'
    elif gender_num == '5':
        cent_id = '20'
        gend_id = 'Male'
    elif gender_num == '6':
        cent_id = '20'
        gend_id = 'Female'

    # IF statement to check region of birth
    if int(birth_region) in range(1, 11):
        region = 'Kuressaare haigla'
    elif int(birth_region) in range(11, 20):
        region = 'Tartu Ülikooli Naistekliinik'
    elif int(birth_region) in range(21, 151):
        region = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
    elif int(birth_region) in range(151, 161):
        region = 'Keila haigla'
    elif int(birth_region) in range(161, 221):
        region = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
    elif int(birth_region) in range(221, 271):
        region = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
    elif int(birth_region) in range(271, 371):
        region = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
    elif int(birth_region) in range(371, 421):
        region = 'Narva haigla'
    elif int(birth_region) in range(421, 471):
        region = 'Pärnu haigla'
    elif int(birth_region) in range(471, 491):
        region = 'Haapsalu haigla'
    elif int(birth_region) in range(491, 521):
        region = 'Järvamaa haigla (Paide)'
    elif int(birth_region) in range(521, 571):
        region = 'Rakvere haigla, Tapa haigla'
    elif int(birth_region) in range(571, 601):
        region = 'Valga haigla'
    elif int(birth_region) in range(601, 651):
        region = 'Viljandi haigla'
    elif int(birth_region) in range(651, 701):
        region = 'Lõuna-Eesti haigla (Võru), Põlva haigla'
    else:
        region = 'Unknown'


    result_str = 'ID: ' + idcode + '\nGender: ' + gend_id + '\nDate of birth: ' +\
                 bd_num + '.' + bm_num + '.' + cent_id + by_num + \
                 '\nRegion: ' + region + '\nID check number: ' + chk_num
    return result_str


isikukood_img = PhotoImage(file='isikukood.png')
img_label = Label(window, image=isikukood_img)
img_label.grid(row=0, column=0, rowspan=4)

id_entry_label = Label(window, text='Enter ID:', bg='#FFFFFF')
id_entry_label.grid(row=0, column=1)
id_entry = Entry(window, width=35)
id_entry.grid(row=0, column=2)

var = IntVar()
id_validation = Checkbutton(window, text='Validate my ID', variable=var, bg='#FFFFFF')
id_validation.deselect()
id_validation.grid(row=1, column=2)
condition = var.get()


id_button = Button(window, text="Get data by ID", command=check_id)
id_button.grid(row=0, column=3)

print_result = StringVar()


output_label = Label(window, textvariable=print_result, bg='#FFFFFF')
output_label.grid(row=2, column=1, columnspan=3)


window.mainloop()
