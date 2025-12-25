def safe_float(v, d):
    try:
        return float(v)
    except:
        return d

def safe_int(v, d):
    try:
        return int(v)
    except:
        return d

def hostel_info(name="Lavanya", year="3", cgpa=8.0, distance=100, user_priority="auto"):
    if user_priority == "auto":
        if cgpa >= 8.5 and distance >= 100:
            priority = "High Priority"
        elif cgpa >= 7.0:
            priority = "Medium Priority"
        else:
            priority = "Low Priority"
    else:
        priority = user_priority

    result = (
        f"Student Name: {name}\n"
        f"Year: {year}\n"
        f"CGPA: {cgpa}\n"
        f"Distance: {distance}\n"
        f"Priority: {priority}"
    )
    return result

# For CLI usage
if __name__ == "__main__":
    import sys
    args = sys.argv
    if len(args) == 6:
        output = hostel_info(
            name=args[1],
            year=args[2],
            cgpa=safe_float(args[3], 8.0),
            distance=safe_int(args[4], 100),
            user_priority=args[5]
        )
    else:
        output = hostel_info()
    print(output)
