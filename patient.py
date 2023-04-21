class Patient:
    def __init__(self, pid, name, disease, gender, age):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age
    
    def get_pid(self):
        return self.pid
    
    def get_name(self):
        return self.name
    
    def get_disease(self):
        return self.disease
    
    def get_gender(self):
        return self.gender
    
    def get_age(self):
        return self.age
    
    def set_pid(self, new_pid):
        if new_pid.isdigit():
            self.__pid = new_pid
            
    def set_name(self, new_name):
        if not new_name.isdigit():
            self.__name = new_name
        
    def set_disease(self, new_disease):
        if not new_disease.isdigit():
            self.__disease = new_disease
    
    def set_gender(self, new_gender):
        if not new_gender.isdigit():
            self.__gender = new_gender
            
    def set_age(self, new_age):
        if new_age.isdigit():
            self.__age = new_age
    
    def __str__(self):
        return self.pid +'_' +self.name +'_' +self.disease +'_'  +self.gender +'_' +self.age +''
########
# This section is just to test the output
patientlist = [Patient("2042", "Jack", "Ligma", "Male", "17")]

for Patient in patientlist:
    print (Patient)
        