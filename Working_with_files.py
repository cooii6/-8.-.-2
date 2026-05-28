# Тема: Робота з файлами
# Студент: Корпало Ярослав Андрійович
# Програма створює текстовий файл та дозволяє доповнювати його даними.
# Кожен наступний студент відповідає на питання попереднього студента
# і записує своє питання для наступного студента.
# У програмі використано обробку виключних ситуацій try-except.

FILE_NAME = "python_questions.txt"

# Функція створення початкового файлу першим студентом
def create_file():
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            file.write("Тема: Робота з файлами\n")
            file.write("Мета: здобути практичні навички роботи з файлами.\n\n")

            file.write("Студент 1: Корпало Ярослав Андрійович\n")
            file.write("Питання для наступного студента:\n")
            file.write(
                "Що таке конструкція try-except у Python і для чого вона використовується під час роботи з файлами?\n\n"
            )

        print("Файл успішно створено і заповнено початковими даними.")

    except IOError:
        print("Помилка. Не вдалося створити або записати файл.")

# Функція визначає номер наступного студента
def get_next_student_number():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            lines = file.readlines()

        count = 0

        for line in lines:
            if line.startswith("Студент"):
                count += 1

        return count + 1

    except FileNotFoundError:
        print("Помилка. Спочатку потрібно створити файл.")
        return None
    except IOError:
        print("Помилка. Не вдалося прочитати файл.")
        return None

# Функція отримує останнє питання з файлу
def get_last_question():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            lines = file.readlines()

        last_question = ""

        for i in range(len(lines)):
            if lines[i].strip() == "Питання для наступного студента:":
                if i + 1 < len(lines):
                    last_question = lines[i + 1].strip()

        return last_question

    except FileNotFoundError:
        print("Помилка. Спочатку потрібно створити файл.")
        return ""
    except IOError:
        print("Помилка. Не вдалося прочитати файл.")
        return ""

# Функція введення багаторядкової відповіді
def input_answer():
    print("Введіть відповідь на питання.")
    print("Щоб завершити введення, натисніть Enter на порожньому рядку:")

    answer_lines = []

    while True:
        line = input()

        if line == "":
            break

        answer_lines.append(line)

    return "\n".join(answer_lines)

# Функція доповнення файлу даними наступного студента
def add_student_answer():
    question = get_last_question()

    if question == "":
        print("Немає питання для відповіді. Спочатку створіть файл.")
        return

    student_number = get_next_student_number()

    if student_number is None:
        return

    print("\nПитання, на яке потрібно відповісти:")
    print(question)

    surname = input("\nВведіть прізвище студента: ")

    answer = input_answer()

    if answer.strip() == "":
        print("Відповідь не може бути порожньою.")
        return

    next_question = input("Введіть питання для наступного студента: ")

    if next_question.strip() == "":
        print("Питання для наступного студента не може бути порожнім.")
        return

    try:
        with open(FILE_NAME, "a", encoding="utf-8") as file:
            file.write(f"Студент {student_number}: {surname}\n")
            file.write("Відповідь на питання:\n")
            file.write(question + "\n")
            file.write("Відповідь:\n")
            file.write(answer + "\n\n")
            file.write("Питання для наступного студента:\n")
            file.write(next_question + "\n\n")

        print("Дані студента успішно дописано у файл.")

    except IOError:
        print("Помилка. Не вдалося дописати дані у файл.")

# Функція читання та виведення вмісту файлу
def read_file():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            print("\nВміст файлу:")
            print(file.read())

    except FileNotFoundError:
        print("Помилка. Файл не знайдено.")
    except IOError:
        print("Помилка. Не вдалося прочитати файл.")


# Меню програми
def menu():
    while True:
        print("\nМеню")
        print("1 - Створити файл")
        print("2 - Додати студента, відповідь і нове питання")
        print("3 - Вивести вміст файлу")
        print("0 - Вийти")

        choice = input("Виберіть пункт меню: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            add_student_answer()
        elif choice == "3":
            read_file()
        elif choice == "0":
            print("Роботу програми завершено.")
            break
        else:
            print("Помилка. Такого пункту меню немає.")


menu()