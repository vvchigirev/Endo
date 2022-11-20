from ....common.base_classes.models.base_dict_model import *


class DeviceModel(BaseDictModel):
    """ Модель. Орган"""

    def __init__(self, code, name: str = ""):
        """ Конструктор
        :param code: Код
        :param name: Наименование
        """

        super().__init__(code, name=name)

    # region Свойства
    @property
    def code(self):
        """ Свойство. Код инструмента """
        return self.id
    # endregion
