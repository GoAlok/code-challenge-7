"""
    Introduction:
        You have access to a database of student_score in the format of dictionary. 
        The keys in student_score are the names of the students and the values are
        their exam score.
        
        Write a program that converts their scores to grades. By the end of your 
        program, you should have new dictionary called student_grades that should 
        contain student names for keys and their grades for values. The final 
        version of the student_grades dictionary will be checked.
        
            score:                  Grade
        -------------------------------------------------
            91  -   100     :   "Outstanding"
            81  -   90      :   "Exceeds Expectations"
            71  -   80      :   "Acceptable"
            70 and lower    :   "Fail"
"""

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermon": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if int(score) >= 91:
        student_grades[student] = "Outstanding"
    elif int(score) >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif int(score) >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
print(student_grades)