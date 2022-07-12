from file import File
from student import Student

file = File()


data_stundent = file.process_data_file()


student = Student(data_stundent)

data_stundent_winners = student.find_winners(3)
data_stundent_by_percent = student.find_users_by_percent(70)
# print(student.find_winners(2))
# print(student.find_users_by_percent(70))
print("\n---------------students with the highest score---------------\n")
for i in data_stundent_winners:
    position = 0
    name = i["name"]
    score = i["score"]
    acuracy = i["acuracy"]
    print(
        f"Rank: {position} \nName: {name} \nScore: {score} \nAcuracy: {acuracy} \n  ********** \n", end="\n")
print("\n---------------students with acuracy greater than 70%---------------\n")
for i in data_stundent_by_percent:
    name = i["name"]
    score = i["score"]
    acuracy = i["acuracy"]
    print(
        f"Name: {name} \nScore: {score} \nAcuracy: {acuracy}% \n  ********** \n", end="\n")
