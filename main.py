
from file import File
from student import Student

file = File()


dataStundent = file.process_data_file()


student = Student(dataStundent)

student.find_winners(3)
print(student.find_users_by_percent(70))
