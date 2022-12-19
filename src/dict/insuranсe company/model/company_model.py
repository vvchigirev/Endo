from ....common.base_classes.models.base_dict_model import *


class CompanyModel(BaseDictModel):
    """ Модель. Страх. компания"""

    def __init__(self, code, name: str = ""):
        """ Конструктор
        :param code: Код
        :param name: Наименование
        """

        super().__init__(code, name=name)

    # region Свойства

    @property
    def code(self):
        """ Свойство. Код органа """
        return self.id

    # endregion
