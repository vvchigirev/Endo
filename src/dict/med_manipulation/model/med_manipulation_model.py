from ....common.base_classes.models.base_dict_model import *


class MedManipulationModel(BaseDictModel):
    """ Модель. Орган"""

    def __init__(self, code, name: str = ""):
        """ Конструктор
        :param code: Код
        :param name: Наименование
        """

        super().__init__(code, name=name)

    def __str__(self):
        """Строковое представление модели лечебных манипуляций"""

        s = f'["MedManipulationModel"] ({self.code}) {self.name}'

        return s

