# Импортируем библиотеки
# Библиотека requests позволяет отправлять HTTP-запросы к веб-сайтам
# Библиотека BeautifulSoup позволяет анализировать HTML-код и извлекать из него данные
import requests
from bs4 import BeautifulSoup

# Создаем пустой список для сайтов
# Список - это изменяемая коллекция элементов, которые могут быть любого типа
sayte = []

# Запрашиваем у пользователя адреса сайтов в цикле
# Цикл while выполняется, пока условие истинно
while True:
    # Вводим адрес сайта
    # Функция input() позволяет получить строку от пользователя
    sayt = input("Введите адрес сайта или напишите 'стоп', чтобы закончить: ")
    # Проверяем, не ввел ли пользователь слово "стоп"
    # Оператор == сравнивает два значения на равенство
    if sayt == "стоп":
        # Прерываем цикл
        # Оператор break выходит из цикла
        break
    # Пытаемся отправить запрос по адресу сайта
    # Блок try-except позволяет обрабатывать исключения, которые могут возникнуть во время выполнения кода
    try:
        # Отправляем запрос и получаем ответ
        # Метод get() библиотеки requests принимает адрес сайта и возвращает объект Response, содержащий различную информацию о ответе
        otvet = requests.get(sayt)
        # Проверяем, что ответ успешный (код 200)(Код ответа 200 ОК означает успешный запрос к серверу. Это означает, что сервер успешно обработал запрос и вернул запрошенные данные.
        # Веб-страницы, которые возвращают код 200, отображаются без ошибок, и пользователи могут без проблем просматривать их.)
        # Атрибут status_code объекта Response содержит числовой код состояния ответа
        if otvet.status_code == 200:
            # Добавляем сайт в список
            # Метод append() списка добавляет элемент в конец списка
            sayte.append(sayt)
            # Выводим сообщение об успехе
            # Функция print() печатает аргументы на стандартный вывод
            # Ф-строка - это строка, в которой можно вставлять выражения в фигурных скобках
            print(f"Сайт {sayt} добавлен в список.")
        else:
            # Выводим сообщение об ошибке
            print(f"Сайт {sayt} недоступен или не существует. Попробуйте другой.")
    # Ловим исключение, если запрос не удался
    # Класс RequestException - это базовый класс для всех исключений, связанных с библиотекой requests
    except :
        # Выводим сообщение об ошибке
        # Переменная e содержит объект исключения, который можно преобразовать в строку
        print(f"Произошла ошибка при запросе к сайту {sayt}. Попробуйте другой.")

# Создаем пустой словарь для хранения информации
# Словарь - это изменяемая коллекция пар ключ-значение, где ключи должны быть уникальными и неизменяемыми
information = {}

# Итерируем по списку сайтов
# Цикл for проходит по каждому элементу итерируемого объекта (например, списка) и присваивает его переменной
for sayt in sayte:
    # Отправляем запрос и получаем ответ
    otvet = requests.get(sayt)
    # Извлекаем HTML-код из ответа
    # Атрибут text объекта Response содержит текстовое содержимое ответа
    html = otvet.text
    # Создаем объект Soup
    # Класс BeautifulSoup принимает HTML-код и парсер и возвращает объект Soup, который представляет собой дерево HTML-документа
    soup = BeautifulSoup(html, "html.parser")
    # Находим все элементы с тегом <p> (абзацы текста)
    # Вы можете изменить этот критерий поиска на другой
    # Метод find_all() объекта Soup принимает имя тега или другой фильтр и возвращает список всех элементов, удовлетворяющих этому фильтру
    elementi = soup.find_all("p")
    # Сохраняем элементы в словарь по ключу сайта
    # Словарь можно индексировать по ключу, чтобы получить или установить значение
    information[sayt] = elementi

# Вводим наш запрос
zapros = input("Введите ваш запрос: ")

# Итерируем по словарю информации
# Метод items() словаря возвращает пары ключ-значение в виде кортежей
for sayt, elementi in information.items():
    # Итерируем по элементам в списке
    for element in elementi:
        # Получаем текст из элемента
        # Метод get_text() объекта Soup возвращает текстовое содержимое элемента
        text = element.get_text()
        # Сравниваем текст с нашим запросом
        # Вы можете использовать другие методы сравнения, например, регулярные выражения
        # Оператор in проверяет, содержит ли строка подстроку
        if zapros in text:
            # Выводим адрес сайта и текст элемента
            print(f"Найдено на сайте {sayt}:")
            print(text)
            print()
