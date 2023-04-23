import patient


class PatientManager:

    def __init__(self):
        self.__patientsLists = []  # Empty list for patients
        PatientManager.read_patients_file(self)

    def format_patient_info_for_file(self, new_patient):
        return patient.Patient.__str__(new_patient)

    def enter_patient_info(self):  # This function ask user to enter the new patients information and creates a new patient with it
        patient_id = str(input("Enter Patient id: "))
        patient_name = str(input("Enter Patient name: "))
        patient_disease = str(input("Enter Patient disease: "))
        patient_gender = str(input("Enter Patient gender: "))
        patient_age = str(input("Enter Patient age: "))
        new_patient = patient.Patient(patient_id, patient_name, patient_disease, patient_gender, patient_age)  # Creates a patient object with the Patient class

        return new_patient

    def read_patients_file(self):  # This function reads the patient file and creates an object for each patient record and appends it to the patients list.
        patient_file = open('patients.txt', 'r')  # Opens the patients file and reads it.
        next(patient_file)  # Skips the first line of the text file (Since the first line in the text file is a template).
        for person in patient_file:  # This for loop will go through each person in the text file.
            data = person.strip().split("_")  # Strips the new line from the data and split each value inbetween each "_".
            new_patient = patient.Patient(data[0], data[1], data[2], data[3], data[4])  # Creates a patient object with the data.
            self.__patientsLists.append(new_patient)  # Appends it to the patient list.
        patient_file.close()

    def search_patient_by_id(self):  # This function searches for a patient using their ID.
        patient_id = input("Enter the Patient id: ")
        counter = 0  # Counter use to keep track of how many iterations the for loop has gone.
        for person in self.__patientsLists:  # This for loop will go through each person in the patient lists.
            counter += 1
            ID, name, disease, gender, age = [str(data) for data in str(person).split("_")] # Assigns each patient properties to its corresponding variable.
            if patient_id == ID:  # Check if the user enter patient id matches with an id in the patient list.
                print(f'\n{"ID":<5s}{"Name":<24s}{"Disease":<18s}{"Gender":<18s}{"Age"}\n')  # Formats the information template.
                print(f'{ID:<5s}{name:<24s}{disease:<18s}{gender:<18s}{age}')   # Formats the patient's information.
                break  # Used to stop the for loop once it found an ID match.
            elif counter == len(self.__patientsLists):  # This is a condition use to display a message for the user, once the for loop has gone through all the patients on the list.
                print("Can't find the Patient with the same id on the system")

    def display_patient_info(self, person):
        if person in self.__patientsLists:
            print(person)

    def edit_patient_info_by_id(self):
        user_input = input("Please enter the id of the Patient that you want to edit their information: ")
        counter = 0
        for person in self.__patientsLists:
            counter += 1
            patient_id = str(person).split("_")[0]
            if user_input == patient_id:
                new_name = str(input("Enter new name: "))
                new_disease = str(input("Enter new disease: "))
                new_gender = str(input("Enter new gender: "))
                new_age = str(input("Enter new age:"))
                updated_patient = patient.Patient(patient_id, new_name, new_disease, new_gender, new_age)
                self.__patientsLists[self.__patientsLists.index(person)] = updated_patient
                PatientManager().write_list_of_patients_to_file(self.__patientsLists)
                break
            elif counter == len(self.__patientsLists):  # This is a condition use to display a message for the user, once the for loop has gone through all the patients on the list.
                print("Can't find the Patient with the same id on the system")

        print("\nPatient whose ID is", patient_id, "has been edited.")

    def display_patients_list(self):
        print(f'\n{"ID":<5s}{"Name":<24s}{"Disease":<18s}{"Gender":<18s}{"Age"}\n')  # Formats and displays the information template.

        for person in self.__patientsLists:
            ID, name, disease, gender, age = [str(data) for data in str(person).split("_")]  # Assigns each patient properties to its corresponding variable.
            print(f'{ID:<5s}{name:<24s}{disease:<18s}{gender:<18s}{age}\n')  # Formats and displays the patient's information.

    def write_list_of_patients_to_file(self, patients_list):
        patient_file = open('patients.txt', 'w')
        self.__patientsLists = patients_list
        for x in patients_list:
            patient_file.write(str(x) + "\n")
        patient_file.close()

    def add_patient_to_file(self):
        new_patient = PatientManager().enter_patient_info()
        self.__patientsLists.append(new_patient)
        data = PatientManager().format_patient_info_for_file(new_patient)
        print(data)
        patient_id = str(data).split("_")[0]
        patient_file = open('patients.txt', 'a+')
        patient_file.write("\n" + data)
        patient_file.close()

        print("\nPatient whose ID is", patient_id, "has been added.")


