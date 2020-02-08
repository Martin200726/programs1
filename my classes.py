# -*- coding: cp1251 -*-
class Student:

    name = ""
    surname = ""
    grade = 1
    mark = {"math":0,"ph":0}    
    
    def __init__(self,name,surname,grade,mark):
        self.name = name
        self.surname = surname
        self.grade = grade
        self.mark["math"] = mark["math"]
        self.mark["ph"] = mark["ph"]
    

vasya = Student("Вася","Пупкин",7,{"math":4,"ph":5})
print(vasya.name)
print(vasya.surname)
print(vasya.grade)
print(vasya.mark)
