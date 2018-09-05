"""
This script is creating the logic to take the necessary inputs in order to do the calculations for possible outcomes
of graduation.
"""


from lesson import Lesson
from student import Student


def take_input():
    """
    The last element of the return tuple, which is an integer, is representing the semester amount in which the user
    wanted to be graduated.
    :return: tuple(Student, list(Lesson), int)
    """

    print('You will be prompted for several inputs.')
    print('With each input you will be told the form of input.')
    print('Please, comply.')

    while True:
        try:
            year = int(input('Which year will the evaluation process start? (As a positive integer.):'))
        except ValueError:
            print('Please use integers.')
            continue
        if year <= 0:
            print('At least one year is needed.')
            continue
        break

    while True:
        try:
            spend_semester = int(input('How many semesters did you spend including Summers? (As a positive integer.):'))
        except ValueError:
            print('Please use integers.')
            continue
        if spend_semester <= 0:
            print('At least one semester is needed.')
            continue
        break

    while True:
        try:
            semester = int(input('Which semester will the evaluation process start? ' +
                                 '1 for Fall, 2 for Spring and 3 for Summer:'))
        except ValueError:
            print('Please use integers.')
            continue
        if 3 < semester <= 0:
            print('Input form is not correct.')
            continue
        break
    if semester == 1:
        semester = 3
    else:
        semester -= 1

    while True:
        try:
            graduate_in = int(input('How many semesters in which you want to graduate? (As a positive integer.):'))
        except ValueError:
            print('Please use integers.')
            continue
        if graduate_in <= 0:
            print('At least one semester is needed.')
            continue
        break

    lessons = []
    i = 0
    while i < spend_semester:
        semester_lessons = []
        lessons.append(semester_lessons)
        print('You will be asked questions for the lessons you have taken in your semester number ' + str(i + 1) + '.')
        while True:
            if input('Type --END-- if you have not taken any more lessons in this semester. ' +
                     'Otherwise press Enter without that input:') == '--END--':
                break
            code = input('Type the code of the lesson, it does not checked for correctness, so type carefully:')
            credit = 0
            try:
                credit = int(input('How many credits the lesson have? (As a positive integer.):'))
            except ValueError:
                print('Please use integers.')
            if credit < 0:
                print('A neutral credit is needed.')
                continue
            lesson_year = 0
            try:
                lesson_year = int(input('Which year is the lesson in? (As a positive integer.):'))
            except ValueError:
                print('Please use integers.')
            if lesson_year <= 0:
                print('A positive year is needed.')
                continue
            prerequisites = input('Type the codes of prerequisites, do not use any white spaces, separate with "|". ' +
                                  'Be careful since there is no correctness check for this input:').split('|')

            while True:
                is_ok = True
                open_semesters = input('Type the semesters of lesson, do not use any white spaces, separate with "|". '
                                       'No ordering needed; type 1 for Fall, 2 for Spring and 3 for Summer:').split('|')
                open_semesters = list(map(lambda x: int(x), open_semesters))
                for semester_numb in open_semesters:
                    if semester_numb > 3 or semester_numb < 1:
                        is_ok = False
                if is_ok:
                    break
                continue

            grade = input('Grade of the lesson as letter grade. Type carefully, if typed wrong the program may crash:')

            semester_lessons.append(Lesson(code, credit, lesson_year, prerequisites, open_semesters, grade))
        i += 1

    new_lessons = []
    while True:
        print('You will be asked questions for the lessons you will take.')
        while True:
            if input('Type --END-- if you will not take any more lessons. Otherwise hit Enter without typing:') \
                    == '--END--':
                break
            code = input('Type the code of the lesson, it does not checked for correctness, so type carefully:')
            credit = 0
            try:
                credit = int(input('How many credits the lesson have? (As a positive integer.):'))
            except ValueError:
                print('Please use integers.')
            if credit < 0:
                print('A neutral credit is needed.')
                continue
            lesson_year = 0
            try:
                lesson_year = int(input('Which year is the lesson in? (As a positive integer.):'))
            except ValueError:
                print('Please use integers.')
            if lesson_year <= 0:
                print('A positive year is needed.')
                continue
            prerequisites = input('Type the codes of prerequisites, do not use any white spaces, separate with "|". ' +
                                  'Be careful since there is no correctness check for this input:').split('|')

            if prerequisites[0] == '':
                prerequisites = []

            while True:
                is_ok = True
                open_semesters = input('Type the semesters of lesson, do not use any white spaces, separate with "|". '
                                       'No ordering needed; type 1 for Fall, 2 for Spring and 3 for Summer:').split('|')
                open_semesters = list(map(lambda x: int(x), open_semesters))
                for semester_numb in open_semesters:
                    if semester_numb > 3 or semester_numb < 1:
                        is_ok = False
                if is_ok:
                    break
                continue

            new_lessons.append(Lesson(code, credit, lesson_year, prerequisites, open_semesters))
        break

    return Student(year, semester, lessons), new_lessons, graduate_in


# Below code is for testing purposes. May be removed from production software.
if __name__ == '__main__':
    student, lesson, grad_in = take_input()
    # Add test cases below. For test cases, you can use classes' internal variables.
    print('\n\n\nTesting starts...')
    print('Lessons the student has taken are going to be printed.')
    for curr in student.lessons:
        for less in curr:
            print(less.get_code())
    print('Lessons the student will take are going to be printed.')
    for less in lesson:
        print(less.get_code())
    print('Student status: ' + str(student.get_status()))
    print('Student CGPA: ' + str(student.get_cgpa()))
