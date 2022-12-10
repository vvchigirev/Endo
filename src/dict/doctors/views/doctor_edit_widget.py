import os

from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox
from src.common.base_classes.views.base_model_edit_widget import BaseModelEditWidget
from ..model.doctor_model import DoctorModel


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'doctor_edit_widget.ui'))


class DoctorEditWidget(BaseModelEditWidget, FORM_CLASS):
    """Компонент. Редактирование врача"""

    __doctor = None     # Моддель врача для обработки

    def __init__(self, parent=None, doctor: DoctorModel = None):
        """Конструктор"""

        print(": DoctorEditWidget.__init__()")

        super(DoctorEditWidget,self).__init__(parent)
        # self.setupUi(self)

        self.__doctor = doctor

        self.__prepare_ui()

    # region Свойства

    @property
    def doctor(self):
        """Модель - Врач"""

        return self.__doctor

    # endregion

    def get_model(self):
        """ Получение подели из вложенного виджета """

        print(": DoctorEditWidget.get_model()")

        self.__doctor = self.__get_value_fields()

        return self.__doctor

    def __prepare_ui(self):
        """ Подготовка элемента """

        print(": DoctorEditWidget.__prepare_ui()")

        self.__set_fields()

        self.lineEditCode.textChanged.connect(self.__on_lineEditCode_text_changed)
        self.lineEditLastName.textChanged.connect(self.__on_lineEditLastName_text_changed)

    def __set_fields(self):
        """ Установка значений в поля ввода """

        print(": DoctorEditWidget.__set_fields")

        print(self.__doctor)

        if self.__doctor:
            self.lineEditCode.setText(str(self.__doctor.code))
            self.lineEditLastName.setText(self.__doctor.last_name)
            self.lineEditFirstName.setText(self.__doctor.first_name)
            self.lineEditMiddleName.setText(self.__doctor.middle_name)

    def __get_value_fields(self):
        """ Получение введенные значения в полях ввода
        :return:
        """

        code = self.lineEditCode.text()
        last_name = self.lineEditLastName.text()
        first_name = self.lineEditFirstName.text()
        middle_name = self.lineEditMiddleName.text()

        doctor = DoctorModel(code, last_name, first_name, middle_name)

        return doctor

    def check_input_values(self):
        """ Проверка введенных значений в поля ввода"""

        print(": DoctorEditWidget.check_input_values()")

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
        print(": DoctorEditWidget.__on_lineEditCode_text_changed()")
        print("value=", value)

        if value == "":
            self.lineEditCode.setStyleSheet("QLineEdit { background-color : #ffcdcf; }")
        else:
            # self.lineEditCode.setStyleSheet("QLineEdit { background-color : #f0f0f0; }")
            self.lineEditCode.setStyleSheet("QLineEdit { background-color : #ffffff; }")

    def __on_lineEditLastName_text_changed(self, value):
        print(": DoctorEditWidget.__on_lineEditLastName_text_changed()")
        print("value=", value)

        if value == "":
            self.lineEditLastName.setStyleSheet("QLineEdit { background-color : #ffcdcf; }")
        else:
            # self.lineEditLastName.setStyleSheet("QLineEdit { background-color : #f0f0f0; }")
            self.lineEditLastName.setStyleSheet("QLineEdit { background-color : #ffffff; }")