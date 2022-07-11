class Student():

    def __init__(self, list_student) -> None:
        self.list_student = list_student

    def find_winners(self, positions: int):
        """
        The find_winners function calls the top X places in the score.
        sorted from highest to lowest by index.

        >>> receives a number that is the amount of the best students

        >>> return  [{'name': 'xxx', 'score': xxx, 'acuracy': xx}, ...]
        """

        return self.list_student[0:positions]

    def find_users_by_percent(self, percent: int):
        """
        The find_users_by_percent function queries the score
        and the acuracy to the student list
        For:
        If the student['acuracy'] is greater than or equal to the percentage
        append method is applied
        returning a new list in main.py

        >>> receives the percent for filter 

        >>> return [{'name': 'diego angeles', 'score': 16640, 'acuracy': 95}, .....]


        """
        student_filter_by_percent = []
        for student in self.list_student:
            if student['acuracy'] >= percent:
                student_filter_by_percent.append(student)
        return(student_filter_by_percent)
