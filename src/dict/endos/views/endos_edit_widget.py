import os

from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox
from src.common.base_classes.views.base_model_edit_widget import BaseModelEditWidget
from ..model.endo_model import EndoModel
from ....common.Exceptions.business_exception import BusinеssException


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'endos_edit_widget.ui'))


class EndoEditWidget(BaseModelEditWidget, FORM_CLASS):
    """Компонент. Редактирование эндоскопии"""

    __endo = None     # Моддель эндоскопии для обработки

    def __init__(self, parent=None, endo: EndoModel = None):
        """Конструктор"""

        print(": EndoEditWidget.__init__()")

        super(EndoEditWidget,self).__init__(parent)
        # self.setupUi(self)

        self.__endo = endo

        self.__prepare_ui()

    # region Свойства

    @property
    def endo(self):
        """Модель - Эндоскопия"""

        return self.__endo

    # endregion

    def get_model(self):
        """ Получение подели из вложенного виджета """

        print(": EndoEditWidget.get_model()")

        self.__endo = self.__get_value_fields()

        return self.__endo

    def __prepare_ui(self):
        """ Подготовка элемента """

        print(": EndoEditWidget.__prepare_ui()")

        self.__set_fields()

        self.lineEditCode.textChanged.connect(self.__on_lineEditCode_text_changed)
        self.lineEditName.textChanged.connect(self.__on_lineEditName_text_changed)

    def __set_fields(self):
        """ Установка значений в поля ввода """

        print(": EndoEditWidget.__set_fields")

        print(self.__endo)

        if self.__endo:
            self.lineEditCode.setText(str(self.__endo.code))
            self.lineEditName.setText(self.__endo.name)
            self.lineEditUet.setText(self.__endo.uet)

    def __get_value_fields(self):
        """ Получение введенные значения в полях ввода
        :return:
        """
        print(":__get_value_fields")

        code = self.lineEditCode.text()
        name = self.lineEditName.text()
        uet = 0
        try:
            uet = float(self.lineEditUet.text())
        except Exception as e:
            uet = 0
            print("В УЕТ только числа!")

        endo = EndoModel(code, name, uet)
        print("endo=", endo)


        return endo

    def check_input_values(self):
        """ Проверка введенных значений в поля ввода"""

        print(": EndoEditWidget.check_input_values()")

        s_fields = ""
        is_add_field = False
        if self.lineEditCode.text() == "":
            s_fields += "Код"
            is_add_field = True

        if self.lineEditName.text() == "":
            if is_add_field:
                s_fields += ", "
            s_fields += "Имя"
            is_add_field = True



        print("s_fields=", s_fields)
        if s_fields != "":
            message = "Следующие обязательные поля не заполнены: " + s_fields
            print("message=", message)

            QMessageBox.critical(self, "Ошибка ", message, QMessageBox.Ok)
            return False

        return True

    def __on_lineEditCode_text_changed(self, value):
        print(": EndoEditWidget.__on_lineEditCode_text_changed()")
        print("value=", value)

        if value == "":
            self.lineEditCode.setStyleSheet("QLineEdit { background-color : #ffcdcf; }")
        else:
            # self.lineEditCode.setStyleSheet("QLineEdit { background-color : #f0f0f0; }")
            self.lineEditCode.setStyleSheet("QLineEdit { background-color : #ffffff; }")

    def __on_lineEditName_text_changed(self, value):
        print(": EndoEditWidget.__on_lineEditName_text_changed()")
        print("value=", value)

        if value == "":
            self.lineEditName.setStyleSheet("QLineEdit { background-color : #ffcdcf; }")
        else:
            # self.lineEditLastName.setStyleSheet("QLineEdit { background-color : #f0f0f0; }")
            self.lineEditName.setStyleSheet("QLineEdit { background-color : #ffffff; }")