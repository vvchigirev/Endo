import os
from PyQt5 import uic, QtWidgets
from ...dict.doctors.views.doctor_edit import DoctorEditWidget


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'model_edit_dialog.ui'))


class ModelEditDialog(QtWidgets.QDialog, FORM_CLASS):
    """Диалог редактирования модели"""

    __show_widget = None    # Показываемый виджет

    def __init__(self, widget):
        """Конструктор"""

        print(": ModelEditDialog.__init__()")

        super(ModelEditDialog, self).__init__()
        self.setupUi(self)

        self.__show_widget = widget

        self.__prepare_ui()

    def __prepare_ui(self):
        """ Подготовка окна """

        print(": ModelEditDialog.__prepare_ui()")
        self.setModal(True)

        print("1")
        self.buttonBox.accepted.connect(self.__on_click_btn_accept)
        print("2")
        self.buttonBox.rejected.connect(self.close)

        print("3")
        print("self.__show_widget=", self.__show_widget)
        self.layoutContaner.addWidget(self.__show_widget)
        print("4")

    def __on_click_btn_accept(self):
        """ Обработчик события нажатия на кнопку 'OK' """

        print("ОК")
