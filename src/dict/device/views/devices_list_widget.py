import os

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from ....common.base_classes.views.base_dict_model_list_widget import BaseDictModelListWidget


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'devices_list_widget.ui'))


class DevicesListWidget(BaseDictModelListWidget, FORM_CLASS):
    """ Виджет. Список приборов """

    def __init__(self, parent=None):
        """ Конструктор
        :param parent: Родитель
        """

        print(": DevicesListWidget.__init__()")

        super(DevicesListWidget, self).__init__(parent)

        self.__init_table()
        self.refresh()

    def __init_table(self):
        """ Инициализация таблицы данных """

        self.__table_model = QStandardItemModel()
        self.__table_model.setHorizontalHeaderLabels(['Код', 'Наименование'])
        self.table.setModel(self.__table_model)

    def refresh(self):
        """Обновление списка Приборов"""

        print(": DevicesListWidget.refresh()")

    def update_element(self):
        """ Обновление врача """

        print(": DevicesListWidget.update_element()")