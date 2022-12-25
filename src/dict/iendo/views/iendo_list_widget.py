import os

from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from ....common.base_classes.views.base_model_list_widget import BaseDictModelListWidget

from ....common.views.model_edit.dict_model_edit_codename_widget import DictModelEditCodeNameWidget
from ....common.controllers.dict_iendo_controller import ControllerDictIEndo
from ....common.views.model_edit.model_edit_dialog import ModelEditDialog
from ....common.views.model_edit.dict_model_edit_codename_widget import DictModelEditCodeNameWidget

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'iendo_list_widget.ui'))


class IEndosListWidget(BaseDictModelListWidget, FORM_CLASS):
    """ Виджет. Список приборов """

    __table_model = None  # Модель таблицы
    __controller_iendos = None  # Контроллер справочника докторов

    def __init__(self, parent=None):
        """ Конструктор
        :param xml_provider: Провайдер данных xml
        :param parent: Родитель
        """

        print(": IEndosListWidget.__init__()")

        super(IEndosListWidget, self).__init__(parent)

        self.__init_table()

        self.__controller_iendos = ControllerDictIEndo()
        self.refresh()

    def __init_table(self):
        """ Инициализация таблицы данных """

        print(": IEndosListWidget.__init_table()")

        self.__table_model = QStandardItemModel()

        self.__table_model.setHorizontalHeaderLabels(['Код', 'Наименование'])
        self.table.setModel(self.__table_model)

    def refresh(self):
        """Обновление списка приборов"""

        print(": IEndosListWidget.refresh()")

        self.__table_model.clear()
        self.__table_model.setHorizontalHeaderLabels(['Код', 'Наименование'])


        list_iendos = self.__controller_iendos.select_iendos()

        print("list_iendos=", list_iendos)

        for row, iendo in enumerate(list_iendos):
            print("iendo=", iendo)

            item_code = QStandardItem(str(iendo.code))
            print("item_code=", str(item_code))
            item_name = QStandardItem(iendo.name)
            print("item_name=", item_name)

            self.__table_model.setItem(row, 0, item_code)
            self.__table_model.setItem(row, 1, item_name)

            print("self.__table_model=", self.__table_model)
        # self.__table_model.resizeColumnsToContents()

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def create_element(self):
        """ Добавление прибора """

        print(": IEndosListWidget.create_element()")
        try:
            edit_iendo_widget = DictModelEditCodeNameWidget(parent=self, model=None)

            print("edit_iendo_widget=", edit_iendo_widget)

            edit_dlg = ModelEditDialog(edit_iendo_widget)
            edit_dlg.show()
            result = edit_dlg.exec_()

            if result:
                iendo = edit_dlg.get_model()
                print("iendo=", iendo)

                if self.__controller_iendos.create_iendo(iendo=iendo):
                    self.refresh()
        except Exception as e:
            print("e=", e)

    def update_element(self):
        """ Обновление прибора """

        print(": IEndosListWidget.update_element()")

        # iendo = IEndoModel(222, "2", "2", "2")
        curr_index = self.table.currentIndex()
        row = curr_index.row()
        col = curr_index.column()

        code = self.table.model().index(row, 0).data()

        iendo = self.__controller_iendos.get_iendo(code)

        if not iendo:
            return

        edit_iendo_widget = DictModelEditCodeNameWidget(parent=self, model=iendo)

        edit_dlg = ModelEditDialog(edit_iendo_widget)
        edit_dlg.show()
        result = edit_dlg.exec_()

        if result:
            iendo = edit_dlg.get_model()
            print("iendo=", iendo)

            if self.__controller_iendos.update_iendo(iendo=iendo):
                self.refresh()

    def delete_element(self):
        """ Удаление прибора """

        print(": IEndosListWidget.delete_element()")

        try:
            curr_index = self.table.currentIndex()

            row = curr_index.row()
            col = curr_index.column()

            code = self.table.model().index(row, 0).data()

            if self.__controller_iendos.delete_iendo(code):
                self.refresh()
        except Exception as e:
            print("e=", e)
