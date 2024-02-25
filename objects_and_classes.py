class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def average_grade(self):
        average = sum(sum(grade_list) / len(grade_list) for grade_list in self.grades.values())
        return average

    def __str__(self):

        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)

        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade():.2f}\nКурсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {finished_courses_str}"

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def rate_lec(self, teacher, course, grade):
        if isinstance(teacher, Lecturer) and course in self.courses_attached and course in teacher.courses_in_progress:
            if course in teacher.grades:
                teacher.grades[course] += [grade]
            else:
                teacher.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_in_progress = []

    def average_grade(self):
        average = sum(sum(grade_list) / len(grade_list) for grade_list in self.grades.values())
        return average

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade():.2f}"

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


# Лучшие ученики
best_student = Student('Harry', 'Potter', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']

best_student1 = Student('Hermione', 'Granger', 'your_gender')
best_student1.courses_in_progress += ['Python']
best_student1.finished_courses += ['Введение в программирование']

best_student2 = Student('Ronald', 'Weasley', 'your_gender')
best_student2.courses_in_progress += ['Python']
best_student2.finished_courses += ['Введение в программирование']

# Лучшие преподаватели

best_teacher = Lecturer('Albus', 'Dumbledore')
best_teacher.courses_in_progress += ['Python']

best_teacher1 = Lecturer('Severus', 'Snape')
best_teacher1.courses_in_progress += ['Python']

best_teacher2 = Lecturer('Minerva', 'McGonagall')
best_teacher2.courses_in_progress += ['Python']

cool_student = Student('Ruoy', 'Eman', 'your_gender')
cool_student.courses_attached += ['Python']
cool_student.courses_attached += ['JAVA']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['JAVA']

cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)

cool_reviewer.rate_hw(best_student1, 'Python', 10)
cool_reviewer.rate_hw(best_student1, 'Python', 10)
cool_reviewer.rate_hw(best_student1, 'Python', 10)

cool_reviewer.rate_hw(best_student2, 'Python', 7)
cool_reviewer.rate_hw(best_student2, 'Python', 6)
cool_reviewer.rate_hw(best_student2, 'Python', 6)


cool_student.rate_lec(best_teacher, 'Python', 10)
cool_student.rate_lec(best_teacher, 'Python', 10)
cool_student.rate_lec(best_teacher, 'Python', 10)

cool_student.rate_lec(best_teacher1, 'Python', 9)
cool_student.rate_lec(best_teacher1, 'Python', 8)
cool_student.rate_lec(best_teacher1, 'Python', 10)

cool_student.rate_lec(best_teacher2, 'Python', 9)
cool_student.rate_lec(best_teacher2, 'Python', 10)
cool_student.rate_lec(best_teacher2, 'Python', 9)

print(f'Эксперты:\n\n{cool_reviewer}')
print()

print(f'Лекторы:\n\n{best_teacher}\n\n{best_teacher1}\n\n{best_teacher2}')
print()

print(f'Студенты:\n\n{best_student}\n\n{best_student1}\n\n{best_student2}')
print()
print('Сравнение оценок студентов:', "\n")
print(best_student < best_student1, "\n")
print(best_student > best_student2, "\n")
print(best_student1 == best_student2, "\n")
print()
print('Сравнение оценок лекторов:', "\n")
print(best_teacher < best_teacher1, "\n")
print(best_teacher > best_teacher2, "\n")
print(best_teacher1 == best_teacher2, "\n")

student_list = [best_student, best_student1, best_student2]
teacher_list = [best_teacher, best_teacher1, best_teacher2]

def avg_rating(list_st, course_name):
    sum_all = 0
    count_all = 0
    for elem in list_st:
        if course_name in elem.courses_in_progress:
            sum_all += elem.average_grade()
            count_all += 1
    average_for_all = round(sum_all / count_all, 2)
    return average_for_all


print(f"Средняя оценка для всех студентов по курсу {'Python'}: {avg_rating(student_list, 'Python')}")
print()
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {avg_rating(teacher_list, 'Python')}")
print()
