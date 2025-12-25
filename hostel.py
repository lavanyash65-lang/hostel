import sys

def allocate_room(name,year,cgpa,distance):
    if cgpa>=8.5 and distance>=200:
        return "High Priority"
    elif cgpa>=7.0:
        return "Medium Priority"
    else:
        return "Low Priority"

use_args=False
if len(sys.argv)==5:
    try:
        name=sys.argv[1]
        year=sys.argv[2]
        cgpa=float(sys.argv[3])
        distance=int(sys.argv[4])
        use_args=True
    except:
        use_args=False

if not use_args:
    name="Anita"
    year="2nd Year"
    cgpa=8.2
    distance=180

priority=allocate_room(name,year,cgpa,distance)

print("\n--- Hostel Room Allocation Result ---")
print("Student Name :",name)
print("Year         :",year)
print("CGPA         :",cgpa)
print("Distance     :",distance)
print("Priority     :",priority)
