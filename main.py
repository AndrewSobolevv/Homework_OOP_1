class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade_l):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.finished_courses:
            if course in lecturer.grades_l:
                lecturer.grades_l[course] += [grade_l]
            else:
                lecturer.grades_l[course] = [grade_l]
        else:
            return 'Ошибка'
    def average_rating_s(self):
        count = 0
        if len(self.grades.values()) == 0:
            return 'Ошибка'
        else:
            for rates_s in self.grades.values():
                for rate_s in rates_s:
                    count += rate_s
                    average_rate_s = count / len(rates_s)
                return average_rate_s
    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_rating_s()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершённые курсы: {", ".join(self.finished_courses)}')
    def __lt__(self, other):
        if not isinstance(other, Student) and isinstance(other, Lecturer):
            print('Сравнение невозможно')
        elif (Lecturer.average_rating_l(self, other) < Student.average_rating_s(self, other)):
            return 'Оценка студента, выше оценки лектора'
        elif (Lecturer.average_rating_l(self, other) > Student.average_rating_s(self, other)):
            return 'Оценка студента, ниже оценки лектора'
        else:
            return 'Оценки равны'
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades_l = {}
    def average_rating_l(self):
        count = 0
        if len(self.grades_l.values()) == 0:
            return 'Ошибка'
        else:
            for rates_l in self.grades_l.values():
                for rate_l in rates_l:
                    count += rate_l
                    average_rate_l = count / len(rates_l)
                return average_rate_l
    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating_l()}')

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_rate =[]
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_rate and course in student.finished_courses:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}')


list_lect = ['Василий Петров', 'Иван Голуб']
list_stud = ['Максим Чернов', 'Олег Иванов']
name_cours = 'Python'


def average_rate_hw_cours(list_stud, name_cours):
    count = 0
    for stud in list_stud:
        if not isinstance(stud, Student):
            return
        for i in Student.grades.values(name_cours):
            count += int(i)
            average_rate_hw = count / len(Student.grades.values(name_cours))
    return average_rate_hw


def average_rate_lect(list_lect, name_cours):
    count = 0
    for lect in list_lect:
        if not isinstance(lect, Lecturer):
            return
        for i in Lecturer.grades_l.values(name_cours):
            count += int(i)
            average_rate_lect = count / len(Lecturer.grades_l.values(name_cours))
    return average_rate_lect


student_1 = Student('Максим', 'Чернов', 'man')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Олег', 'Иванов', 'man')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Введение в программирование']

lecturer_1 = Lecturer('Василий', 'Петров')
lecturer_1.courses_attached += ['Введение в программирование']

lecturer_2 = Lecturer('Иван', 'Голуб')
lecturer_2.courses_attached += ['Введение в программирование']

reviewer_1 = Reviewer('Егор', 'Черных')
reviewer_1.courses_rate += ['Введение в программирование']

reviewer_2 = Reviewer('Ольга', 'Васильева')
reviewer_2.courses_rate += ['Введение в программирование']

reviewer_1.rate_hw(student_1, 'Введение в программирование', 10)
reviewer_2.rate_hw(student_2, 'Введение в программирование', 10)

reviewer_1.rate_hw(student_1, 'Введение в программирование', 10)
reviewer_2.rate_hw(student_2, 'Введение в программирование', 10)

student_1.rate_lecturer(lecturer_1, 'Введение в программирование', 10)
student_1.rate_lecturer(lecturer_2, 'Введение в программирование', 10)

student_1.rate_lecturer(lecturer_1, 'Введение в программирование', 10)
student_1.rate_lecturer(lecturer_2, 'Введение в программирование', 10)

print(reviewer_1)
print()
print(reviewer_2)
print()
print(lecturer_1)
print()
print(lecturer_2)
print()
print(student_1)
print()
print(student_2)

