from ....common.base_classes.models.base_dict_model import *


class IEndoModel(BaseDictModel):
    """ Модель. Орган"""

    def __init__(self, code, name: str = ""):
        """ Конструктор
        :param code: Код
        :param name: Наименование
        """

        super().__init__(code, name=name)

    # region Свойства
    #
    # @property
    # def code(self):
    #     """ Свойство. Код прибора """
    #     return self.id

    # endregion
    def __str__(self):
        """Строковое представление модели приборов"""

        s = f'["IEndosModel"] ({self.code}) {self.name}'

        return s

