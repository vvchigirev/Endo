import os

from PyQt5 import uic, QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from ....common.base_classes.views.base_model_edit_widget import BaseModelEditWidget
from ....common.base_classes.views.base_model_list_widget import BaseDictModelListWidget
from ....common.data.xml_data_provider import XmlDataProvider
from ....common.controllers.dict_nurse_controller import ControllerDictNurse
from ....common.views.model_edit.model_edit_dialog import ModelEditDialog
from .nurse_edit_widget import NurseEditWidget
from ..model.nurse_model import NurseModel


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'nurse_list_widget.ui'))


class NursesListWidget(BaseDictModelListWidget, FORM_CLASS):
    """ Виджет. Список мед сестер """

    __table_model = None            # Модель таблицы
    __controller_nurses = None     # Крнтроллер справочника докторов

    def __init__(self, parent=None):
        """ Конструктор
        :param parent: Родитель
        """

        print(": NurseListWidget.__init__()")

        super(NursesListWidget, self).__init__(parent)

        self.__init_table()

        self.__controller_nurses = ControllerDictNurse()
        self.refresh()

    def __init_table(self):
        """ Инициализация таблицы данных """

        self.__table_model = QStandardItemModel()

        # self.__table_model.verticalHeader().hide()
        # self.__table_model.setColumnCount(4)
        self.__table_model.setHorizontalHeaderLabels(['Код', 'Фамилия', 'Имя', 'Отчество'])

        # self.table.setSelectionMode(2)
        # self.table.setHorizontalHeaderLabels(('Код', 'Фамилия', 'Имя', 'Отчество'))
        self.table.setModel(self.__table_model)
        # self.table.verticalHeader().hide()
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        self.table.setSortingEnabled(True)
        self.table.sortByColumn(
            0, QtCore.Qt.AscendingOrder
            # 0, QtCore.Qt.DescendingOrder
        )

    def refresh(self):
        """Обновление списка мед сестер"""

        print(": NurseListWidget.refresh()")

        list_nurses = self.__controller_nurses.select_nurses()

        print("list_nurses=", list_nurses)

        for row, nurse in enumerate(list_nurses):
            item_code = QStandardItem(str(nurse.code))
            item_last_name = QStandardItem(nurse.last_name)
            item_first_name = QStandardItem(nurse.first_name)
            item_middle_name = QStandardItem(nurse.middle_name)

            self.__table_model.setItem(row, 0, item_code)
            self.__table_model.setItem(row, 1, item_last_name)
            self.__table_model.setItem(row, 2, item_first_name)
            self.__table_model.setItem(row, 3, item_middle_name)

        # self.__table_model.resizeColumnsToContents()

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def create_element(self):
        """ Добавление мед сестры """

        print(": NurseListWidget.create_element()")

        edit_nurse_widget = NurseEditWidget(parent=self, nurse=None)

        edit_dlg = ModelEditDialog(edit_nurse_widget)
        edit_dlg.show()
        result = edit_dlg.exec_()

        if result:
            nurse = edit_dlg.get_model()
            print("nurse=", nurse)

            if self.__controller_nurses.create_nurse(nurse=nurse):
                self.refresh()

    def update_element(self):
        """ Обновление мед сестры """

        print(": NurseListWidget.update_element()")

        curr_index = self.table.currentIndex()
        row = curr_index.row()
        col = curr_index.column()

        code = self.table.model().index(row, 0).data()

        nurse = self.__controller_nurses.get_nurse(code)

        if not nurse:
            return

        edit_nurse_widget = NurseEditWidget(parent=self, nurse=nurse)

        edit_dlg = ModelEditDialog(edit_nurse_widget)
        edit_dlg.show()
        result = edit_dlg.exec_()

        if result:
            nurse = edit_dlg.get_model()
            print("nurse=", nurse)

            if self.__controller_nurses.update_nurse(nurse=nurse):
                self.refresh()

    def delete_element(self):
        """ Удаление мед сестры """

        print(": NurseListWidget.delete_element()")

        curr_index = self.table.currentIndex()

        row = curr_index.row()
        col = curr_index.column()

        code = self.table.model().index(row, 0).data()

        if self.__controller_nurses.delete_nurse(code):
            self.refresh()
