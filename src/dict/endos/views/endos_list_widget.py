import os

from PyQt5 import uic, QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from ....common.base_classes.views.base_model_list_widget import BaseDictModelListWidget
from ....common.controllers.dict_endo_controller import ControllerDictEndo
from ....common.views.model_edit.model_edit_dialog import ModelEditDialog
from .endos_edit_widget import EndoEditWidget

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'endos_list_widget.ui'))


class EndosListWidget(BaseDictModelListWidget, FORM_CLASS):
    """ Виджет. Список эндоскопий """

    __table_model = None            # Модель таблицы
    __controller_endos = None     # Крнтроллер справочника докторов

    def __init__(self, parent=None):
        """ Конструктор
        :param parent: Родитель
        """

        print(": DocktorListWidget.__init__()")

        super(EndosListWidget, self).__init__(parent)

        self.__init_table()

        self.__controller_endos = ControllerDictEndo()
        self.refresh()

    def __init_table(self):
        """ Инициализация таблицы данных """

        self.__table_model = QStandardItemModel()

        self.__table_model.setHorizontalHeaderLabels(['Код', 'Наименование', 'УЕТ'])

        self.table.setModel(self.__table_model)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        self.table.setSortingEnabled(True)
        self.table.sortByColumn(
            0, QtCore.Qt.AscendingOrder
        )

    def refresh(self):
        """Обновление списка эндоскопий"""

        self.__table_model.clear()

        print(": DocktorListWidget.refresh()")

        list_endos = self.__controller_endos.select_endos()

        print("list_endos=", list_endos)

        for row, endo in enumerate(list_endos):
            item_code = QStandardItem(str(endo.code))
            print("endo.name=", endo.name)
            item_name = QStandardItem(str(endo.name))
            print("item_name=", item_name)
            item_uet = QStandardItem(str(endo.uet))

            self.__table_model.setItem(row, 0, item_code)
            self.__table_model.setItem(row, 1, item_name)
            self.__table_model.setItem(row, 2, item_uet)

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def create_element(self):
        """ Добавление эндоскопии """

        print(": EndoListWidget.create_element()")
        try:
            edit_endo_widget = EndoEditWidget(parent=self, endo=None)

            edit_dlg = ModelEditDialog(edit_endo_widget)
            edit_dlg.show()
            result = edit_dlg.exec_()

            if result:
                endo = edit_dlg.get_model()
                print("endo=", endo)

                if self.__controller_endos.create_endo(endo=endo):
                    self.refresh()
        except Exception as e:
            print("e=", e)

    def update_element(self):
        """ Обновление эндоскопии """

        print(": DocktorListWidget.update_element()")

        curr_index = self.table.currentIndex()
        row = curr_index.row()
        col = curr_index.column()

        code = self.table.model().index(row, 0).data()

        endo = self.__controller_endos.get_endo(code)

        if not endo:
            return

        edit_endo_widget = EndoEditWidget(parent=self, endo=endo)

        edit_dlg = ModelEditDialog(edit_endo_widget)
        edit_dlg.show()
        result = edit_dlg.exec_()

        if result:
            endo = edit_dlg.get_model()
            print("endo=", endo)

            if self.__controller_endos.update_endo(endo=endo):
                self.refresh()

    def delete_element(self):
        """ Удаление эндоскопии """

        print(": DocktorListWidget.delete_element()")

        curr_index = self.table.currentIndex()

        row = curr_index.row()
        col = curr_index.column()

        code = self.table.model().index(row, 0).data()

        if self.__controller_endos.delete_endo(code):
            self.refresh()
