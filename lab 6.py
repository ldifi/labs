def zad_1():
    c = {
        "Россия": "Москва",
        "США": "Вашингтон DC",
        "Франция": "Париж",
        "Китай": "Пекин",
        "Германия": "Берлин",
        "Корея":"Сеул"
    }
    country = input("Введите название страны: ")
    if country in c:
        сity = c[country]
        print(f"Столица {country} - {сity}")
    else:
        print("Этой страны нет в списке")

    sorted_c = sorted(c.items())
    print("Список стран и их столиц в алфавитном порядке:")
    for country, city in sorted_c:
        print(f"{country} - {city}")

def zad_2():
    scores = {
        "А": 1, "Б": 3, "В": 1, "Г": 3, "Д": 2, "Е": 1, "Ё": 3, "Ж": 5, "З": 5,
        "И": 1, "Й": 4, "К": 2, "Л": 2, "М": 2, "Н": 1, "О": 1, "П": 2, "Р": 1,
        "С": 1, "Т": 1, "У": 2, "Ф": 10, "Х": 5, "Ц": 5, "Ч": 5, "Ш": 8, "Щ": 10,
        "Ъ": 10, "Ы": 4, "Ь": 3, "Э": 8, "Ю": 8, "Я": 3
    }
    word = input("Введите слово: ").upper()
    summa = sum(scores[letter] for letter in word)
    print(f"Стоимость слова '{word}' равна {summa} очкам")


def zad_3():
    students = [
        {"name": "Маша", "languages": ["английский", "французский", "испанский"]},
        {"name": "Катя", "languages": ["немецкий", "русский", "английский"]},
        {"name": "Кирилл", "languages": ["японский", "китайский", "английский"]},
        {"name": "Берни", "languages": ["испанский", "итальянский", "французский"]}]

    lang = set()
    for student in students:
        lang.update(student["languages"])

    sl = sorted(lang)
    print("Список всех языков:", sl)

    china = []
    for student in students:
        if "китайский" in student["languages"]:
            china.append(student["name"])
    print("Студенты, знающие китайский язык:", china)