import os

from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox
from src.common.base_classes.views.base_model_edit_widget import BaseModelEditWidget
from ..model.organ_model import OrganModel


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'organ_edit_widget.ui'))


class OrganEditWidget(BaseModelEditWidget, FORM_CLASS):
    """Компонент. Редактирование органа"""

    __organ = None     # Моддель органа для обработки

    def __init__(self, parent=None, organ: OrganModel = None):
        """Конструктор"""

        print(": OrganEditWidget.__init__()")

        super(OrganEditWidget, self).__init__(parent)
        # self.setupUi(self)

        self.__organ = organ

        self.__prepare_ui()

        print(":End OrganEditWidget.__init__()")
    # region Свойства

    @property
    def organ(self):
        """Модель - Орган"""

        return self.__organ

    # endregion

    def get_model(self):
        """ Получение подели из вложенного виджета """

        print(": OrganEditWidget.get_model()")

        self.__organ = self.__get_value_fields()

        return self.__organ

    def __prepare_ui(self):
        """ Подготовка элемента """

        print(": OrganEditWidget.__prepare_ui()")

        self.__set_fields()

        self.lineEditCode.textChanged.connect(self.__on_lineEditCode_text_changed)
        self.lineEditName.textChanged.connect(self.__on_lineEditName_text_changed)

        print(":End OrganEditWidget.__prepare_ui()")

    def __set_fields(self):
        """ Установка значений в поля ввода """

        print(": OrganEditWidget.__set_fields")

        print(self.__organ)

        if self.__organ:
            self.lineEditCode.setText(str(self.__organ.code))
            self.lineEditName.setText(self.__organ.name)

    def __get_value_fields(self):
        """ Получение введенные значения в полях ввода
        :return:
        """

        code = self.lineEditCode.text()
        name = self.lineEditName.text()

        organ = OrganModel(code, name)

        return organ

    def check_input_values(self):
        """ Проверка введенных значений в поля ввода"""

        print(": OrganEditWidget.check_input_values()")

        s_fields = ""
        is_add_field = False
        if self.lineEditCode.text() == "":
            s_fields += "Код"
            is_add_field = True

        if self.lineEditName.text() == "":
            if is_add_field:
                s_fields += ", "
            s_fields += "Наименование"
            is_add_field = True

        print("s_fields=", s_fields)
        if s_fields != "":
            message = "Следующие обязательнве поля не заполнены: " + s_fields
            print("message=", message)

            QMessageBox.critical(self, "Ошибка ", message, QMessageBox.Ok)
            return False

        return True

    def __on_lineEditCode_text_changed(self, value):
        print(": OrganEditWidget.__on_lineEditCode_text_changed()")
        print("value=", value)

        if value == "":
            self.lineEditCode.setStyleSheet("QLineEdit { background-color : #ffcdcf; }")
        else:
            # self.lineEditCode.setStyleSheet("QLineEdit { background-color : #f0f0f0; }")
            self.lineEditCode.setStyleSheet("QLineEdit { background-color : #ffffff; }")

    def __on_lineEditName_text_changed(self, value):
        print(": OrganEditWidget.__on_lineEditName_text_changed()")
        print("value=", value)

        if value == "":
            self.lineEditName.setStyleSheet("QLineEdit { background-color : #ffcdcf; }")
        else:
            # self.lineEditName.setStyleSheet("QLineEdit { background-color : #f0f0f0; }")
            self.lineEditName.setStyleSheet("QLineEdit { background-color : #ffffff; }")