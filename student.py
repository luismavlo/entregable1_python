class Student():

    def __init__(self, list_student) -> None:
        self.list_student = list_student

    def find_winners(self, positions: int):
        return self.list_student[0:positions]

    def find_users_by_percent(self, percent: int):

        student_filter_by_percent = []
        for student in self.list_student:
            if student['acuracy'] >= percent:
                student_filter_by_percent.append(student)
        return(student_filter_by_percent)
