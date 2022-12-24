import os

from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from ....common.base_classes.views.base_model_list_widget import BaseDictModelListWidget

from ....common.views.model_edit.dict_model_edit_codename_widget import DictModelEditCodeNameWidget
from ....common.controllers.dict_complication_controller import ControllerDictComplication
from ....common.views.model_edit.model_edit_dialog import ModelEditDialog
from ....common.views.model_edit.dict_model_edit_codename_widget import DictModelEditCodeNameWidget

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'complications_list_widget.ui'))


class ComplicationsListWidget(BaseDictModelListWidget, FORM_CLASS):
    """ Виджет. Список осложнений """

    __table_model = None  # Модель таблицы
    __controller_complications = None  # Контроллер справочника докторов

    def __init__(self, parent=None):
        """ Конструктор
        :param xml_provider: Провайдер данных xml
        :param parent: Родитель
        """

        print(": ComplicationsListWidget.__init__()")

        super(ComplicationsListWidget, self).__init__(parent)

        self.__init_table()

        self.__controller_complications = ControllerDictComplication()
        self.refresh()

    def __init_table(self):
        """ Инициализация таблицы данных """

        print(": ComplicationsListWidget.__init_table()")

        self.__table_model = QStandardItemModel()

        self.__table_model.setHorizontalHeaderLabels(['Код', 'Наименование'])
        self.table.setModel(self.__table_model)

    def refresh(self):
        """Обновление списка осложнений"""

        print(": ComplicationsListWidget.refresh()")

        self.__table_model.clear()
        self.__table_model.setHorizontalHeaderLabels(['Код', 'Наименование'])


        list_complications = self.__controller_complications.select_complications()

        print("list_complications=", list_complications)

        for row, complication in enumerate(list_complications):
            print("complication=", complication)

            item_code = QStandardItem(str(complication.code))
            print("item_code=", str(item_code))
            item_name = QStandardItem(complication.name)
            print("item_name=", item_name)

            self.__table_model.setItem(row, 0, item_code)
            self.__table_model.setItem(row, 1, item_name)

            print("self.__table_model=", self.__table_model)
        # self.__table_model.resizeColumnsToContents()

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def create_element(self):
        """ Добавление осложнения """

        print(": ComplicationsListWidget.create_element()")
        try:
            edit_complication_widget = DictModelEditCodeNameWidget(parent=self, model=None)

            print("edit_complication_widget=", edit_complication_widget)

            edit_dlg = ModelEditDialog(edit_complication_widget)
            edit_dlg.show()
            result = edit_dlg.exec_()

            if result:
                complication = edit_dlg.get_model()
                print("complication=", complication)

                if self.__controller_complications.create_complication(complication=complication):
                    self.refresh()
        except Exception as e:
            print("e=", e)

    def update_element(self):
        """ Обновление осложнения """

        print(": ComplicationsListWidget.update_element()")

        # complication = ComplicationModel(222, "2", "2", "2")
        curr_index = self.table.currentIndex()
        row = curr_index.row()
        col = curr_index.column()

        code = self.table.model().index(row, 0).data()

        complication = self.__controller_complications.get_complication(code)

        if not complication:
            return

        edit_complication_widget = DictModelEditCodeNameWidget(parent=self, model=complication)

        edit_dlg = ModelEditDialog(edit_complication_widget)
        edit_dlg.show()
        result = edit_dlg.exec_()

        if result:
            complication = edit_dlg.get_model()
            print("complication=", complication)

            if self.__controller_complications.update_complication(complication=complication):
                self.refresh()

    def delete_element(self):
        """ Удаление осложнения """

        print(": ComplicationsListWidget.delete_element()")

        try:
            curr_index = self.table.currentIndex()

            row = curr_index.row()
            col = curr_index.column()

            code = self.table.model().index(row, 0).data()

            if self.__controller_complications.delete_complication(code):
                self.refresh()
        except Exception as e:
            print("e=", e)
