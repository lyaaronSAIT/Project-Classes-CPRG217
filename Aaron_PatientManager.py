"""
This is the patient manager class for the Project Classes assignment. In this file will include methods for the user to use to create, display, and edit the patients' data.
This class also has a constructor to create a list to fill the patients' data with. Also, this class will import the patient class to be able to create and update patient objects.

Group: Aaron, Mae, Sang, Alex
Due Date: April 26, 2023
"""
import patient


class PatientManager:

    def __init__(self):  # Constructor, creates a empty list for patients and fill it with the read_patients_file method.
        self.__patientsLists = []  # Empty list for patients
        PatientManager.read_patients_file(self)

    def format_patient_info_for_file(self, new_patient):  # This function used to format the patient data.
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

    def display_patient_info(self, person):  # This function takes a patient object and displays the patient information.
        if person in self.__patientsLists:  # Checks if patient is in list
            print(person)

    def edit_patient_info_by_id(self):  # This function will prompt the user for an ID number and let the user change information for that patient.
        user_input = input("Please enter the id of the Patient that you want to edit their information: ")
        counter = 0  # Counter use to keep track of how many iterations the for loop has gone.
        for person in self.__patientsLists:
            counter += 1
            patient_id = str(person).split("_")[0]  # Use to get only the ID for the patient data.
            if user_input == patient_id:  # Check if ID matches.
                new_name = str(input("Enter new name: "))
                new_disease = str(input("Enter new disease: "))
                new_gender = str(input("Enter new gender: "))
                new_age = str(input("Enter new age:"))
                updated_patient = patient.Patient(patient_id, new_name, new_disease, new_gender, new_age)  # Creates the new patient object.
                self.__patientsLists[self.__patientsLists.index(person)] = updated_patient  # Replace old patient object with the updated one.
                PatientManager().write_list_of_patients_to_file(self.__patientsLists)  # Uses write_list_of_patients_to_file method to save new list.
                break  # End for loop once user has finished updating.
            elif counter == len(self.__patientsLists):  # This is a condition use to display a message for the user, once the for loop has gone through all the patients on the list.
                print("Can't find the Patient with the same id on the system")

        print("\nPatient whose ID is", patient_id, "has been edited.")

    def display_patients_list(self):  # This function will go through each patient in the list and display the information with the correct format.
        print(f'\n{"ID":<5s}{"Name":<24s}{"Disease":<18s}{"Gender":<18s}{"Age"}\n')  # Formats and displays the information template.

        for person in self.__patientsLists:
            ID, name, disease, gender, age = [str(data) for data in str(person).split("_")]  # Assigns each patient properties to its corresponding variable.
            print(f'{ID:<5s}{name:<24s}{disease:<18s}{gender:<18s}{age}\n')  # Formats and displays the patient's information.

    def write_list_of_patients_to_file(self, patients_list):  # This function will write the current patient list to the patient.txt file.
        patient_file = open('patients.txt', 'w')
        self.__patientsLists = patients_list
        for x in patients_list:
            patient_file.write(str(x) + "\n")
        patient_file.close()

    def add_patient_to_file(self):  # This function will add a new patient to the patient.txt file.
        new_patient = PatientManager().enter_patient_info()  # Uses the enter_patient_info method to get the new patients' information.
        self.__patientsLists.append(new_patient)  # Adds the new patient to the list.
        data = PatientManager().format_patient_info_for_file(new_patient)  # Formats the data
        patient_id = str(data).split("_")[0]
        patient_file = open('patients.txt', 'a+')
        patient_file.write("\n" + data)
        patient_file.close()

        print("\nPatient whose ID is", patient_id, "has been added.")


