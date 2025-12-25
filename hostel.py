import sys

def safe_float(v,d):
    try:
        return float(v)
    except:
        return d

def safe_int(v,d):
    try:
        return int(v)
    except:
        return d

if len(sys.argv)==6:
    script=sys.argv[0]
    name=sys.argv[1]
    year=sys.argv[2]
    cgpa=safe_float(sys.argv[3],8.0)
    distance=safe_int(sys.argv[4],100)
    user_priority=sys.argv[5]
    print("user provided input values:")
else:
    script=sys.argv[0]
    name="Lavanya"
    year="3"
    cgpa=8.0
    distance=100
    user_priority="auto"
    print("no input given - using default values:")

if user_priority=="auto":
    if cgpa>=8.5 and distance>=100:
        priority="High Priority"
    elif cgpa>=7.0:
        priority="Medium Priority"
    else:
        priority="Low Priority"
else:
    priority=user_priority

print("\n--- Hostel Room Allocation Result ---")
print("script name :",script)
print("student name :",name)
print("year :",year)
print("cgpa :",cgpa)
print("distance :",distance)
print("priority :",priority)
