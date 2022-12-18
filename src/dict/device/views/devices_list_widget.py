import os

from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from ....common.base_classes.views.base_model_list_widget import BaseDictModelListWidget

from ....common.views.model_edit.dict_model_edit_codename_widget import DictModelEditCodeNameWidget
from ....common.controllers.dict_device_controller import ControllerDictDevice
from ....common.views.model_edit.model_edit_dialog import ModelEditDialog
from ....common.views.model_edit.dict_model_edit_codename_widget import DictModelEditCodeNameWidget

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'devices_list_widget.ui'))


class DevicesListWidget(BaseDictModelListWidget, FORM_CLASS):
    """ Виджет. Список приборов """

    __table_model = None  # Модель таблицы
    __controller_devices = None  # Контроллер справочника докторов

    def __init__(self, parent=None):
        """ Конструктор
        :param xml_provider: Провайдер данных xml
        :param parent: Родитель
        """

        print(": DevicesListWidget.__init__()")

        super(DevicesListWidget, self).__init__(parent)

        self.__init_table()

        self.__controller_devices = ControllerDictDevice()
        self.refresh()

    def __init_table(self):
        """ Инициализация таблицы данных """

        print(": DevicesListWidget.__init_table()")

        self.__table_model = QStandardItemModel()

        self.__table_model.setHorizontalHeaderLabels(['Код', 'Наименование'])
        self.table.setModel(self.__table_model)

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

    # def set_data(self, list_devices):
    #     """Установка списка моделе приборов"""
    #
    #     print(": DocktorListWidget.set_data()")
    #     print("list_devices=", list_devices)
    #
    #     # self.__table_model.clear()
    #     self.__table_model.setRowCount(len(list_devices))
    #     # self.__table_model.setColumnCount(4)
    #     # self.__table_model.columns = ['ID', 'Наименование', 'order']
    #     # self.__table_model.setHorizontalHeaderLabels(['ID', 'Наименование', 'order'])
    #
    #     for row, device in enumerate(list_devices):
    #         item_code = QStandardItem(str(device.code))
    #         item_last_name = QStandardItem(device.last_name)
    #         item_first_name = QStandardItem(device.first_name)
    #         item_middle_name = QStandardItem(device.middle_name)
    #
    #         self.__table_model.setItem(row, 0, item_code)
    #         self.__table_model.setItem(row, 1, item_last_name)
    #         self.__table_model.setItem(row, 2, item_first_name)
    #         self.__table_model.setItem(row, 3, item_middle_name)

    def refresh(self):
        """Обновление списка приборов"""

        print(": DevicesListWidget.refresh()")

        self.__table_model.clear()
        self.__table_model.setHorizontalHeaderLabels(['Код', 'Наименование'])


        list_devices = self.__controller_devices.select_devices()

        print("list_devices=", list_devices)

        for row, device in enumerate(list_devices):
            print("device=", device)

            item_code = QStandardItem(str(device.code))
            print("item_code=", str(item_code))
            item_name = QStandardItem(device.name)
            print("item_name=", item_name)

            self.__table_model.setItem(row, 0, item_code)
            self.__table_model.setItem(row, 1, item_name)

            print("self.__table_model=", self.__table_model)
        # self.__table_model.resizeColumnsToContents()

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def create_element(self):
        """ Добавление прибора """

        print(": DevicesListWidget.create_element()")
        try:
            edit_device_widget = DictModelEditCodeNameWidget(parent=self, model=None)

            print("edit_device_widget=", edit_device_widget)

            edit_dlg = ModelEditDialog(edit_device_widget)
            edit_dlg.show()
            result = edit_dlg.exec_()

            if result:
                device = edit_dlg.get_model()
                print("device=", device)

                if self.__controller_devices.create_device(device=device):
                    self.refresh()
        except Exception as e:
            print("e=", e)

    def update_element(self):
        """ Обновление прибора """

        print(": DevicesListWidget.update_element()")

        # device = DeviceModel(222, "2", "2", "2")
        curr_index = self.table.currentIndex()
        row = curr_index.row()
        col = curr_index.column()

        code = self.table.model().index(row, 0).data()

        device = self.__controller_devices.get_device(code)

        if not device:
            return

        edit_device_widget = DictModelEditCodeNameWidget(parent=self, model=device)

        edit_dlg = ModelEditDialog(edit_device_widget)
        edit_dlg.show()
        result = edit_dlg.exec_()

        if result:
            device = edit_dlg.get_model()
            print("device=", device)

            if self.__controller_devices.update_device(device=device):
                self.refresh()

    def delete_element(self):
        """ Удаление прибора """

        print(": DevicesListWidget.delete_element()")

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
        try:
            curr_index = self.table.currentIndex()

            row = curr_index.row()
            col = curr_index.column()

            code = self.table.model().index(row, 0).data()

            if self.__controller_devices.delete_device(code):
                self.refresh()
        except Exception as e:
            print("e=", e)
