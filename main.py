from file import File
from student import Student

file = File()


data_stundent = file.process_data_file()


student = Student(data_stundent)

print(student.find_winners(2))
print(student.find_users_by_percent(70))
