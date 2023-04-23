class Management:

    def display_menu(self):

        print("Welcome to Alberta Hospital (AH) Management system ")

        while True:
            print("Select from the following options, or select 3 to stop:")
            print("1 - Doctor")
            print("2 - Patients")
            print("3 - Exit Program")

            user_choice_options = input(">>> ")

            doctor_manager = DoctorManager()
            patient_manager = PatientManager()

            if user_choice_options == "1":
                while True:
                    print("Doctors Menu:")
                    print("1 - Display Doctors list")
                    print("2 - Search for doctor by ID")
                    print("3 - Search for doctor by name")
                    print("4 - Add doctor")
                    print("5 - Edit doctor info")
                    print("6 - Back to the Main Menu")

                    user_doctor_choice = input(">>> ")

                    if user_doctor_choice == "1":
                        doctor_manager.display_doctors_list()  # Display Doctors list

                    elif user_doctor_choice == "2":
                        doctor_manager.search_doctor_by_id()  # Search for doctor by ID

                    elif user_doctor_choice == "3":
                        doctor_manager.search_doctor_by_name()  # Search for doctor by name

                    elif user_doctor_choice == "4":
                        doctor_manager.add_dr_to_file()  # Add doctor

                    elif user_doctor_choice == "5":
                        doctor_manager.edit_doctor_info()  # Edit doctor info

                    elif user_doctor_choice == "6":
                        break  # Back to the Main Menu

            if user_choice_options == "2":
                while True:
                    print("Patients Menu:")
                    print("1 - Display patients list")
                    print("2 - Search for patient by ID")
                    print("3 - Add patient")
                    print("4 - Edit patient info")
                    print("5 - Back to the Main Menu")

                    user_patients_options = input(">>> ")

                    if user_patients_options == "1":
                        patient_manager.display_patients_list()  # Display patients list"

                    elif user_patients_options == "2":
                        patient_manager.search_patient_by_id()  # Search for patient by ID

                    elif user_patients_options == "3":
                        patient_manager.add_patient_to_file()  # Add patient

                    elif user_patients_options == "4":
                        patient_manager.edit_patient_info_by_id()  # Edit patient info

                    elif user_patients_options == "5":
                        break  # Back to the Main Menu

            if user_choice_options == "3":
                print("Thanks for using the program. Bye!")
                break
                
management_system = Management()

management_system.display_menu()  # Display
