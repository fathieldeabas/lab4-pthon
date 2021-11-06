import datetime
def  update():
    print("enter the  title  for project")
    title=input()
    print("choose the filed which you want to up date:(title-details-fund)")
    filed=input()
    if filed == "title":
        i=0
    elif filed == "details":
        i=1
    elif filed== "fund":
        i=2
    else:
        print("your choice cant update")
    print("enter the new value")
    newvalue=input()
    if i==1 or i==2:
        while not newvalue.isalpha():
            print("invaild value enter new value ")
            newvalue=input()
    else:
        while not newvalue.isdigit():
            print("invaild value enter new value ")
            newvalue=input()

    try:
        data=open("project.txt","r")
    except :
        print("except error")
    else:
        lines = data.readlines()
        for line in lines:
            pro=line.split(":")
            if pro[0] == title:
                updateline=line

    finally:
        data.close()
    try:
        data=open("project.txt","w")
    except :
        print("except error")
    else:
        for line in lines:
            if line == updateline:
                pro=line.split(":")
                pro[i]=newvalue
                line=":".join(pro)
                data.write(f"{line}")
            else:
                data.write(f"{line}")


    finally:
        data.close()
    

def  delete():
    print("enter the  title  for project")
    title=input()
    try:
        data=open("project.txt",'r')
    except :
        print("except error")
    else:
        lines = data.readlines()
        for line in lines:
            pro=line.split(":")
            if pro[0] == title:
                del_line=line

    finally:
        data.close()
    try:
        data=open("project.txt",'w')
    except:
        print("except error")
    else:
        for linee in lines:
            print(linee)
            if del_line ==linee:
                continue
            else:  
                data.write(linee)

    finally:
        data.close()
def view():
    try:
        data=open("project.txt")
    except :
        print("except error")
    else:
        for line in data:
            print(line)
    finally:
        data.close()
def viewproject():
    print("enter the name of the project")
    searchitem=input()
    try:
        data=open("project.txt")
    except :
        print("except error")
    else:
        check=""
        for line in data:
            project_data=line.split(":")
            if project_data[0]== searchitem:
                print(line)
                check=True
            else:
                check=False
        if check ==False:
            print("not found")
    finally:
        data.close()


def project():
    print("plz enter  the title of project")
    title=input()
    while not title.isalpha():
        print("plz enter  the title of project")
        title=input()
    else:
        title=title
    print("plz enter  the details of project")
    details=input()
    while details.isspace():
        print("plz enter  the details of project")
        details=input()
    else:
        details=details
    print("plz enter  the fund of project")
    fund=input()
    while not fund.isdigit():
        print("plz enter  the fund of project")
        fund=input()
    else:
        fund=fund
    start_date=datetime.date.today()
    print(f"your start date is {start_date}")
    margin = datetime.timedelta(days = 30)
    end_date=datetime.date.today()+margin
    print(f"the end date {end_date}")
    fulldata=":".join([title,details,fund, str(start_date),str(end_date)])
    try:
        data=open("project.txt",'a')
    except :
        print("except error")
    else:
        data.write(f"{fulldata}\n")
    finally:
        data.close()
