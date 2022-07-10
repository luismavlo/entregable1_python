import csv
import os
import operator


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

        result = {}

        for i in dataStudents:
            completed_name = i["firstName"] + " " + i["lastName"]
            if completed_name in result.keys():
                result[completed_name] += int(i["score"])
            else:
                result[completed_name] = int(i["score"])

        sortedStudents = sorted(
            result.items(), key=operator.itemgetter(1), reverse=True)
        return sortedStudents
