# corey schafer python tutorial 5: Dictionaries
# https://www.youtube.com/watch?v=daefaLgNkw0

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

student['phone'] = '555-555 555'

print student.get('phone', 'Not Found')

student['name'] = 'Jane'

print student

student.update({'name': 'John', 'age': 23, 'phone': '555-5555'})
print student

#del student['age']
age = student['age']
print student
print age

print student.keys()
print student.values()
print student.items()

for key, value in student.items():
    print key, value
