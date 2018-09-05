"""
In this script the Lesson class is created in order to be used in the main script to evaluate possible outcomes for
graduation.
"""


class Lesson:
    code = ''
    credit = 0
    year = 0    # Since in first year of METU you cannot take classes from upper years it is important.
    prerequisites = []
    semesters = []     # Semesters of lesson. Add 1 for Fall, 2 for Spring and 3 for Summer. No order needed.
    grade = 'NG'    # NG = Not Graded, the rest is as in the METU System.

    def __init__(self, code, credit, year, prerequisites, semesters, grade='NG'):
        """
        :param code: str
        :param credit: int
        :param year: int
        :param prerequisites: list(str(code))
        :param semesters: list(int)
        :param grade: str(grade)
        """

        self.code = code
        self.credit = credit
        self.year = year
        self.prerequisites = prerequisites
        self.semesters = semesters
        self.grade = grade

    def get_code(self):
        """
        :return: str(code)
        """

        return self.code

    def update_grade(self, grade):
        """
        :param grade: str(grade)
        :return: None
        """

        self.grade = grade

    def is_passed(self):
        """
        :return: bool
        """

        if self.grade in ['AA', 'BA', 'BB', 'CB', 'CC', 'DC', 'DD', 'S', 'EX']:
            return True
        return False

    def get_credits(self):
        """
        :return: float
        """

        if self.grade == 'AA':
            return self.credit * 4.0
        if self.grade == 'BA':
            return self.credit * 3.5
        if self.grade == 'BB':
            return self.credit * 3.0
        if self.grade == 'CB':
            return self.credit * 2.5
        if self.grade == 'CC':
            return self.credit * 2.0
        if self.grade == 'DC':
            return self.credit * 1.5
        if self.grade == 'DD':
            return self.credit * 1.0
        if self.grade == 'FD':
            return self.credit * 0.5
        return 0.0

    def get_credit(self):
        """
        :return: int
        """
        return self.credit

    def get_prerequisites(self):
        """
        :return: list(str(code))
        """

        return self.prerequisites

    def get_semesters(self):
        """
        :return: list(int)      # integers are 1 for Fall, 2 for Spring and 3 for Summer.
        """

        return self.semesters

    def get_grade(self):
        """
        :return: str
        """

        return self.grade