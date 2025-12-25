import sys

if len(sys.argv)==5:
    script_name=sys.argv[0]
    name=sys.argv[1]
    year=sys.argv[2]
    cgpa=float(sys.argv[3])
    distance=int(sys.argv[4])
    print("user provided input values:")
else:
    script_name=sys.argv[0]
    name="Lavanya"
    year="3"
    cgpa=8.2
    distance=120
    print("no input given - using default values:")

if cgpa>=8.5 and distance>=100:
    priority="High Priority"
elif cgpa>=7.0:
    priority="Medium Priority"
else:
    priority="Low Priority"

print("script name:",script_name)
print("student name:",name)
print("year:",year)
print("cgpa:",cgpa)
print("distance:",distance)
print("priority:",priority)
