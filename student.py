class Student():

    def __init__(self, list_student) -> None:
        self.list_student = list_student

    def find_winners(self, positions: int):
           """
    La función find_winners hace un llamado a los 3 primeros lugares en el score.
    ordenado de mayor a menor por el index.
"""
        return self.list_student[0:positions]

    def find_users_by_percent(self, percent: int):
           """
    La función find_users_by_percent hace una consulta del score 
    y el acuracy a la lista de estudiantes
    For:
    Si el student['acuracy'] es mayor o igual al porcentaje 
    se aplica método append
    devolviendo una nueva lista en el main.py 

    """
        student_filter_by_percent = []
        for student in self.list_student:
            if student['acuracy'] >= percent:
                student_filter_by_percent.append(student)
        return(student_filter_by_percent)
