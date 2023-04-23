from doctor import Doctor


class DoctorManager:
    def __init__(self):
        self.__doctors_list = [] #Empty list of doctors
        DoctorManager.read_doctors_file(self) #Reads the doctor data from the doctor.txt file


    def format_dr_info(self, new_doctor):
        return Doctor.__str__(new_doctor) #Formats the information as the __str__ method called from the Doctor class


    def enter_dr_info(self): #User is asked for the doctor's information
        dr_id = str(input("Enter the doctor’s ID: "))
        dr_name = str(input("Enter the doctor’s name: "))
        dr_speciality = str(input("Enter the doctor’s speciality: "))
        dr_timing = str(input("Enter the doctor’s timing (e.g., 7am-10pm): "))
        dr_qualification = str(input("Enter the doctor’s qualification: "))
        dr_roomnum = str(input("Enter the doctor’s room number: "))
        doctor = Doctor(dr_id, dr_name, dr_speciality, dr_timing, dr_qualification, dr_roomnum)
        return doctor #Doctor object is returned


    def read_doctors_file(self):
        data = open('doctors.txt', 'r')
        next(data) #This skips the first line in the doctors.txt file as it contains the information headings
        for doctor in data: #Loop is created to go through each doctor in the doctors.txt file
            data = doctor.strip().split("_") #Ensures each line and words in the doctors.txt file are separated
            new_doctor = Doctor(data[0], data[1], data[2], data[3], data[4], data[5])
            self.__doctors_list.append(new_doctor)


    def search_doctor_by_id(self):
        doctor_id = input("Enter the doctor Id: ")
        counter = 0
        for doctor in self.__doctors_list: #Loop that goes through each doctor on the self.__doctors_list list (of doctors)
            counter += 1 #Adds one each time it goes through one doctor.
            id, name, speciality, timing, qualification, room_number = [str(data) for data in str(doctor).split("_")]
            if doctor_id == id:
                print(f'\n{"ID":<5s}{"Name":<23s}{"Speciality":<16s}{"Timing":<16s}{"Qualification":<16s}{"Room Number"}\n') #Formats the information headings with their respected spacing
                print(f'{id:<5s}{name:<23s}{speciality:<16s}{timing:<16s}{qualification:<16s}{room_number}') #Formats the doctor information with their respected spacing
                break #This will break the loop if the ID exists
            elif counter == len(self.__doctors_list): #Message occurs if the counter has gone through each doctor and the ID has not been found
                print("Can't find the doctor with the same ID on the system")


    def search_doctor_by_name(self):
        doctor_name = input("Enter the doctor name: ")
        counter = 0
        for doctor in self.__doctors_list: #Loop that goes through each doctor on the self.__doctors_list list (of doctors)
            counter += 1 #Adds one each time it goes through one doctor.
            id, name, speciality, timing, qualification, room_number = [str(data) for data in str(doctor).split("_")]
            if doctor_name == name:
                print(f'\n{"ID":<5s}{"Name":<23s}{"Speciality":<16s}{"Timing":<16s}{"Qualification":<16s}{"Room Number"}\n') #Formats the information headings with their respected spacing
                print(f'{id:<5s}{name:<23s}{speciality:<16s}{timing:<16s}{qualification:<16s}{room_number}') #Proper formatting with their respected spacing according to the output file
                break #This will break the loop if the name exists
            elif counter == len(self.__doctors_list): #Message occurs if the counter has gone through each doctor and the name has not been found
                print("Can't find the doctor with the same name on the system")


    def display_doctor_info(self, doctor):
        if doctor in self.__doctors_list: #Displays the doctor information
            print(doctor)


    def edit_doctor_info(self):
        id = input("Please enter the id of the doctor that you want to edit their information: ")
        for doctor in self.__doctors_list: #This is a loop that will go through each doctor
            doctor_id = str(doctor).split("_")[0]
            if id == doctor_id: #This will go through each doctor_id value and see if it exists
                new_name = str(input("Enter new Name: "))
                new_speciality = str(input("Enter new Specialist in: "))
                new_timing = str(input("Enter new Timing: "))
                new_qualification = str(input("Enter new Qualification: "))
                new_room_number = str(input("Enter new Room number: "))
                updated_doctor = Doctor(doctor_id, new_name, new_speciality, new_timing, new_qualification, new_room_number) #Groups all new information as one
                self.__doctors_list[self.__doctors_list.index(doctor)] = updated_doctor #This ensures the correct doctor information in the doctors.txt file is the only one to be changed
                self.write_list_of_doctors_to_file(self.__doctors_list) #Calls write_list_of_doctors_to_file for the doctors.txt file to be updated
                print("Doctor whose ID is", doctor_id, "has been edited")
                break

        else:
            print("Cannot find the doctor...")


    def display_doctors_list(self):
        print(f'\n{"Id":<5s}{"Name":<23s}{"Speciality":<16s}{"Timing":<16s}{"Qualification":<16s}{"Room Number"}\n') #Formats the headings

        for doctor in self.__doctors_list:
            id, name, speciality, timing, qualification, room_number = [str(data) for data in str(doctor).split("_")] #Formats the information with the respected spaces
            print(f'{id:<5s}{name:<23s}{speciality:<16s}{timing:<16s}{qualification:<16s}{room_number}\n')


    def write_list_of_doctors_to_file(self, doctors):
        doctors_file = open('doctors.txt', 'w')
        self.__doctors_list = doctors
        doctors_file.write("id_name_specialist_timing_qualification_roomNb\n")
        for doctor in doctors:
            doctors_file.write(str(doctor) + "\n") #This will have each of the doctor's information on different lines when the doctors.txt file is updated


    def add_dr_to_file(self):
        new_doctor = DoctorManager.enter_dr_info(self) #Calls the method enter_dr_info for user inputs
        self.__doctors_list.append(new_doctor) #This will add the new information into the list
        data = DoctorManager().format_dr_info(new_doctor) #This calls the format_dr_info method to format the new information correctly when added onto doctors.txt
        doctor_id = str(data).split("_")[0]
        doctor_file = open('doctors.txt', 'a')
        doctor_file.write("\n" + data)
        doctor_file.close()

        print("\nDoctor whose ID is", doctor_id, "has been added.")
