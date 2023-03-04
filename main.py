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

    def rate_lectors(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не тот студент')
            return
        else:
            return self.avg_grade() < other.avg_grade()

    def avg_grade(self):
        self.all_grades = []
        for value in self.grades.values():
            self.all_grades.extend(value)
        return round(sum(self.all_grades) / len(self.all_grades), 2)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self.courses_attached = courses_attached
        self.grades = {}

    def avg_grade(self):
        self.all_grades = []
        for value in self.grades.values():
            self.all_grades.extend(value)
        return round(sum(self.all_grades) / len(self.all_grades), 2)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade()}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Не тот лектор")
            return
        else:
            return self.avg_grade() < other.avg_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self.courses_attached = courses_attached

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


first_student = Student("Ян", "Миронов", "муж")
second_student = Student("Диана", "Арбенина", "жен")
first_lecturer = Lecturer("Илья", "Яшин", ['Python', 'C++'])
second_lecturer = Lecturer("Алексей", "Навальный", ["Advertisement", "Java"])
first_reviewer = Reviewer("Кира", "Ярмыш", ['Python', 'C++'])
second_reviewer = Reviewer("Люба", "Соболь", ["Advertisement", "Java"])

first_student.courses_in_progress += ["Python", "C++"]
second_student.courses_in_progress += ["Advertisement", "Java"]
first_student.finished_courses += ["ChatGPT"]
second_student.finished_courses += ["GIT"]


first_student.rate_lectors(first_lecturer, "C++", 7)
first_student.rate_lectors(first_lecturer, "Python", 10)
first_student.rate_lectors(second_lecturer, "Advertisement", 8)

second_student.rate_lectors(second_lecturer, "Java", 9)
second_student.rate_lectors(second_lecturer, "Advertisement", 10)
second_student.rate_lectors(first_lecturer, 'Python', 4)

first_reviewer.rate_hw(first_student, "Python", 6)
first_reviewer.rate_hw(first_student, 'C++', 9)
first_reviewer.rate_hw(first_student, 'Java', 6)
first_reviewer.rate_hw(second_student, 'Advertisement', 6)
first_reviewer.rate_hw(second_student, 'Git', 9)
first_reviewer.rate_hw(second_student, 'C++', 7)

second_reviewer.rate_hw(first_student, 'Python', 6)
second_reviewer.rate_hw(first_student, 'Python', 9)
second_reviewer.rate_hw(first_student, 'C++', 9)
second_reviewer.rate_hw(second_student, 'Java', 6)
second_reviewer.rate_hw(second_student, 'Advertisement', 9)
second_reviewer.rate_hw(second_student, 'Python', 7)

student_list = [first_student, second_student]


def mid_grade_course(student_list, course):
    all_student_avg_grades = []
    for student in student_list:
        if course not in student.courses_in_progress:
            return "нет курса"
        else:
            all_student_avg_grades.extend(student.grades[course])

    return round(sum(all_student_avg_grades) / len(all_student_avg_grades), 2)


# print(first_lecturer.__lt__(second_lecturer))
print(mid_grade_course(student_list, "Java"))
# print(first_student.courses_in_progress)



