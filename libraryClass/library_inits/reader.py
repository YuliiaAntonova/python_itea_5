"""
Module for describing the "Reader" entity

"""


class Reader:
    def __init__(self,
                 name: str,
                 surname: str,
                 year: int,
                 _id: int = None):

        self.__id = _id if _id is not None else int(id(self))
        self.__name = name
        self.__surname = surname
        self.__year = year

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_year(self):
        return self.__year

    def __str__(self):
        return f'{self.__id}) {self.__name} {self.__surname}, {self.__year}'