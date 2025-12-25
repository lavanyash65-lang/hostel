def allocate_room(name, year, cgpa, distance):
    if cgpa >= 8.5 and distance >= 200:
        priority = "High Priority"
    elif cgpa >= 7.0:
        priority = "Medium Priority"
    else:
        priority = "Low Priority"
    return priority
use_user_input = True   
if use_user_input:
    name = input("Enter Student Name: ")
    year = input("Enter Year of Study: ")
    cgpa = float(input("Enter CGPA: "))
    distance = int(input("Enter Distance from Home (km): "))
else:
    name = "lavanya"
    year = "3rd Year"
    cgpa = 8.9
    distance = 250
priority = allocate_room(name, year, cgpa, distance)
print("\n--- Hostel Room Allocation Result ---")
print("Student Name :", name)
print("Year         :", year)
print("CGPA         :", cgpa)
print("Distance     :", distance)
print("Priority     :", priority)
