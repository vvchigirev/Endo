import xml.etree.ElementTree as ET


class BaseXmlElement:
    """ Базовый класс для xml структур"""

    __group_name = None
    __element_name = None

    def __init__(self):
        """ Конструктор """

        self.__group_name = None
        self.__element_name = None

    # region Свойства

    @property
    def group_name(self):
        """ Свойство. Имя группы """

        return self.__group_name

    @group_name.setter
    def group_name(self, value):
        """ Свойство (установка). Имя группы
        :param value: Устанавливаемое значение
        """

        self.__group_name = value

    @property
    def element_name(self):
        """ Свойство. Имя элемента """

        return self.__element_name

    @element_name.setter
    def element_name(self, value):
        """ Свойство (установка). Имя элемента """
        self.__element_name = value

    # endregion
