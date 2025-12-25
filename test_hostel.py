from hostel_allocation import hostel_info

def test_default_hostel_info():
    expected_output = (
        "Student Name: Lavanya\n"
        "Year: 3\n"
        "CGPA: 8.0\n"
        "Distance: 100\n"
        "Priority: Medium Priority"
    )
    assert hostel_info() == expected_output

def test_high_priority():
    expected_output = (
        "Student Name: Ravi\n"
        "Year: 2\n"
        "CGPA: 9.0\n"
        "Distance: 150\n"
        "Priority: High Priority"
    )
    assert hostel_info("Ravi", "2", 9.0, 150, "auto") == expected_output

def test_manual_priority():
    expected_output = (
        "Student Name: Anil\n"
        "Year: 4\n"
        "CGPA: 7.5\n"
        "Distance: 80\n"
        "Priority: Low Priority"
    )
    assert hostel_info("Anil", "4", 7.5, 80, "Low Priority") == expected_output
