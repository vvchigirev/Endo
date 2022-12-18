import os

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from ....common.base_classes.views.base_model_edit_widget import BaseModelEditWidget
from ....common.base_classes.views.base_model_list_widget import BaseDictModelListWidget
from ....common.data.xml_data_provider import XmlDataProvider
from ....common.controllers.dict_organ_controller import ControllerDictOrgan
from ....common.views.model_edit.model_edit_dialog import ModelEditDialog
from .organ_edit_widget import OrganEditWidget
from ..model.organ_model import OrganModel


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'organ_list_widget.ui'))


class OrgansListWidget(BaseDictModelListWidget, FORM_CLASS):
    """ Виджет. Список органов """

    __table_model = None            # Модель таблицы
    __xml_provider = None
    __controller_organs = None     # Контроллер справочника докторов

    def __init__(self, xml_provider: XmlDataProvider, parent=None):
        """ Конструктор
        :param xml_provider: Провайдер данных xml
        :param parent: Родитель
        """

        print(": OrgansListWidget.__init__()")

        super(OrgansListWidget, self).__init__(parent)

        self.__xml_provider = xml_provider
        self.__controller_organs = ControllerDictOrgan(self.__xml_provider)

        try:
            print("xxx")

            # # super(OrgansListWidget, self).__init__()
            # # self.setupUi(self)
            # print("- 1")
            # self.__table_model = QStandardItemModel()
            #
            # self.__table_model.setHorizontalHeaderLabels(['Код', 'Наименование'])
            #
            # print("- 2")
            #
            # self.table.setModel(self.__table_model)
            # # self.table.verticalHeader().hide()
            # print("- 3")
            # self.table.resizeColumnsToContents()
            # self.table.resizeRowsToContents()
            # self.table.setSortingEnabled(True)
            # self.table.sortByColumn(
            #     0, QtCore.Qt.AscendingOrder
            #     # 0, QtCore.Qt.DescendingOrder
            # )
            #
            # self.refresh()
        except Exception as e:
            print("e=", e)

    # def set_data(self, list_organs):
    #     """Установка списка моделе органов"""
    #
    #     print(": DocktorListWidget.set_data()")
    #     print("list_organs=", list_organs)
    #
    #     # self.__table_model.clear()
    #     self.__table_model.setRowCount(len(list_organs))
    #     # self.__table_model.setColumnCount(4)
    #     # self.__table_model.columns = ['ID', 'Наименование', 'order']
    #     # self.__table_model.setHorizontalHeaderLabels(['ID', 'Наименование', 'order'])
    #
    #     for row, organ in enumerate(list_organs):
    #         item_code = QStandardItem(str(organ.code))
    #         item_last_name = QStandardItem(organ.last_name)
    #         item_first_name = QStandardItem(organ.first_name)
    #         item_middle_name = QStandardItem(organ.middle_name)
    #
    #         self.__table_model.setItem(row, 0, item_code)
    #         self.__table_model.setItem(row, 1, item_last_name)
    #         self.__table_model.setItem(row, 2, item_first_name)
    #         self.__table_model.setItem(row, 3, item_middle_name)

    def refresh(self):
        """Обновление списка органов"""


        print(": OrgansListWidget.refresh()")

        list_organs = self.__controller_organs.select_organs()

        print("list_organs=", list_organs)

        for row, organ in enumerate(list_organs):
            item_code = QStandardItem(str(organ.code))
            item_name = QStandardItem(organ.name)

            self.__table_model.setItem(row, 0, item_code)
            self.__table_model.setItem(row, 1, item_name)

        # self.__table_model.resizeColumnsToContents()

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def create_element(self):
        """ Добавление органа """

        print(": OrgansListWidget.create_element()")

        edit_organ_widget = OrganEditWidget(parent=self, organ=None)

        edit_dlg = ModelEditDialog(edit_organ_widget)
        edit_dlg.show()
        result = edit_dlg.exec_()

        if result:
            organ = edit_dlg.get_model()
            print("organ=", organ)

            if self.__controller_organ.create_organ(organ=organ):
                self.refresh()

    def update_element(self):
        """ Обновление органа """

        print(": OrgansListWidget.update_element()")

        # organ = OrganModel(222, "2", "2", "2")
        curr_index = self.table.currentIndex()
        row = curr_index.row()
        col = curr_index.column()

        code = self.table.model().index(row, 0).data()

        organ = self.__controller_organs.get_organ(code)

        if not organ:
            return

        edit_organ_widget = OrganEditWidget(parent=self, organ=organ)

        edit_dlg = ModelEditDialog(edit_organ_widget)
        edit_dlg.show()
        result = edit_dlg.exec_()

        if result:
            organ = edit_dlg.get_model()
            print("organ=", organ)

            if self.__controller_organs.update_organ(organ=organ):
                self.refresh()

    def delete_element(self):
        """ Удаление органа """

        print(": OrgansListWidget.delete_element()")

        # try:
        #     print("self.table=", self.table)
        #     print("self.table.selectedIndexes()=", self.table.selectedIndexes())
        #     # print("self.table.currentItem()= ", self.table.currentItem())
        #     index = self.table.selectedIndexes()["code"]
        #     print("index=", str(index))
        #     code = self.table.model().data(index)
        #
        #     print("code=", str(code))
        #
        #     print("self.table.currentIndex()=", self.table.currentIndex())
        #
        #
        #
        #     # row = self.table.currentItem().row()
        #     # print("row=", row)
        # except Exception as e:
        #     print("e=", e)

        curr_index = self.table.currentIndex()

        row = curr_index.row()
        col = curr_index.column()

        code = self.table.model().index(row, 0).data()

        if self.__controller_organ.delete_organ(code):
            self.refresh()


