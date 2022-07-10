import imp
from file import File
from student import Student

file = File()


dataStundent = file.process_file()

student = Student(dataStundent)

student.find_winners(2)
