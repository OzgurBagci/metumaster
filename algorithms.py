"""
In this file the algorithms are defined which are going to be used while evaluating outcomes for graduation. As of now
there is only random force algorithm present. There will be other algorithms with future versions.
"""

import random
import copy
import takeinput


def call_random_force(student, new_lessons, graduate_in):
    """
    This function calls the real algorithm. Because of the dynamics of the algorithm used, this infinite loop is needed.
    :param student: Student
    :param new_lessons: list(Lesson)
    :param graduate_in: int
    :return: list(list(Lesson))     # Inner lists represents semesters.
    """

    while True:
        cpy_stud = copy.deepcopy(student)
        cpy_less = copy.deepcopy(new_lessons)
        result = random_force(cpy_stud, cpy_less, graduate_in)
        if type(result) is list:
            return result


def random_force(student, new_lessons, graduate_in):
    """
    - This algorithm, for now, finds only one solution which is not always optimum. Even, most of the time not optimum.
    - Note that only a few grades included to this algorithm since otherwise it takes too long to evaluate for some
        inputs.

    :param student: Student
    :param new_lessons: list(Lesson)
    :param graduate_in: int
    :return: list(list(Lesson)) || False     # Inner lists represents semesters. False in case of failure.
    """

    grade_list = ['CC', 'DC', 'DD']     # Some grades removed to speed up. Change the passing grades for other tests.
    no_credit_grades = ['S']    # Some grades removed to speed up.

    if len(new_lessons) == 0:
        return student.get_lessons()
    elif graduate_in == 0:
        return False

    student.new_semester()

    old_lessons = []
    max_lessons = student.get_max_lessons()
    status = student.get_status()

    if not student.get_status():
        for curr in student.get_lessons():
            for less in curr:
                if less.get_credit() > 0.0:
                    old_lessons.append(less)

    max_available = 0

    if not len(old_lessons) == 0:
        lessons = old_lessons
        max_available = len(list(filter(lambda x: student.get_semester() in x.get_semesters(), lessons)))
    else:
        lessons = new_lessons
        for less in lessons:
            if student.is_lesson_ok(less) and \
                    less in list(filter(lambda x: student.get_semester() in x.get_semesters(), lessons)):
                max_available += 1

    add_lessons = []
    add_in = []
    i = 0
    while i < min(max_lessons, max_available):
        lesson = random.choice(lessons)
        if len(list(filter(lambda x: lesson.get_code() == x.get_code(), add_in))):
            continue
        new_lesson = copy.deepcopy(lesson)
        if lesson.get_credit() > 0:
            grade = random.choice(grade_list)
        else:
            grade = random.choice(no_credit_grades)
        if student.add_lesson(new_lesson):
            new_lesson.update_grade(grade)
            add_in.append(new_lesson)
            i += 1
            lessons.remove(lesson)
            if grade in ['FD', 'FF', 'NA', 'U'] and status:
                add_lessons.append(lesson)
    new_lessons.extend(add_lessons)

    student.end_semester()

    result = random_force(student, new_lessons, graduate_in - 1)
    if result:
        return result


# Below code is for testing purposes. May be removed from production software. Change algorithms if needed.
if __name__ == '__main__':
    student, new_lessons, grad_in = takeinput.take_input()
    print('\n\n\nTesting starts...')
    print('Lessons the student has taken are going to be printed.')
    for curr in student.lessons:
        for less in curr:
            print(less.get_code())
    print('Lessons the student will take are going to be printed.')
    for less in new_lessons:
        print(less.get_code())
    print('Student status: ' + str(student.get_status()))
    print('Student CGPA: ' + str(student.get_cgpa()))
    transcript = call_random_force(student, new_lessons, grad_in)
    print('\nTRANSCRIPT TESTS\n')
    print('Transcript with Objects: ', transcript)
    for i in range(len(transcript)):
        print('\nSEMESTER NUMBER ' + str(i + 1) + ' STARTS!')
        for lesson in transcript[i]:
            print(lesson.get_code(), lesson.get_grade())
    print('END')
