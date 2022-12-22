from ....common.base_classes.models.base_dict_model import BaseDictModel
from typing import Any


class EndoModel(BaseDictModel):
    """ Модель. Доктор"""

    def __init__(self, code, name: str = "", uet: float = 0.0):
        """ Конструктор
        :param code: Код
        :param name: Наименование
        :param uet: УЕТ
        """

        super().__init__(code=code, name=name)
        self.__uet = uet

    # region Свойства

    # @property
    # def code(self):
    #     """ Свойство. Код врача """
    #     return self.id

    @property
    def uet(self):
        return self.__uet

    @uet.setter
    def uet(self, value):
        self.__uet = value

    # endregion

    def __str__(self):
        """ Строковое представление модели эндоскопии
        :return:
        """
        s = f'["EndoModel"] ({self.code}) {self.name} {self.__uet}'

        return s
