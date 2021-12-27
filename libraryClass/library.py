from typing import Union

from libraryClass.library_inits.book import Book
from libraryClass.library_inits.reader import Reader


class Library:
    """
    creating class Library
    """
    def __init__(self,
                 books: list = None,
                 readers: list = None):

        self.__books = books if books else []
        self.__readers = readers if readers else []

    def add_book(self, title: str, author: str, year: int, book_id: int = None) -> str:
        """
        method is adding a book
        :param title:
        :param author:
        :param year:
        :param book_id:
        :return:
        """
        if book_id is not None:                                          #check if there is such a book in the library
            for book in self.__books:
                if book.get_id() == book_id:
                    return f'Error: book with id {book_id} already exists'

        self.__books.append(Book(title, author, year, book_id))           #added book to library
        return f'Done: book was successfully added to the library'

    def add_reader(self, name: str, surname: str, year: int, reader_id: int = None) -> str:
        if reader_id is not None:                                         #checking reader_id in Library
            for reader in self.__readers:
                if reader.get_id() == reader_id:
                    return f'Error: reader with id {reader_id} already exists'

        self.__readers.append(Reader(name, surname, year, reader_id))     #added to readers
        return f'Done: reader was successfully added to the library'

    def print_all_books(self):
        if not self.__books:
            print('There are no books in the library yet')
            return

        for book in self.__books:
            print(book)                                                  #printing book's list

    def print_available_books(self):
        for book in self.__books:
            if not book.get_reader_id():
                print(book)

    def print_all_readers(self):
        if not self.__readers:
            print('There are no readers in the library yet')
            return

        for reader in self.__readers:
            print(reader)                                                  #printing list of readers

    def print_sorted_book(self, sort: str = 'id', reverse: bool = False):
        if sort not in ['id', 'title', 'year']:
            print(f'Error: no sorting by {sort} field')
            return

        def get_sort_field(book: Book):                                    #sorting books on title, author, year
            if sort == 'id': return book.get_id()
            elif sort == 'title': return book.get_title()
            elif sort == 'year': return book.get_year()

        for book in sorted(self.__books, key=get_sort_field, reverse=reverse):
            print(book)

    def give_book(self, book_id: int, reader_id: int):                    # giving a book to reader
        book = self.__get_book_by_id(book_id)
        if not book:
            print(f'Error: book with id {book_id} is not in the library')
            return

        reader = self.__get_reader_by_id(reader_id)
        if not reader:
            print(f'Error: reader with id {reader_id} is not in the library')
            return

        if book.get_reader_id() is not None:
            print(f'Error: book with id {book_id} are out of stock')
            return

        book.set_reader_id(reader_id)
        print(f'Books with id {book_id} have been successfully issued to the reader with id {reader_id}')

    def return_book(self, book_id: int, reader_id: int):                #accept a book from a reader
        book = self.__get_book_by_id(book_id)
        if not book:
            print(f'Error: book with id {book_id} is not in the library')
            return

        reader = self.__get_reader_by_id(reader_id)
        if not reader:
            print(f'Error: reader with id {reader_id} is not in the library')
            return

        if book.get_reader_id() != reader.get_id():
            print(f'Error: book with id {book_id} is not '
                  f'in the possession of the reader '
                  f'{reader.get_name()} {reader.get_surname()}')
            return

        book.set_reader_id(None)
        print(f'Reader {reader.get_name()} {reader.get_surname()} '
              f'returned the book "{book.get_title()}" to the library')

    def __get_book_by_id(self, book_id: int) -> Union[Book, None]:
        """
            Function for getting a book by id from the list of books
        :param book_id: id of the book we want to get
        :return: obj Book (if books is exist); None (if books is None)
        """
        for book in self.__books:
            if book.get_id() == book_id:
                return book
        return None

    def __get_reader_by_id(self, reader_id: int) -> Union[Reader, None]:
        """
            The function of getting a reader by id from the list of readers
        :param reader_id: id reader
        :return: obj Reader (if the reader is in the library); None (if is not)
        """
        for reader in self.__readers:
            if reader.get_id() == reader_id:
                return reader
        return None
