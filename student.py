import random


class Student:
    '''checks enrollment status for people'''

    def __init__(self, name, student_status = True):
        self.name = name
        self.status = student_status

    def is_student(self):
        '''checks if person is a student'''
        if self.status:
            return True
        return False
    
    def graduate(self):
        '''updates status for graduating'''
        if self.status:
            self.status = False
            return f'Congratulations {self.name} you did it'
    

class BloomTechStudent(Student):
    '''checks bloomtech enrollment status for people'''

    def __init__(self, name, student_status = True, bloomtech_student = True):
        super().__init__(name, student_status = True)
        self.bloomtech_student = bloomtech_student

    def bloomtech_enrolled(self):
        '''checks if student is enrolled in bloomtech'''
        if self.bloomtech_student:
            return True
        return False
    
    def graduate_bloomtech(self):
        '''updates status for graduating'''
        if self.bloomtech_student:
            self.bloomtech_student = False
            return f'Congratulations {self.name} you did it'   
        if self.statusTrue:
            self.status = False  


names = ['harry', 'henry', 'harriett', 'hailey', 'hannah']

def student_generator():
    student_attributes = []
    student_attributes.append(random.choice(names))
    student_attributes.append(random.choice([True, False]))
    student_attributes.append(random.choice([True, False]))
    if student_attributes[-1]:
        student_attributes[-2] = True
    return student_attributes

student_list = []
for student in range(0,31):
    student_list.append(student_generator())
print(student_list)


        
