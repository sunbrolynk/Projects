student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}


outstanding = range(91,100)
exceeds = range(81, 90)
acceptable = range(71, 80)
fail = range(0, 70)


student_grades = {}

for keys in student_scores.keys():
    student_grades.update({keys: "none"})
for keys in student_scores:
    if student_scores.values() in outstanding:
        student_grades.update({keys: "Outstanding"})
    elif student_scores.values() in exceeds:
        student_grades.update({keys: "Exceeds Expectations"})
    elif student_scores.values() in acceptable:
        student_grades.update({keys: "Acceptable"})
    else:
        student_grades.update({keys: "Fail"})