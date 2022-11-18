from typing import Any


class BaseModel:
    """ Базовый класс моделей """

    __id = None         # Идентификатор
    __is_delete = None  # Признак удаленности записи

    def __init__(self, id: Any = None):
        """ Конструктор
        :param id: Идентификатор"""

        self.__id = id
        self.__is_delete = False

    # region Свойства

    @property
    def id(self):
        """ Свойство. Идентификатор """

        return self.__id

    @property.setter
    def id(self, value):
        """ Свойство (установка). Идентификатор
        :param value: Присваемое значение
        """

        self.__id = value

    @property
    def is_delete(self):
        """ Свойство. Признак удаления
        :return:
        """
        return self.__is_delete

    # endregion

    def set_delete(self):
        """ Установка признака удаления """

        self.__is_delete = False
