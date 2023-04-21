class Doctor:

    def __init__(self, doctor_id, name, special, working_time, qualification, room_number):
        self.doctor_id = doctor_id
        self.name = name
        self.special = special
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def get_doctor_id(self):
        return self.doctor_id

    def get_name(self):
        return self.name

    def get_special(self):
        return self.special

    def get_working_time(self):
        return self.working_time

    def get_qualification(self):
        return self.qualification

    def get_room_number(self):
        return self.room_number

    def set_doctor_id(self, new_id):
        if new_id.isdigit():
            self.__doctor_id = new_id

    def set_name(self,new_name):
        if not new_name.isdigit():
            self.__name = new_name
        
    def set_special(self, new_special):
        if not new_special.isdigit():
            self.__special = new_special
                
    def set_working_time(self, new_time):
        if new_time.isdigit():
            self.__working_time = new_time
        
    def set_qualification(self, new_qualification):
        if not new_qualification.isdigit():
            self.__qualification = new_qualificataion
        
    def set_room_number(self, new_room_number):
        if new_room_number.isdigit():
            self.__room_number = new_room_number
                
    def __str__(self):
        return  self.doctor_id + "_" +self.name + "_" +self.special +'_'  +self.working_time +'_'   +self.qualification +'_' +self.room_number +''
########################
# This section is just to test the output
doctor1 = Doctor("2034", "Jack", "Medicine", "0600 to 1200", "Doctor", "1024")

doctorlist = [Doctor("2035", "Dr.Sam", "Medicine", "0400-2400", "Doctor", "1025")]
for Doctor in doctorlist:
    print(Doctor)
