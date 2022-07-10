import csv
import os


class File():

    def open_files(self):
        fileQuiz = os.listdir()

        files = [file for file in fileQuiz if file.endswith("csv")]

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

    def process_file(self):
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
                result_acuracy[completed_name] += int(
                    (i["accuracy"]).split()[0]) // 4
            else:
                result_acuracy[completed_name] = int(
                    (i["accuracy"]).split()[0]) // 4

        for i in result_acuracy.items():
            # print(i) (k,v)
            for j in result_score.items():
                # print(j) (k,v)
                if i[0] == j[0]:
                    data = {"name": i[0], "score": j[1], "acuracy": i[1]}
                    data_result.append(data)

        data_result.sort(key=lambda d: d['score'], reverse=True)

        return data_result
