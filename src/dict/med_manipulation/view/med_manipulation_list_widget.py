import os

from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from ....common.base_classes.views.base_model_list_widget import BaseDictModelListWidget

from ....common.views.model_edit.dict_model_edit_codename_widget import DictModelEditCodeNameWidget
from ....common.controllers.dict_med_manipulation_controller import ControllerDictMedManipulation
from ....common.views.model_edit.model_edit_dialog import ModelEditDialog
from ....common.views.model_edit.dict_model_edit_codename_widget import DictModelEditCodeNameWidget

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'med_manipulation_list_widget.ui'))


class MedManipulationsListWidget(BaseDictModelListWidget, FORM_CLASS):
    """ Виджет. Список мед манипуляций """

    __table_model = None  # Модель таблицы
    __controller_med_manipulations = None  # Контроллер справочника докторов

    def __init__(self, parent=None):
        """ Конструктор
        :param xml_provider: Провайдер данных xml
        :param parent: Родитель
        """

        print(": MedManipulationsListWidget.__init__()")

        super(MedManipulationsListWidget, self).__init__(parent)

        self.__init_table()

        self.__controller_med_manipulations = ControllerDictMedManipulation()
        self.refresh()

    def __init_table(self):
        """ Инициализация таблицы данных """

        print(": MedManipulationsListWidget.__init_table()")

        self.__table_model = QStandardItemModel()

        self.__table_model.setHorizontalHeaderLabels(['Код', 'Наименование'])
        self.table.setModel(self.__table_model)

    def refresh(self):
        """Обновление списка мед манипуляций"""

        print(": MedManipulationsListWidget.refresh()")

        self.__table_model.clear()
        self.__table_model.setHorizontalHeaderLabels(['Код', 'Наименование'])


        list_med_manipulations = self.__controller_med_manipulations.select_med_manipulations()

        print("list_med_manipulations=", list_med_manipulations)

        for row, med_manipulation in enumerate(list_med_manipulations):
            print("med_manipulation=", med_manipulation)

            item_code = QStandardItem(str(med_manipulation.code))
            print("item_code=", str(item_code))
            item_name = QStandardItem(med_manipulation.name)
            print("item_name=", item_name)

            self.__table_model.setItem(row, 0, item_code)
            self.__table_model.setItem(row, 1, item_name)

            print("self.__table_model=", self.__table_model)
        # self.__table_model.resizeColumnsToContents()

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def create_element(self):
        """ Добавление мед манипуляцияа """

        print(": MedManipulationsListWidget.create_element()")
        try:
            edit_med_manipulation_widget = DictModelEditCodeNameWidget(parent=self, model=None)

            print("edit_med_manipulation_widget=", edit_med_manipulation_widget)

            edit_dlg = ModelEditDialog(edit_med_manipulation_widget)
            edit_dlg.show()
            result = edit_dlg.exec_()

            if result:
                med_manipulation = edit_dlg.get_model()
                print("med_manipulation=", med_manipulation)

                if self.__controller_med_manipulations.create_med_manipulation(med_manipulation=med_manipulation):
                    self.refresh()
        except Exception as e:
            print("e=", e)

    def update_element(self):
        """ Обновление мед манипуляцияа """

        print(": MedManipulationsListWidget.update_element()")

        # med_manipulation = MedManipulationModel(222, "2", "2", "2")
        curr_index = self.table.currentIndex()
        row = curr_index.row()
        col = curr_index.column()

        code = self.table.model().index(row, 0).data()

        med_manipulation = self.__controller_med_manipulations.get_med_manipulation(code)

        if not med_manipulation:
            return

        edit_med_manipulation_widget = DictModelEditCodeNameWidget(parent=self, model=med_manipulation)

        edit_dlg = ModelEditDialog(edit_med_manipulation_widget)
        edit_dlg.show()
        result = edit_dlg.exec_()

        if result:
            med_manipulation = edit_dlg.get_model()
            print("med_manipulation=", med_manipulation)

            if self.__controller_med_manipulations.update_med_manipulation(med_manipulation=med_manipulation):
                self.refresh()

    def delete_element(self):
        """ Удаление мед манипуляцияа """

        print(": MedManipulationsListWidget.delete_element()")

        try:
            curr_index = self.table.currentIndex()

            row = curr_index.row()
            col = curr_index.column()

            code = self.table.model().index(row, 0).data()

            if self.__controller_med_manipulations.delete_med_manipulation(code):
                self.refresh()
        except Exception as e:
            print("e=", e)
