import sys
def allocate_room(name,year,cgpa,distance):
    if cgpa>=8.5 and distance>=200:
        return "High Priority"
    elif cgpa>=7.0:
        return "Medium Priority"
    else:
        return "Low Priority"
if len(sys.argv)>1:
    data=sys.argv[1:]
    name=data[0]
    year=data[1]
    cgpa=float(data[2])
    distance=int(data[3])
else:
    name="lavanya"
    year="3rd Year"
    cgpa=8.9
    distance=250
priority=allocate_room(name,year,cgpa,distance)
print(name)
print(year)
print(cgpa)
print(distance)
print(priority)
