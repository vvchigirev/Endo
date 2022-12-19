from ....common.base_classes.models.base_dict_model import BaseDictModel
from typing import Any

class DoctorModel(BaseDictModel):
    """ Модель. Доктор"""

    def __init__(self, code, name: str = "", YET: Any = None):
        """ Конструктор
        :param code: Код
        :param name: Наименование
        :param YET: УЕТ
        """

        super().__init__(code, name=name)

        self.YET = YET

    # region Свойства

    @property
    def code(self):
        """ Свойство. Код врача """
        return self.id

    @property
    def YET(self):
        return self.YET

    @YET.setter
    def YET(self, value):
        self.YET =value

    # endregion

    def __str__(self):
        """ Строковое представление модели эндоскопии
        :return:
        """
        s = f'["EndoModel"] ({self.code}) {self.name} {self.YET}'

        return s
