def personal_sum(numbers):
    """
    Подсчитывает сумму чисел в коллекции, игнорируя нечисловые элементы.
    """
    result = 0
    incorrect_data = 0
    for item in numbers:
        try:
            result += item
        except TypeError:
            incorrect_data += 1
            print(f"Некорректный тип данных для подсчёта суммы - {item}")
    return result, incorrect_data

def calculate_average(numbers):
    """
    Вычисляет среднее арифметическое чисел в коллекции.
    """
    try:
        total, incorrect_count = personal_sum(numbers)
        if incorrect_count == len(numbers):
            print("В numbers записан некорректный тип данных")
            return None
        return total / len(numbers)
    except ZeroDivisionError:
        return 0
    except TypeError:
        print("В numbers записан некорректный тип данных")
        return None

# Пример выполнения программы:
print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
