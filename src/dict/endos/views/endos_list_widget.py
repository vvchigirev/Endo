import os

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QWidget

from ....common.base_classes.views.base_dict_model_list_widget import BaseDictModelListWidget


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'endos_list_widget.ui'))


class EndosListWidget(BaseDictModelListWidget, FORM_CLASS):
    """ Виджет. Список эндоскопий """

    def __init__(self, parent=None):
        """ Конструктор
        :param xml_provider: Провайдер данных xml
        :param parent: Родитель
        """

        try:

            print(": EndoskopsListWidget.__init__()")

            super(EndosListWidget, self).__init__(parent)

        except Exception as e:
            print("e=", e)
