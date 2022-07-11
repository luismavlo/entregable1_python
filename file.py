import csv
import os
from tkinter.tix import Tree


class File():

    def __init__(self) -> None:
        self.length_file = 0

    def open_files(self):
    """
    La función open_files fusiona varios archivos .csv
    los importa desde la biblioteca.
    Configura las rutas de los archivos.

    >>> Luego, usando el método csv.DictReader() lee todos los archivos .csv
 
    """
        fileQuiz = os.listdir()

        files = [file for file in fileQuiz if file.endswith("csv")]

        try:
            self.length_file = len(files)
        except Exception as e:
            print('no se le puede sacar logitud a null | 0')

        data = []

        for file in files:
            with open(file, encoding="utf-8") as csv_file:
                file_to_process = csv.DictReader(csv_file)
                for i in file_to_process:
                    obj = {
                        "rank": i["Rank"],
                        "firstName": i["First Name"],
                        "lastName": i["Last Name"],
                        "accuracy": i["Accuracy"],
                        "score": i["Score"],
                    }
                    obj['firstName'] = obj['firstName'].lower()
                    obj['lastName'] = obj['lastName'].lower()
                    data.append(obj)
        return(data)

    def process_data_file(self):
    """
    La función process_data_file recibe los datos de los estudiantes, nombre completo,
    score y acuracy.
    Divide los datos 

    >>> retorna el total de puntos acumulados por cada estudiante.
 
    """
        dataStudents = self.open_files()
        data_result = []
        result_score = {}
        result_acuracy = {}

        for i in dataStudents:
            completed_name = i["firstName"] + " " + i["lastName"]

            if completed_name in result_score.keys():
                result_score[completed_name] += int(i["score"])
            else:
                result_score[completed_name] = int(i["score"])

            if completed_name in result_acuracy.keys():
                try:
                    result_acuracy[completed_name] += int(
                        (i["accuracy"]).split()[0]) // self.length_file
                except ZeroDivisionError:
                    print('No se puede dividir por cero')
            else:
                try:
                    result_acuracy[completed_name] = int(
                        (i["accuracy"]).split()[0]) // self.length_file
                except ZeroDivisionError:
                    print('No se puede dividir por cero')

        for i in result_acuracy.items():
            # print(i) (k,v)
            for j in result_score.items():
                # print(j) (k,v)
                if i[0] == j[0]:

                    data = {"name": i[0], "score": j[1], "acuracy": i[1]}
                    data_result.append(data)

        total_points = self.add_points_to_students(
            data_result, [{'name': 'kevin salvador', 'score': 8000}, {'name': 'diego angeles', 'score': 2000}])

        return total_points

    def add_points_to_students(self, data_result: list, extra_student_points: list):
    """
    La función add_points_to_students recibe la lista de estudiantes extra.
    Diccionario:
    name
    score
    Se suma el score, si los nombres son iguales
   
    >>> suma(student['score'] + extra-point['score'])
    >>> se ordenan los resultados con el método sort
    
    """
        for student in data_result:
            for extra_point in extra_student_points:
                if student['name'] == extra_point['name']:
                    student['score'] = int(
                        student['score']) + int(extra_point['score'])

        data_result.sort(key=lambda d: d['score'], reverse=True)
        return data_result
