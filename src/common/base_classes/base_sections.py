import xml.etree.ElementTree as ET


class BaseSections:
    """ Базовый класс для наименования xml секций """

    _group_name: str = ""
    _element_name: str = ""

    def __init__(self):
        """ Конструктор """

        self._group_name = el_group_name
        self._element_name = el_name

    # region Свойства

    @property
    def group_name(self):
        """ Свойство. Имя группы """

        return self._group_name

    @group_name.setter
    def group_name(self, value):
        """ Свойство (установка). Имя группы
        :param value: Устанавливаемое значение
        """

        self._group_name = value

    @property
    def element_name(self):
        """ Свойство. Имя элемента """

        return self._element_name

    @element_name.setter
    def element_name(self, value):
        """ Свойство (установка). Имя элемента """

        self._element_name = value

    # endregion

    def __str__(self):
        s = ""
        s += "group_name= " + self.group_name + ", "
        s += "element_name= " + self.element_name


        return s