import os

from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from ....common.base_classes.views.base_model_list_widget import BaseDictModelListWidget

from ....common.views.model_edit.dict_model_edit_codename_widget import DictModelEditCodeNameWidget
from ....common.controllers.dict_biopsy_controller import ControllerDictBiopsy
from ....common.views.model_edit.model_edit_dialog import ModelEditDialog
from ....common.views.model_edit.dict_model_edit_codename_widget import DictModelEditCodeNameWidget

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'biopsys_list_widget.ui'))


class BiopsysListWidget(BaseDictModelListWidget, FORM_CLASS):
    """ Виджет. Список биопсий """

    __table_model = None  # Модель таблицы
    __controller_biopsys = None  # Контроллер справочника докторов

    def __init__(self, parent=None):
        """ Конструктор
        :param xml_provider: Провайдер данных xml
        :param parent: Родитель
        """

        print(": BiopsysListWidget.__init__()")

        super(BiopsysListWidget, self).__init__(parent)

        self.__init_table()

        self.__controller_biopsys = ControllerDictBiopsy()
        self.refresh()

    def __init_table(self):
        """ Инициализация таблицы данных """

        print(": BiopsysListWidget.__init_table()")

        self.__table_model = QStandardItemModel()

        self.__table_model.setHorizontalHeaderLabels(['Код', 'Наименование'])
        self.table.setModel(self.__table_model)

    def refresh(self):
        """Обновление списка биопсий"""

        print(": BiopsysListWidget.refresh()")

        self.__table_model.clear()
        self.__table_model.setHorizontalHeaderLabels(['Код', 'Наименование'])


        list_biopsys = self.__controller_biopsys.select_biopsys()

        print("list_biopsys=", list_biopsys)

        for row, biopsy in enumerate(list_biopsys):
            print("biopsy=", biopsy)

            item_code = QStandardItem(str(biopsy.code))
            print("item_code=", str(item_code))
            item_name = QStandardItem(biopsy.name)
            print("item_name=", item_name)

            self.__table_model.setItem(row, 0, item_code)
            self.__table_model.setItem(row, 1, item_name)

            print("self.__table_model=", self.__table_model)
        # self.__table_model.resizeColumnsToContents()

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def create_element(self):
        """ Добавление биопсии """

        print(": BiopsysListWidget.create_element()")
        try:
            edit_biopsy_widget = DictModelEditCodeNameWidget(parent=self, model=None)

            print("edit_biopsy_widget=", edit_biopsy_widget)

            edit_dlg = ModelEditDialog(edit_biopsy_widget)
            edit_dlg.show()
            result = edit_dlg.exec_()

            if result:
                biopsy = edit_dlg.get_model()
                print("biopsy=", biopsy)

                if self.__controller_biopsys.create_biopsy(biopsy=biopsy):
                    self.refresh()
        except Exception as e:
            print("e=", e)

    def update_element(self):
        """ Обновление биопсии """

        print(": BiopsysListWidget.update_element()")

        # biopsy = BiopsyModel(222, "2", "2", "2")
        curr_index = self.table.currentIndex()
        row = curr_index.row()
        col = curr_index.column()

        code = self.table.model().index(row, 0).data()

        biopsy = self.__controller_biopsys.get_biopsy(code)

        if not biopsy:
            return

        edit_biopsy_widget = DictModelEditCodeNameWidget(parent=self, model=biopsy)

        edit_dlg = ModelEditDialog(edit_biopsy_widget)
        edit_dlg.show()
        result = edit_dlg.exec_()

        if result:
            biopsy = edit_dlg.get_model()
            print("biopsy=", biopsy)

            if self.__controller_biopsys.update_biopsy(biopsy=biopsy):
                self.refresh()

    def delete_element(self):
        """ Удаление биопсии """

        print(": BiopsysListWidget.delete_element()")

        try:
            curr_index = self.table.currentIndex()

            row = curr_index.row()
            col = curr_index.column()

            code = self.table.model().index(row, 0).data()

            if self.__controller_biopsys.delete_biopsy(code):
                self.refresh()
        except Exception as e:
            print("e=", e)
