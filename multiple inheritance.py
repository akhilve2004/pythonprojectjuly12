#MULTIPLE INHERITANCE

class Hospital:
    def __init__(self):
        self.hos_name=input("Enter Hospital name")
        self.location=input("Enter location")
        self.phone=int(input("Enter Phone"))
    def display_hospital(self):
        print("Hospital Name",self.hos_name,"Phone",self.phone,"Location",self.loaction)
class Department:
    def __init__(self):
        self.department_name=input("Enter department name")
        self.doctor_name=input("Enter doctor name")
    def display_department(self):
        print("Department name",self.department_name,"Doctor name",self.doctor_name)





class Patient(Hospital , Department):
    def __init__(self):
        Hospital.__init__(self)
        Department.__init__(self)
        # patient properties

    def full_summary(self):
        Hospital.display(self)
        department.__init(self)
        self.patient_name=input("enter Patient name")
        self.age=int(input("enter age"))
        #patient details

    def set_discharge(self):
        self.discharge_date=input("Enter discharge date")

p=Patient()
p.full_summary()
p.set_discharge()
p.full_summary()