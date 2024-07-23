calls = 0

def count_calls():
    """Функция для подсчета вызовов других функций."""
    global calls
    calls += 1

def string_info(string):
    """Функция, принимающая строку и возвращающая кортеж из длины строки,
    строки в верхнем регистре и строки в нижнем регистре."""
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    """Функция, принимающая строку и список, и возвращающая True, если строка
    присутствует в списке, игнорируя регистр."""
    count_calls()
    normalized_string = string.lower()
    for item in list_to_search:
        if item.lower() == normalized_string:
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)