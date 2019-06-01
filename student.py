"""
In this script the Student class is created in order to be used in the main script to evaluate possible outcomes for
graduation.
"""


class Student:
    def __init__(self, year, semester, lessons):
        """
        :param year: int
        :param semester: int
        :param lessons: list(list(Lesson)) # Inner lists ordered by semester.
        """

        self.year = year
        self.semester = semester
        self.lessons = lessons
        self.credit = 0

        lesson_list = []
        former_cgpa = -1.0
        for curr in lessons:
            if self.cgpa >= 0.0:
                former_cgpa = self.cgpa
                self.cgpa = 0.0
            else:
                self.cgpa = 0.0
            if former_cgpa >= 0.0:
                self.cgpa = former_cgpa * self.credit
            for lesson in curr:
                if lesson.get_code() in [x.get_code() for x in lesson_list]:
                    self.cgpa -= list(filter(lambda x: x.get_code() == lesson.get_code(),
                                             lesson_list))[-1].get_credits()
                else:
                    self.credit += lesson.get_credit()
                lesson_list.append(lesson)
                self.cgpa += lesson.get_credits()
            self.cgpa /= self.credit
        if former_cgpa < 0.0 and self.cgpa < 0.0:
            self.cgpa = 0.0
        elif 0.0 <= former_cgpa < 2.0 and self.cgpa < 2.0:
            self.status = False

        if self.status:
            self.graduation = True

    def get_credit(self):
        """
        :return: int
        """

        return self.credit

    def new_semester(self):
        """
        :return: None
        """

        self.lessons.append([])
        self.semester = self.semester % 3 + 1

    def add_lesson(self, lesson):
        """
        :param lesson: Lesson
        :return: bool   # True if successfully added, otherwise False.
        """

        if not self.is_lesson_ok(lesson):
            return False

        found = False
        if not self.get_status():
            code = lesson.get_code()
            for curr in self.lessons:
                for less in curr:
                    if less.get_code() == code:
                        found = True
                        break
                if found:
                    break
            if not found:
                return False

        if self.semester not in lesson.get_semesters():
            return False

        self.lessons[-1].append(lesson)
        return True

    def end_semester(self):
        """
        :return: None
        """

        lesson_list = []
        for curr in self.lessons:
            for less in curr:
                lesson_list.append(less)

        semester = self.lessons[-1]

        if len(semester) == 0:
            return

        former_cgpa = self.cgpa
        self.cgpa *= self.credit
        for lesson in semester:
            if lesson.get_code() in [x.get_code() for x in lesson_list]:
                self.cgpa -= list(filter(lambda x: x.get_code() == lesson.get_code(),
                                         lesson_list))[-1].get_credits()
            else:
                self.credit += lesson.get_credit()
            self.cgpa += lesson.get_credits()
        self.cgpa /= self.credit

        if former_cgpa < 2.0 and self.cgpa < 2.0:
            self.status = False

        if self.status:
            self.graduation = True

    def is_graduated(self):
        """
        :return: bool
        """

        return self.graduation

    def get_cgpa(self):
        """
        :return: float
        """

        return self.cgpa

    def get_status(self):
        """
        :return: bool
        """

        return self.status

    def get_lessons(self):
        """
        :return: list(list(Lesson))     # Inner list represents semesters.
        """

        return self.lessons

    def get_max_lessons(self):
        """
        :return: int
        """

        if self.semester == 3:
            return 2

        if self.cgpa < 2.0:
            return 5
        if self.cgpa < 2.5:
            return 6
        if self.cgpa < 3.0:
            return 7
        if self.cgpa < 3.5:
            return 8
        return 9

    def get_semester(self):
        """
        :return: int    # 1 for Fall, 2 for Spring and 3 for Summer.
        """

        return self.semester

    def is_lesson_ok(self, lesson):
        """
        Checks if given lesson's prerequisites satisfied.
        :param lesson: Lesson
        :return: bool
        """

        prereq = lesson.get_prerequisites()

        if len(prereq) == 0:
            return True

        old_lessons = []
        for curr in self.lessons:
            for less in curr:
                old_lessons.append(less)

        for req in prereq:
            if not len(list(filter(
                    lambda x: x.get_code() == req and x.get_grade() != 'U' and
                            (x.get_credit() == 0 or x.get_credits() / x.get_credit() >= 1.0), old_lessons))) > 0:
                return False

        return True
