import os
import json

os.system('cls')
print("STUDENT INFORMATION SYSTEM")
print('--------------------------')

crush_record = {}

while True:
    print("\nSelect from the following options: ")
    print("A - Add student record")
    print("B - Search student record")
    print("C - Edit student record")
    print("D - Delete student record")
    print("E - Print all records")
    print("F - Export data to JSON")
    print("G - Exit system")

    elite = input("Enter here: ").lower().strip()

    # ADD STUDENT
    if elite == 'a':
        os.system('cls')
        print("ADD STUDENT RECORD")

        student_id = input("Input student ID number: ").upper()

        first_name = input("Input student First Name: ").upper()
        last_name = input("Input student Last Name: ").upper()
        course = input("Input student Course: ").upper()
        section = input("Input student Section: ").upper()
        gmail = input("Input student Gmail: ")

        crush_record[student_id] = [first_name, last_name, course, section, gmail]
        print("DATA SAVED SUCCESSFULLY")

    # SEARCH ALL STUDENTS
    elif elite == 'b':
        os.system('cls')
        print("SEARCH STUDENT RECORD")

        search_id = input("ENTER STUDENT ID TO SEARCH: ").upper()

        if search_id in crush_record:
            print("\nRECORD FOUND:")
            print("-------------------------")
            print("First Name:", crush_record[search_id][0])
            print("Last Name :", crush_record[search_id][1])
            print("Course    :", crush_record[search_id][2])
            print("Section   :", crush_record[search_id][3])
            print("Gmail     :", crush_record[search_id][4])
            print("-------------------------")
        else:
            print("NO RECORD FOUND")

    # EDIT STUDENT
    elif elite == 'c':
        os.system('cls')
        print("EDIT STUDENT RECORD")

        search_id = input("ENTER STUDENT ID TO EDIT: ").upper()

        if search_id in crush_record:
            print("\nCURRENT RECORD:")
            print(crush_record[search_id])
            print("-------------------------")

            first_name = input("New First Name: ").upper()
            last_name = input("New Last Name: ").upper()
            course = input("New Course: ").upper()
            section = input("New Section: ").upper()
            gmail = input("New Gmail: ")

            crush_record[search_id] = [first_name, last_name, course, section, gmail]
            print("RECORD UPDATED SUCCESSFULLY")
        else:
            print("NO RECORD FOUND")

    # DELETE STUDENT
    elif elite == 'd':
        os.system('cls')
        print("DELETE STUDENT RECORD")

        search_id = input("ENTER STUDENT ID TO DELETE: ").upper()

        if search_id in crush_record:
            del crush_record[search_id]
            print("RECORD DELETED SUCCESSFULLY")
        else:
            print("NO RECORD FOUND")

    # PRINT ALL RECORDS
    elif elite == 'e':
        os.system('cls')
        print("ALL STUDENT RECORDS")
        print("--------------------------")

        if not crush_record:
            print("NO RECORDS AVAILABLE")
        else:
            for sid, info in crush_record.items():
                print(f"\nSTUDENT ID: {sid}")
                print(f"First Name: {info[0]}")
                print(f"Last Name : {info[1]}")
                print(f"Course    : {info[2]}")
                print(f"Section   : {info[3]}")
                print(f"Gmail     : {info[4]}")
                print("------------------------")

    # EXPORT DATA
    elif elite == 'f':
        print("EXPORTING DATA...")

        with open('crush_record.json', 'w') as new_file:
            json.dump(crush_record, new_file, indent=4)

        print("DATA EXPORTED SUCCESSFULLY (crush_record.json created)")

    # EXIT SYSTEM
    elif elite == 'g':
        print("EXITING SYSTEM...")
        break

    else:
        print("Invalid Choice, Please Enter A Valid Option.")
