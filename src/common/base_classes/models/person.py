from typing import Any

from .base_model import BaseModel


class Person(BaseModel):
    """ Базовая модель - Человек"""

    __last_name = None
    __first_name = None
    __middle_name = None

    def __init__(self, id: Any = None, last_name: str = "", first_name: str = "", middle_name: str = ""):
        """ Конструктор
        :param id: Идентификатор
        :param last_name: Фамилия
        :param first_name: Имя
        :param middle_name: Отчество
        """

        super().__init__(id)

        self.__last_name = last_name
        self.__first_name = first_name
        self.__middle_name = middle_name

    # region Свойства

    @property
    def last_name(self):
        """ Свойство. Фамилия """

        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        """ Свойство (установка). Фамилия
        :param value: Значение
        """

        self.__last_name = value

    @property
    def first_name(self):
        """ Свойство.Имя """

        return self.__last_name

    @first_name.setter
    def first_name(self, value):
        """  Свойство (установка).Имя
        :param value: значение
        """

        self.__last_name = value

    @property
    def middle_name(self):
        """ Свойство. Отчество
        :param value: Значение
        """

        return self.__middle_name

    @middle_name.setter
    def middle_name(self, value):
        """ Свойство (установка). Отчество
        :param value: Значение
        """

        self.__middle_name = value

    @property
    def fio(self):
        """ Свойство. ФИО """

        return self.__last_name + " " + self.first_name + " " + self.middle_name

    @property
    def fam_io(self):
        """ Свойство. Фамилия И.О."""

        return self.__last_name + " " + self.__first_name[0] + ". " + self.__middle_name[0] + "."

    # endregion
