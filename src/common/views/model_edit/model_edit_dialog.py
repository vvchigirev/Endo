import os
from PyQt5 import uic, QtWidgets
from src.common.base_classes.views.base_model_edit_widget import BaseModelEditWidget

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'model_edit_dialog.ui'))


class ModelEditDialog(QtWidgets.QDialog, FORM_CLASS):
    """Диалог редактирования модели"""

    __show_widget: BaseModelEditWidget = None    # Показываемый виджет

    def __init__(self, widget: BaseModelEditWidget):
        """Конструктор"""

        print(": ModelEditDialog.__init__()")

        super(ModelEditDialog, self).__init__()
        self.setupUi(self)

        self.__show_widget = widget

        self.__prepare_ui()

    def get_model(self):
        """ Получение подели из вложенного виджета """

        print(": BaseModelEditWidget.get_model()")

        model = self.__show_widget.get_model()

        print("model=", model)
        return model

    def __prepare_ui(self):
        """ Подготовка окна """

        print(": ModelEditDialog.__prepare_ui()")

        self.setModal(True)
        self.setWindowTitle("Привет")

        self.buttonBox.accepted.connect(self.__on_click_btn_accept)
        self.buttonBox.rejected.connect(self.close)

        print("self.__show_widget=", self.__show_widget)
        self.layoutContaner.addWidget(self.__show_widget)

    def __on_click_btn_accept(self):
        """ Обработчик события нажатия на кнопку 'OK' """

        print("ОК")

    def accept(self):
        """ Событие положительного закрытия формы """

        print(": ModelEditDialog.accept()")

        if self.__show_widget.check_input_values():
            super(ModelEditDialog, self).accept()
        else:
            return