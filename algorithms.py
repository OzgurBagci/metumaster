"""
In this file the algorithms are defined which are going to be used while evaluating outcomes for graduation. As of now
there is only random force algorithm present. There will be other algorithms with future versions.
"""

import constants
import operator


def brute_force(student, new_lessons):
    """
    Brute force algorithm to evaluate graduation status in finite amount of time.

    :param student: Student
    :param new_lessons: list(Lesson)
    :return: Student
    """

    status = student.get_status()

    if student.is_graduated():
        return student

    student.new_semester()

    if not status:
        old_lessons = [item for sub in student.get_lessons() for item in sub]
        old_lessons.sort(key=operator.attrgetter('credit'), reverse=True)

        cgpa = student.get_cgpa()
        credit = student.get_credit()

        needed_credit = (2 - cgpa) * credit

        for i, lesson in enumerate(old_lessons):
            if i + 1 == student.get_max_lessons():
                break
            grades = list(constants.CREDIT_GRADES)
            grades.reverse()
            grade_index = grades.index(lesson.get_grade())
            lesson_credit = lesson.get_credit()
            if (needed_credit <= lesson_credit * (len(grades) - grade_index - 1)):
                to_get = lesson_credit * (len(grades) - grade_index - 1) - needed_credit
                to_get /= lesson_credit
                to_get -= int(to_get / 0.5)
                to_get = int(to_get * 2)
                lesson.update_grade(grades[to_get])
                break
            else:
                lesson.update_grade('AA')
    else:
        pass

    student.end_semester()
