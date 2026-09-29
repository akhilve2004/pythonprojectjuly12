#1. #  Given a dictionary
student_grades={'Alice':98,'bob':85,'charlie':74,'mike':70}
#print the grade of charlie
print(student_grades)
print(student_grades['charlie'])
#update the grade of bob to 90
student_grades['bob']=90
print(student_grades)
#print the total number of students
print(len(student_grades))
#print all student names in the given dictionary
print(student_grades.keys())


#2.Given a dictionary
#
student_marks={'Arun':{'maths':30,'science':35,'english':40,'history':33},
               'Amal':{'maths':40,'science':45,'english':48,'history':43},
               'Anu':{'maths':45,'science':46,'english':47,'history':49}}

#print the mark of Amal in the subject History
#Update the mark of Arun in maths to 35
#print the marks of all students (in all subjects)
print(student_marks)
print(student_marks['Amal']['history'])
student_marks ['Arun']['maths']=35
print(student_marks)
print(student_marks.keys())
