import inspect
from Homework5 import Student

print('Lesson 5: Class Inspect')

print('is function:', inspect.isfunction(Student))
print('is class: ', inspect.isclass(Student))

sigStudent = inspect.signature(Student)

print(sigStudent.parameters)
for item in sigStudent.parameters.items():
    print(f'item - {item[1]}')