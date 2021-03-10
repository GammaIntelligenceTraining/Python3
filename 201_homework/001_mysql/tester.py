import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='12345678',
    database='homework'
)

def get_hospital_detail(hospital_id):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM hospital WHERE Hospital_id LIKE " + str(hospital_id))
    result = mycursor.fetchall()
    print("Printing hospital record")
    print('Hospital id:', result[0][0])
    print('Hospital name:', result[0][1])
    print('Bed count:', result[0][2], '\n')

def get_doctor_detail(doctor_id):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM doctor WHERE Doctor_Id LIKE " + str(doctor_id))
    print('Printing Doctor record')
    result = mycursor.fetchall()
    print('Doctor ID', result[0][0])
    print('Doctor name:', result[0][1])
    print('Hospital ID:', result[0][2])
    print('Joining Date:', result[0][3])
    print('Specialty:', result[0][4])
    print('Salary:', result[0][5])
    print('Experience', result[0][6], '\n')

def user_menu():
    choice = input('Please choose:\n1. Get hospital detail\n2. Get doctor detail\n3. Exit\n-->')
    if choice == '1':
        hospital_id = input('Please enter hospital id\n-->')
        try:
            get_hospital_detail(hospital_id)
        except:
            print('Hospital ID not listed\n')
            user_menu()
        else:
            user_menu()
    elif choice == '2':
        doctor_id = input('Please enter doctor id\n-->')
        try:
            get_doctor_detail(doctor_id)
        except:
            print('Doctor ID is not listed\n')
            user_menu()
        else:
            user_menu()
    elif choice == '3':
        exit()
    else:
        print('Choice is out of range')
        user_menu()

user_menu()