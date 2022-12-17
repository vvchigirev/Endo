import xml.etree.ElementTree as ET


class BaseSections:
    """ Базовый класс для наименования xml секций """

    __group_name: str = ""
    __element_name: str = ""

    def __init__(self, el_group_name=None, el_name=None):
        """ Конструктор
        :param el_group_name: Наименование группы
        :param el_name: Наименование элемента
        """

        self.__group_name = el_group_name
        self.__element_name = el_name

    # region Свойства

    @property
    def group_name(self):
        """ Свойство. Имя группы """

        return self.__group_name

    @group_name.setter
    def group_name(self, value):
        """ Свойство (сетеер). Имя группы
        :param value: Устанавливаемое значение
        """

        self.__group_name = value

    @property
    def element_name(self):
        """ Свойство. Имя элемента """

        return self.__element_name

    @element_name.setter
    def element_name(self, value):
        """ Свойство (сеттер). Имя элемента """

        self.__element_name = value

    # endregion

    def __str__(self):
        s = ""
        s += "group_name= " + self.group_name + ", "
        s += "element_name= " + self.element_name

        return s
