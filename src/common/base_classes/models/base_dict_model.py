from typing import Any
from src.common.base_classes.models.base_model import BaseModel


class BaseDictModel(BaseModel):
    """ Модель. Орган """

    __name = None  # Наименование

    def __init__(self, code: Any = None, name: str = ""):
        """ Конструктор
        :param code: Идентификатор
        :param name: Наименование
        """

        super().__init__(code)

        self.__name = name

    @property
    def name(self):
        """ Свойство. Наименование """

        return self.__name

    @name.setter
    def name(self, value):
        """  Свойство (установка).Наименование
        :param value: значение
        """

        self.__name = value

    @property
    def code(self):
        """ Свойство. Код """
        return self.id

    def __str__(self):
        return f"[BaseDictModel] ({self.id}) {self.__name}"
