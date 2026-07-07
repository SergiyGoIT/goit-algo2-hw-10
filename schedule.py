class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()


def create_schedule(subjects, teachers):
    uncovered_subjects = set(subjects)
    schedule = []

    while uncovered_subjects:
        best_teacher = None
        best_subjects = set()

        for teacher in teachers:
            available_subjects = teacher.can_teach_subjects & uncovered_subjects

            if not available_subjects:
                continue

            if (
                best_teacher is None
                or len(available_subjects) > len(best_subjects)
                or (
                    len(available_subjects) == len(best_subjects)
                    and teacher.age < best_teacher.age
                )
            ):
                best_teacher = teacher
                best_subjects = available_subjects

        if best_teacher is None:
            return None

        best_teacher.assigned_subjects = best_subjects
        schedule.append(best_teacher)
        uncovered_subjects -= best_subjects

    return schedule


if __name__ == "__main__":
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}

    teachers = [
        Teacher(
            "Олександр",
            "Іваненко",
            45,
            "o.ivanenko@example.com",
            {"Математика", "Фізика"},
        ),
        Teacher(
            "Марія", 
            "Петренко", 
            38, 
            "m.petrenko@example.com", 
            {"Хімія"}),
        Teacher(
            "Сергій",
            "Коваленко",
            50,
            "s.kovalenko@example.com",
            {"Інформатика", "Математика"},
        ),
        Teacher(
            "Наталія",
            "Шевченко",
            29,
            "n.shevchenko@example.com",
            {"Біологія", "Хімія"},
        ),
        Teacher(
            "Дмитро",
            "Бондаренко",
            35,
            "d.bondarenko@example.com",
            {"Фізика", "Інформатика"},
        ),
        Teacher("Олена", 
            "Гриценко", 
            42, 
            "o.grytsenko@example.com", 
            {"Біологія"}),
    ]

    schedule = create_schedule(subjects, teachers)

    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            assigned_subjects = ", ".join(sorted(teacher.assigned_subjects))
            print(
                f"{teacher.first_name} {teacher.last_name}, "
                f"{teacher.age} років, email: {teacher.email}"
            )
            print(f"   Викладає предмети: {assigned_subjects}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")