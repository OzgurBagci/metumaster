"""
This is a class file, that creates the necessary data structure, which is a acyclic graph or in other words a tree,
for the graph algorithm to work. Nodes are consist of Lesson class objects. Edges are unweighted.
"""


class Graph:
    student = None  # Student that is ought to be processed.
    node_count = 0  # Number of nodes that are in the graph.
    node_dict = {}  # Graph will be implemented as a dictionary.
    stamp_order = []    # Container of lessons in decreasing order of stamp number which are active.

    def __init__(self, student, lessons):
        """
        :param student: Student
        :param lessons: list(Lesson)    # List of new lessons that ought to be taken.
        """

        self.student = student

        added_lessons = {}  # Lesson code as key, Node ID as value.
        pre_dict = {}   # A variable to hold prerequisite courses that are yet to be added to graph.
        pre_lessons = self.student.get_lessons()
        for semester in pre_lessons:
            for lesson in semester:
                self.node_count += 1
                self.node_dict[self.node_count] = lesson, []
                added_lessons[lesson.get_code()] = self.node_count
                self.add_prerequisites(pre_dict, lesson, added_lessons)
                self.add_posts(pre_dict, lesson)
        for lesson in lessons:
            self.node_count += 1
            self.node_dict[self.node_count] = lesson, []
            added_lessons[lesson.get_code()] = self.node_count
            self.add_prerequisites(pre_dict, lesson, added_lessons)
            self.add_posts(pre_dict, lesson)

    def add_prerequisites(self, pre_dict, lesson, added_lessons):
        """
        In order to use in init function.
        :param pre_dict: dict(str: (Lesson, list(int))
        :param lesson: Lesson
        :param added_lessons: dict(str: int)
        :return: None
        """

        pres = lesson.get_prerequisites()
        if len(pres) > 0:
            for pre in pres:
                try:
                    m_id = added_lessons[pre.get_code()]
                    self.node_dict[self.node_count][1].append(m_id)
                    continue
                except KeyError:
                    pass
                try:
                    pre_dict[pre.get_code()].append(self.node_count)
                except KeyError:
                    pre_dict[pre.get_code()] = [self.node_count]

    def add_posts(self, pre_dict, lesson):
        """
        In order to use in init function.
        :param pre_dict: dict(str: (Lesson, list(int))
        :param lesson: Lesson
        :return: None
        """

        try:
            posts = pre_dict[lesson.get_code()]
            for post in posts:
                self.node_dict[self.node_count][1].append(post)
        except KeyError:
            return
