class Student:
    student_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)

    @property
    def all_grades(self):
        # функция возвращения всех оценок
        sum_grades = []
        for value_item in self.grades.values():
            for x in value_item:
                sum_grades += [x]
        return sum_grades

    def average(self):
        # функция подсчета среднего арифметического числа
        average_grade = 0
        average_grade = sum(Student.all_grades) / len(Student.all_grades)
        return round(average_grade, 1)

    def __lt__(a, b):
        # функция сравнения студентов по средней оценки за домашнее задание
        if a.average() < b.average():
            return f"{a.name} {a.surname} средняя оценка ({a.average()}) меньше, чем {b.name} {b.surname} ({b.average()})"
        elif a.average() == b.average():
            return f"{a.name} {a.surname} средняя оценка ({a.average()}) равна {b.name} {b.surname} ({b.average()})"
        else:
            return f"{a.name} {a.surname} средняя оценка ({a.average()}) больше, чем {b.name} {b.surname} ({b.average()})"



    def __str__(self): #Задание 3.1 студенты
        try:
            print("Имя: ",self.name)
            print("Фамилия: ",self.surname)
            print("Средняя оценка за домашние задания: ",Student.average(self))
            print("Курсы в процессе изучения: ",self.courses_in_progress)
            print("Завершенные курсы: ",self.finished_courses)
            print()
        except ZeroDivisionError:
            print ("нет курсов")

    def lecturer_grades(self, lecturer, course, grade):
        # функция добавления лекторам оценок
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturer_list = []

    def __init__(self, name, surname):
        Lecturer.lecturer_list.append(self)
        self.grades = {}
        super().__init__(name, surname)

    def all_grades(self):
        # функция возвращения всех оценок
        sum_grades = []
        for value_item in self.grades.values():
            for new_list in value_item:
                sum_grades += [new_list]

        return sum_grades

    def average(self):
        # функция подсчета среднего арифметического числа
        average_grade = sum(Lecturer.all_grades(self)) / len(Lecturer.all_grades(self))
        return round(average_grade, 1)

    def __lt__(a, b): #Задание 3.2 Сравнение лекторов
        if a.average() > b.average():
            return f"{a.name} {a.surname} средняя оценка ({a.average()}) больше чем ,{b.name} {b.surname} ({b.average()})"
        elif a.average() == b.average():
            return f"{a.name} {a.surname} средняя оценка ({a.average()}) равна ,{b.name} {b.surname} ({b.average()})"
        else:
            return f"{a.name} {a.surname} средняя оценка ({a.average()}) меньше чем ,{b.name} {b.surname} ({b.average()})"




    def __str__(self): #Задание 3.1 лекторы
        try:
            print("Имя: ",self.name)
            print("Фамилия: ",self.surname)
            print("Средняя оценка за лекции: ",Lecturer.average(self))
            print()
        except ZeroDivisionError:
            print("нет лекций")

    def show_grades(self):
        # просмотр всех оценок у лекторов
        for key_course, value_grades in self.grades.items():
            print("Курс: ",key_course, " Оценка: ",value_grades)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):  #Задание 3.1 проверяющие
        print("Имя: ",self.name)
        print("Фамилия: ",self.surname)
        print()

    def rate_hw(self, student, course, grade):
        # функция добавления студентам оценок
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def courses_average_students(student_list, course):
    # ЗАДАНИЕ 4.1 Подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса
    # в качестве аргументов принимаем список студентов и название курса

    for student in student_list:
        for k, v in student.grades.items():
            if course == k:
                sum_average = sum(v) / len(v)
                print("Студент: ",student.name," ", student.surname," Курс: ",k)
                print("Cредняя оценка за домашние задания: ",round(sum_average, 1))
                print()


def courses_average_lecturer(lecturer_list, course):
    # Задание 4.2 Подсчет средней оценки за лекции всех лекторов в рамках конкретного курса
    # в качестве аргументов принимаем список лекторов и название курса
    for lecturer in lecturer_list:
        for k, v in lecturer.grades.items():
            if course == k:
                sum_average = sum(v) / len(v)
                print("Лектор: ",lecturer.name, " ",lecturer.surname, " Курс: ",k)
                print("Cредняя оценка за курс: ",round(sum_average, 1))
                print()


# студенты
student_peter = Student('Пётр', 'Петров', 'М')
student_peter.courses_in_progress += ['Python']
student_peter.courses_in_progress += ['Git']

student_ivan = Student('Иван', 'Иванов', 'М')
student_ivan.courses_in_progress += ['Python']
student_ivan.courses_in_progress += ['Git']

student_katya = Student('Екатерина', 'Катина', 'Ж')
student_katya.courses_in_progress += ['С++']
student_katya.courses_in_progress += ['Git']


# проверяющие
reviewer_alex = Reviewer('Александр', 'Кузнецов')
reviewer_alex.courses_attached += ['Git']
reviewer_alex.rate_hw(student_peter, 'Git', 8)
reviewer_alex.rate_hw(student_ivan, 'Git', 9)
reviewer_alex.rate_hw(student_katya, 'Git', 7)


reviewer_sidor = Reviewer('Сидор', 'Сидоров')
reviewer_sidor.courses_attached += ['Git']
reviewer_sidor.courses_attached += ['С++']
reviewer_sidor.courses_attached += ['Python']
reviewer_sidor.rate_hw(student_ivan, 'Git', 9)
reviewer_sidor.rate_hw(student_peter, 'Git', 10)
reviewer_sidor.rate_hw(student_katya, 'С++', 8)
reviewer_sidor.rate_hw(student_peter, 'Python', 3)




# лекторы
lecturer_maxim = Lecturer('Максим', 'Максимов')
lecturer_serg = Lecturer('Сергей', 'Сергеев')
lecturer_anton = Lecturer('Антон', 'Антонов')
#оценки лекторам
student_peter.lecturer_grades(lecturer_maxim, 'Python', 7)
student_ivan.lecturer_grades(lecturer_maxim, 'Python', 10)
student_ivan.lecturer_grades(lecturer_serg, 'Git', 8)
student_katya.lecturer_grades(lecturer_serg, 'Git', 7)
student_katya.lecturer_grades(lecturer_maxim, 'Git', 9)
student_katya.lecturer_grades(lecturer_anton, 'C++', 10)

# Задание 3.1__str()__
print('Задание 3.1 __str__ проверяющие')
reviewer_sidor.__str__()
print('Задание 3.1__str__ лекторы')
lecturer_maxim.__str__()
print('Задание 3.1__str__ студенты')
student_peter.__str__()



# подсчет средней оценки за домашние задания
print("Задание 4.1")
courses_average_students(Student.student_list, 'Git')
print("Задание 4.2")
courses_average_lecturer(Lecturer.lecturer_list, 'Git')
# сравнение студентов и лекторов
print('Задание 3.2 Сравнение лекторов и студентов')
print(lecturer_maxim < lecturer_serg)
print(student_peter < student_katya)
