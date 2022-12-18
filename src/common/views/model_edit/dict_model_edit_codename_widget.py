import os

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from ...base_classes.views.base_model_edit_widget import BaseModelEditWidget
from ...base_classes.models.base_dict_model import BaseDictModel

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'dict_model_edit_codename_widget.ui'))


class DictModelEditCodeNameWidget(BaseModelEditWidget, FORM_CLASS):
    """ Базовый виджет для редактирования моделей """

    __parent = None  # Родительский элемент
    __model:BaseDictModel = None  # Модель

    def __init__(self, parent, model):
        """ Конструктор
        :param parent: Родитель
        :param model: Модель
        """

        super(BaseModelEditWidget, self).__init__()
        self.setupUi(self)

        self.__model = model
        print("self.__model=", self.__model)
        self.__parent = parent
        self.__prepare_ui()

    # region Свойства
    @property
    def parent(self):
        """ Свойство. Родитель """

        return self.__parent
    # endregion

    def __prepare_ui(self):
        """ Подготовка элемента """

        print(": DictModelEditCodeNameWidget.__prepare_ui()")

        self.lineEditName.setFocus(True)
        self.__set_fields()


    def get_model(self):
        """ Получени модели """

        print(": BaseModelEditWidget.get_model()")

        model = BaseDictModel(code=self.lineEditCode.text(), name=self.lineEditName.text())

        return model

    def check_input_values(self):
        """ Проверка введенных значений """

        print("Метод check_input_values() не перегружен!")

        return True

    def get_value_fields(self):
        """ Получение """
        pass

    def __set_fields(self):
        """ Установка значений в поля ввода """

        print(": DictModelEditCodeNameWidget.__set_fields")

        print("self.__model=", self.__model)

        if self.__model:
            self.lineEditCode.setText(str(self.__model.code))
            self.lineEditName.setText(self.__model.name)
