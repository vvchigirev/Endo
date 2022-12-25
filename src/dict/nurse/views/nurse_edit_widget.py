import os

from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox
from src.common.base_classes.views.base_model_edit_widget import BaseModelEditWidget
from ..model.nurse_model import NurseModel


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'nurse_edit_widget.ui'))


class NurseEditWidget(BaseModelEditWidget, FORM_CLASS):
    """Компонент. Редактирование мед сестры"""

    __nurse = None     # Моддель мед сестры для обработки

    def __init__(self, parent=None, nurse: NurseModel = None):
        """Конструктор"""

        print(": NurseEditWidget.__init__()")

        super(NurseEditWidget,self).__init__(parent)
        # self.setupUi(self)

        self.__nurse = nurse

        self.__prepare_ui()

    # region Свойства

    @property
    def nurse(self):
        """Модель - Мед сестра"""

        return self.__nurse

    # endregion

    def get_model(self):
        """ Получение подели из вложенного виджета """

        print(": NurseEditWidget.get_model()")

        self.__nurse = self.__get_value_fields()

        return self.__nurse

    def __prepare_ui(self):
        """ Подготовка элемента """

        print(": NurseEditWidget.__prepare_ui()")

        self.__set_fields()

        self.lineEditCode.textChanged.connect(self.__on_lineEditCode_text_changed)
        self.lineEditLastName.textChanged.connect(self.__on_lineEditLastName_text_changed)

    def __set_fields(self):
        """ Установка значений в поля ввода """

        print(": NurseEditWidget.__set_fields")

        print(self.__nurse)

        if self.__nurse:
            self.lineEditCode.setText(str(self.__nurse.code))
            self.lineEditLastName.setText(self.__nurse.last_name)
            self.lineEditFirstName.setText(self.__nurse.first_name)
            self.lineEditMiddleName.setText(self.__nurse.middle_name)

    def __get_value_fields(self):
        """ Получение введенные значения в полях ввода
        :return:
        """

        code = self.lineEditCode.text()
        last_name = self.lineEditLastName.text()
        first_name = self.lineEditFirstName.text()
        middle_name = self.lineEditMiddleName.text()

        nurse = NurseModel(code, last_name, first_name, middle_name)

        return nurse

    def check_input_values(self):
        """ Проверка введенных значений в поля ввода"""

        print(": NurseEditWidget.check_input_values()")

        s_fields = ""
        is_add_field = False
        if self.lineEditCode.text() == "":
            s_fields += "Код"
            is_add_field = True

        if self.lineEditLastName.text() == "":
            if is_add_field:
                s_fields += ", "
            s_fields += "Фамилия"
            is_add_field = True

        print("s_fields=", s_fields)
        if s_fields != "":
            message = "Следующие обязательнве поля не заполнены: " + s_fields
            print("message=", message)

            QMessageBox.critical(self, "Ошибка ", message, QMessageBox.Ok)
            return False

        return True

    def __on_lineEditCode_text_changed(self, value):
        print(": NurseEditWidget.__on_lineEditCode_text_changed()")
        print("value=", value)

        if value == "":
            self.lineEditCode.setStyleSheet("QLineEdit { background-color : #ffcdcf; }")
        else:
            # self.lineEditCode.setStyleSheet("QLineEdit { background-color : #f0f0f0; }")
            self.lineEditCode.setStyleSheet("QLineEdit { background-color : #ffffff; }")

    def __on_lineEditLastName_text_changed(self, value):
        print(": NurseEditWidget.__on_lineEditLastName_text_changed()")
        print("value=", value)

        if value == "":
            self.lineEditLastName.setStyleSheet("QLineEdit { background-color : #ffcdcf; }")
        else:
            # self.lineEditLastName.setStyleSheet("QLineEdit { background-color : #f0f0f0; }")
            self.lineEditLastName.setStyleSheet("QLineEdit { background-color : #ffffff; }")