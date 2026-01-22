import pandas as pd
from datetime import datetime
import time 

  
print(f"ATTENDANCE FOR {datetime.now().strftime('%A %d-%m-%Y')}")
attendance = {"FULL NAME" : [],
              "TIME IN"   : [],
              "STATUS"    : []}
# To add new students     
def update_attendence():
    new_name= input("Enter your FULL NAME --> ").strip().title()
    now = datetime.now()
    time_in = now.strftime("%I:%M %p")
    arrival_limit = now.replace(hour= 10, minute = 0, second = 0, microsecond= 0)
    if now <= arrival_limit:
        status = "EARLY"
    else:
        status = "LATE"
    attendance["FULL NAME"].append(new_name)
    attendance["TIME IN"].append(time_in)
    attendance["STATUS"].append(status)

# To Search for Students
def search_students():
    name = input("Type the first 3 letters of the name (e.g., Aki): ").strip().title()
    for d, student in enumerate(attendance["FULL NAME"]):
        if name in student:
            print(f"{student} arrived at {attendance["TIME IN"][d]} ({attendance["STATUS"][d]})")
            break
    else:
        print("Name not found")
        
        
def save_attendance():
    with open("attendance_database.txt", "a") as d:
        d.write(f"\n{attendance}")
    print("Attendance saved to Attendance_database.txt")
    
    
# Main loop
while True:
    print("\n === ATTENDANCE SYSTEM ===")
    print("1. Mark Attendance")
    print("2. View Today's Attendance")
    print("3. Search Student Record")
    print("4. Save Attendance Records")
    print("5. View Past Attendance Records")
    print("6. Close attendance sheet")
    print("=========================")

    try:
        menu_option = int(input("\nEnter an Option (1 - 6) --> "))
        time.sleep(2)
        if menu_option == 1:
            update_attendence()
        elif menu_option == 2:
            attend = pd.DataFrame(attendance)
            attend.index = attend.index + 1
            print(attend)
        elif menu_option == 3:
            search_students()
        elif menu_option == 4:
            save_attendance()
        elif menu_option == 5:
            try:
                with open("attendance_database.txt", "r") as f:
                    records = f.read()
                    print("\n=== PAST ATTENDANCE RECORDS ===")
                    print(records)
            except FileNotFoundError:
                print("No past records found.")
        elif menu_option == 6:
            print("Thank you for using the Attendance System. Goodbye!")
            break
        else:
            print("Please enter a valid option [1, 2, 3, 4] Try Again!!..")
    except ValueError:
        print("Please enter a number....")
    time.sleep(3)