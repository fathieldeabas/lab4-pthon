from modul import update
from modul import delete
from modul import view
from modul import viewproject
from modul import project



def login():
    print("plz enter your email")
    email=input()
    print("plz enter your password")
    password=input()
    try:
        data=open("userdata.txt")
    except :
        print("cant read the file")
    else:
        check=""
        for line in data:
            userdata=line.split(":")
            if userdata[2] == email and  userdata[4] == password+"\n":
                print("loging is successfully")
                print("choose your option (create -view_projects-view_project-delete_project-update)")
                while True:
                    choice=input()
                    choice=choice.strip()
                    if choice == "create":
                        project()
                        break
                    elif choice == "view_projects" :
                        view()
                        break
                    elif choice == "view_project" :
                        viewproject()
                        break
                    elif choice == "delete_project" :
                        delete()
                        break
                    elif choice == "update":
                        update()
                        break
                    else:
                        print("not in choice")
                        break
                break
            else:
                check= False
                if check ==False:
                    print("your not in system you can register")        
                
    
def Registration():
    print("plz enter your first_name ")
    first_name=input()
    while not first_name.isalpha() or  first_name.isspace():
        print("plz try to enter vaild name")
        first_name = input()
    else:
        print(f"your first name  is {first_name}")
        ########################
    print("plz enter your last name ")
    last_name = input()
    while not last_name.isalpha() or last_name.isspace():
        print("plz try to enter vaild name")
        last_name = input()
    else:
        print(f"your last name  is {last_name}")
    #########################################
    print("plz enter your email ")
    email = input()
    while " "in email or  email.isspace():
        print("plz try to enter vaild email")
        email = input()
    else:
        print(f"your mail  is {email}")
    ######################################
    print("plz enter your password ")
    password = input()
    while " " in password or  password.isspace():
        print("plz try to enter vaild password")
        password = input()
    else:
        print(f"your password  is {password}")
        ##################################
        print(" confirm the password")
        confirm_password=input()
    while password != confirm_password:
        print(" confirm the password")
        confirm_password=input()

    print("plz enter your phone ")
    phone = input()
    
    while " " in phone or not phone.isdigit() or phone.isspace():
        print("plz try to enter vaild phone ")
        phone= input()
    else:
        print(f"your phone  is {phone}")
    full_data=":".join([first_name,last_name,email,phone,password])
    try:
        data=open("userdata.txt",'a')
    except :
        print("except error")
    else:
        data.write(f"{full_data}\n")
    finally:
        data.close()

while True :
    print("plz select from choice ( login or Registration:)")
    choice=input(": ")
    if choice == "login":
        print("login")
        login()
        break
    elif choice == "Registration" :
        Registration()
        break
    else:
        print("your choice is wrong")
