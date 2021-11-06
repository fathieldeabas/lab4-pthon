import re
class Person :
    def __init__(self ,name,money=1000):
        self.name=name
        self.money=money
    def sleep(self,hours):
        if hours == 7:
            self.mood="happy"
        elif hours < 7 :
            self.mood="tired"
        else:
            self.mood="lazy"
        
    def eat(self, meals):
        
        if meals == 3:
            self.healthRate="100%"
        elif meals == 2:
            self.healthRate="75%"
        else :
            self.healthRate="50"

    def buy(self):
        self.money=self.money-10


class Employee(Person):
    def __init__(self,name,money,id ,car ,email,salary,distancetowork):
        super().__init__(name,money)
        self.id=id
        self.car=car
        self.email=email
        self.salary=salary
        self.distancetowork=distancetowork
        @property
        def salary(self):
            return self.__salary
        @salary.setter
        def salary(self, salary):
                if salary < 1000:
                    self.__salary= 1000
        @property
        def healthRate(self):
            return self.healthRate
        @property
        def mood(self):
            return self.mood
    
        

    def work(self,hours):
        if hours == 7:
            self.mood="happy"
        elif hours < 7 :
            self.mood="tired"
        else:
            self.mood="lazy"
    def drive(self):
        print(self.name)
    def reful(self):
        print(self.name)
    def send_email(self):
        reg = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        to=input("to" )
        while not  re.match(reg,to) :
            to=input("to" )
        subject=input("subject" )
        while subject.isspace() or subject=="":
            subject=input("not invaild try again" )
            print(subject.isspace())
        msg=input("msg" )
        print(msg.isspace())
        while msg.isspace() or msg=="":
            msg=input("not invaild" )
        reciver_name=input("reciver_name" )
        while reciver_name.isspace() or reciver_name=="":
            reciver_name  =input("reciver_name" )
        all=[to,subject,msg,reciver_name]
        fulldata=":".join(all)
        try:
            em=open("email.txt","w")
        except :
            print("except error")
        else:
            em.write(f"{fulldata}")
        finally:
            em.close()



class Office:
    def __init__(self,name,employee):
        self.employee=employee
        self.name = name
    def get_all_employee(self):
        print("get all employee")
    def get_employee(self):
        print("get employee")
    def hire(self):
        print("hire")
    def calculate_lateness(self):
        print("calculate lateness")
    def deduct(self):
        print("duct")
    def reward(self):
        print("reward")
    class car:
        def __init__(self,name,fulerate,velocity):
            self.name = name
            self.fulerate=fulerate
            self.velocity=velocity
        def run(self):
            print(self.name)
        def stop(self):
            print(self.name)
e=Employee("fathi",1000,1,"fat","hiuohpio",4500,55)
e.eat(2)
print(e.healthRate)
e.sleep(8)
print(e.mood)
e.send_email()