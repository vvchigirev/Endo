import os

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem


from ....common.data.xml_data_provider import XmlDataProvider
from ....common.controllers.dict_doctor_controller import ControllerDictDoctor
from ..model.doctor_model import DoctorModel


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'doctors_list_widget.ui'))


class DocktorListWidget(QWidget, FORM_CLASS):
    """Компонент. Список врачей"""

    __table_model = None            # Модель таблицы
    __xml_provider = None
    __controller_doctors = None     # Крнтроллер справочника докторов

    def __init__(self, xml_provider: XmlDataProvider):
        """Конструктор"""

        print(": DocktorListWidget.__init__()")

        self.__xml_provider = xml_provider
        self.__controller_doctors = ControllerDictDoctor(self.__xml_provider)

        try:
            super(DocktorListWidget, self).__init__()
            self.setupUi(self)

            self.__table_model = QStandardItemModel()

            # self.__table_model.verticalHeader().hide()
            # self.__table_model.setColumnCount(4)
            self.__table_model.setHorizontalHeaderLabels(['Код', 'Фамилия', 'Имя', 'Отчество'])

            # self.table.setHorizontalHeaderLabels(('Код', 'Фамилия', 'Имя', 'Отчество'))
            self.table.setModel(self.__table_model)
            # self.table.verticalHeader().hide()
            self.table.resizeColumnsToContents()
            self.table.setSortingEnabled(True)
            self.table.sortByColumn(
                0, QtCore.Qt.AscendingOrder
                # 0, QtCore.Qt.DescendingOrder
            )

            self.refresh()
        except Exception as e:
            print("e=", e)

    # def set_data(self, list_doctors):
    #     """Установка списка моделе врачей"""
    #
    #     print(": DocktorListWidget.set_data()")
    #     print("list_doctors=", list_doctors)
    #
    #     # self.__table_model.clear()
    #     self.__table_model.setRowCount(len(list_doctors))
    #     # self.__table_model.setColumnCount(4)
    #     # self.__table_model.columns = ['ID', 'Наименование', 'order']
    #     # self.__table_model.setHorizontalHeaderLabels(['ID', 'Наименование', 'order'])
    #
    #     for row, doctor in enumerate(list_doctors):
    #         item_code = QStandardItem(str(doctor.code))
    #         item_last_name = QStandardItem(doctor.last_name)
    #         item_first_name = QStandardItem(doctor.first_name)
    #         item_middle_name = QStandardItem(doctor.middle_name)
    #
    #         self.__table_model.setItem(row, 0, item_code)
    #         self.__table_model.setItem(row, 1, item_last_name)
    #         self.__table_model.setItem(row, 2, item_first_name)
    #         self.__table_model.setItem(row, 3, item_middle_name)

    def refresh(self):
        """Обновление списка врачей"""

        print(": DocktorListWidget.refresh()")

        list_doctors = self.__controller_doctors.select_doctors()

        print("list_doctors=", list_doctors)

        for row, doctor in enumerate(list_doctors):
            item_code = QStandardItem(str(doctor.code))
            item_last_name = QStandardItem(doctor.last_name)
            item_first_name = QStandardItem(doctor.first_name)
            item_middle_name = QStandardItem(doctor.middle_name)

            self.__table_model.setItem(row, 0, item_code)
            self.__table_model.setItem(row, 1, item_last_name)
            self.__table_model.setItem(row, 2, item_first_name)
            self.__table_model.setItem(row, 3, item_middle_name)

        # self.__table_model.resizeColumnsToContents()
    def create_elements(self):
        """Добавление нового врача"""

        print(": DocktorListWidget.create_elements()")

    def update_element(self):
        """Обновление врача"""

        print(": DocktorListWidget.update_element()")

    def delete_element(self):
        """Удаление врача"""

        print(": DocktorListWidget.delete_element()")

        try:
            print("self.table=", self.table)
            print("self.table.selectedIndexes()=", self.table.selectedIndexes())
            # print("self.table.currentItem()= ", self.table.currentItem())
            index = self.table.selectedIndexes()["code"]
            print("index=", str(index))
            code = self.table.model().data(index)

            print("code=", str(code))



            # row = self.table.currentItem().row()
            # print("row=", row)
        except Exception as e:
            print("e=", e)



