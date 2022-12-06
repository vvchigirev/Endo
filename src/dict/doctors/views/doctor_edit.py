import os

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from ..model.doctor_model import DoctorModel


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'doctor_edit.ui'))


class DoctorEditWidget(QWidget, FORM_CLASS):
    """Компонент. Редактирование врача"""

    def __init__(self):
        """Конструктор"""

        print(": DoctorEditWidget.__init__()")

        super(DoctorEditWidget,self).__init__()
        self.setupUi(self)

        print("1")
        self.__prepare_ui()
        print("2")

    def __prepare_ui(self):
        """ Подготовка элемента """

        print(": DoctorEditWidget.__prepare_ui()")

        self.lineEditCode.textChanged.connect(self.__on_lineEditCode_text_changed)
        self.lineEditLastName.textChanged.connect(self.__on_lineEditLastName_text_changed)

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

