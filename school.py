#coding: utf-8
class School(object):
    def __init__(self, students):
        self.students = students

    def saveStudent(self, student):
        self.students.append(student)

    def __getattr__(self, student):
        print u"Ögrenci kayıtlı değildir"
        if student not in self.students:
            self.saveStudent(student)
        return self.students

s = School(["ahmet", "cemil", "dursun"])
print s.nazmiye
print s.cemalettin
