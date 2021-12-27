"""
Module for describing the "Book" entity
"""


class Book:
    def __init__(self,
                 title: str,
                 author: str,
                 year: int,
                 _id: int = None,
                 reader_id: int = None):

        self.__id = _id if _id is not None else int(id(self))
        self.__title = title
        self.__author = author
        self.__year = year
        self.__reader_id = reader_id

    def get_id(self):
        """
        method for returning book's id
        :return:
        """
        return self.__id

    def get_title(self):
        """
        method for returning book's title
        :return:
        """
        return self.__title

    def get_author(self):
        """
         method for returning book's author
        :return:
        """
        return self.__author

    def get_year(self):
        """
        method for returning book's year
        :return:
        """
        return self.__year

    def get_reader_id(self):
        """
         method for getting book's id
        :return:
        """
        return self.__reader_id

    def set_reader_id(self, reader_id: int):
        """
        method for setters __reader_id using setter
        :param reader_id:
        :return:
        """
        self.__reader_id = reader_id

    def __str__(self):
        """
        :return: str
        """
        return f'{self.__id}) "{self.__title}". {self.__author}, {self.__year}'












