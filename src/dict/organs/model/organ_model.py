from ....common.base_classes.models.base_dict_model import *


class OrganModel(BaseDictModel):
    """ Модель. Орган"""

    def __init__(self, code, organ_name: str = ""):
        """ Конструктор
        :param kode: Код
        :param name: Наименование
        """

        super().__init__(code, name=organ_name)

    @property
    def code(self):
        """ Свойство. Код органа """
    # endregion

