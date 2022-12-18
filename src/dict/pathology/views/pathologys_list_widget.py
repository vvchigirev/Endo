import os

from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from ....common.base_classes.views.base_model_list_widget import BaseDictModelListWidget

from ....common.views.model_edit.dict_model_edit_codename_widget import DictModelEditCodeNameWidget
from ....common.controllers.dict_pathology_controller import ControllerDictPathology
from ....common.views.model_edit.model_edit_dialog import ModelEditDialog
from ....common.views.model_edit.dict_model_edit_codename_widget import DictModelEditCodeNameWidget

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'pathologys_list_widget.ui'))


class PathologysListWidget(BaseDictModelListWidget, FORM_CLASS):
    """ Виджет. Список патологий """

    __table_model = None  # Модель таблицы
    __controller_pathologys = None  # Контроллер справочника докторов

    def __init__(self, parent=None):
        """ Конструктор
        :param xml_provider: Провайдер данных xml
        :param parent: Родитель
        """

        print(": PathologysListWidget.__init__()")

        super(PathologysListWidget, self).__init__(parent)

        self.__init_table()

        self.__controller_pathologys = ControllerDictPathology()
        self.refresh()

    def __init_table(self):
        """ Инициализация таблицы данных """

        print(": PathologysListWidget.__init_table()")

        self.__table_model = QStandardItemModel()

        self.__table_model.setHorizontalHeaderLabels(['Код', 'Наименование'])
        self.table.setModel(self.__table_model)

    def refresh(self):
        """Обновление списка патологий"""

        print(": PathologysListWidget.refresh()")

        self.__table_model.clear()
        self.__table_model.setHorizontalHeaderLabels(['Код', 'Наименование'])


        list_pathologys = self.__controller_pathologys.select_pathologys()

        print("list_pathologys=", list_pathologys)

        for row, pathology in enumerate(list_pathologys):
            print("pathology=", pathology)

            item_code = QStandardItem(str(pathology.code))
            print("item_code=", str(item_code))
            item_name = QStandardItem(pathology.name)
            print("item_name=", item_name)

            self.__table_model.setItem(row, 0, item_code)
            self.__table_model.setItem(row, 1, item_name)

            print("self.__table_model=", self.__table_model)
        # self.__table_model.resizeColumnsToContents()

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def create_element(self):
        """ Добавление патологии """

        print(": PathologysListWidget.create_element()")
        try:
            edit_pathology_widget = DictModelEditCodeNameWidget(parent=self, model=None)

            print("edit_pathology_widget=", edit_pathology_widget)

            edit_dlg = ModelEditDialog(edit_pathology_widget)
            edit_dlg.show()
            result = edit_dlg.exec_()

            if result:
                pathology = edit_dlg.get_model()
                print("pathology=", pathology)

                if self.__controller_pathologys.create_pathology(pathology=pathology):
                    self.refresh()
        except Exception as e:
            print("e=", e)

    def update_element(self):
        """ Обновление патологии """

        print(": PathologysListWidget.update_element()")

        # pathology = PathologyModel(222, "2", "2", "2")
        curr_index = self.table.currentIndex()
        row = curr_index.row()
        col = curr_index.column()

        code = self.table.model().index(row, 0).data()

        pathology = self.__controller_pathologys.get_pathology(code)

        if not pathology:
            return

        edit_pathology_widget = DictModelEditCodeNameWidget(parent=self, model=pathology)

        edit_dlg = ModelEditDialog(edit_pathology_widget)
        edit_dlg.show()
        result = edit_dlg.exec_()

        if result:
            pathology = edit_dlg.get_model()
            print("pathology=", pathology)

            if self.__controller_pathologys.update_pathology(pathology=pathology):
                self.refresh()

    def delete_element(self):
        """ Удаление патологии """

        print(": PathologysListWidget.delete_element()")

        try:
            curr_index = self.table.currentIndex()

            row = curr_index.row()
            col = curr_index.column()

            code = self.table.model().index(row, 0).data()

            if self.__controller_pathologys.delete_pathology(code):
                self.refresh()
        except Exception as e:
            print("e=", e)
