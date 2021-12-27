from libraryClass.library import Library

lib = Library()

lib.add_book('Изучаем Python. Программирование игр, визуализация данных, веб-приложения', 'Эрик Мэтиз', 2017)
lib.add_book('Изучаем программирование на Python', 'Пол Бэрри', 2019)
lib.add_book('Изучаем Python', 'Марк Лутц', 2009)

lib.print_available_books()
print()

lib.add_reader('Ivan', 'Petrov', 1990)
lib.print_all_readers()
print()

id_reader = int(input('Enter reader id: '))
id_book = int(input('Enter book id: '))
lib.give_book(id_book, id_reader)

lib.print_available_books()
print()

lib.return_book(id_book, id_reader)

lib.print_available_books()
print()
