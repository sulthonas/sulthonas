def gpa(grades):
  points = {'A+': 4.0, 'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.67,
            'C+': 2.33, 'C': 2.0, 'C-': 1.67, 'D+': 1.33, 'D': 1.0, 'F': 0.0}
  num_courses = len(grades)
  total_points = sum(points[grade] for grade in grades)
  if num_courses > 0:
    return total_points / num_courses
  else:
    return 0.0

grades = []
while True:
  grade = input("Masukkan nilai huruf (atau kosong untuk berhenti): ")
  if grade == "":
    break
  else:
    grades.append(grade)

gpa = gpa(grades)
print("GPA Anda adalah {:.3f}".format(gpa))
