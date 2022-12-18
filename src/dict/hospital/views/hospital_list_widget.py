import os

from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from ....common.base_classes.views.base_model_list_widget import BaseDictModelListWidget

from ....common.views.model_edit.dict_model_edit_codename_widget import DictModelEditCodeNameWidget
from ....common.controllers.dict_hospital_controller import ControllerDictHospital
from ....common.views.model_edit.model_edit_dialog import ModelEditDialog
from ....common.views.model_edit.dict_model_edit_codename_widget import DictModelEditCodeNameWidget

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'hospital_list_widget.ui'))


class HospitalsListWidget(BaseDictModelListWidget, FORM_CLASS):
    """ Виджет. Список больниц """

    __table_model = None  # Модель таблицы
    __controller_hospitals = None  # Контроллер справочника докторов

    def __init__(self, parent=None):
        """ Конструктор
        :param xml_provider: Провайдер данных xml
        :param parent: Родитель
        """

        print(": HospitalsListWidget.__init__()")

        super(HospitalsListWidget, self).__init__(parent)

        self.__init_table()

        self.__controller_hospitals = ControllerDictHospital()
        self.refresh()

    def __init_table(self):
        """ Инициализация таблицы данных """

        print(": HospitalsListWidget.__init_table()")

        try:
            self.__table_model = QStandardItemModel()

            self.__table_model.setHorizontalHeaderLabels(['Код', 'Наименование'])
            self.table.setModel(self.__table_model)
        except Exception as e:
            print("e=", e)


    def refresh(self):
        try:
            """Обновление списка больниц"""

            print(": HospitalsListWidget.refresh()")

            self.__table_model.clear()
            self.__table_model.setHorizontalHeaderLabels(['Код', 'Наименование'])


            list_hospitals = self.__controller_hospitals.select_hospitals()

            print("list_hospitals=", list_hospitals)

            for row, hospital in enumerate(list_hospitals):
                print("hospital=", hospital)

                item_code = QStandardItem(str(hospital.code))
                print("item_code=", str(item_code))
                item_name = QStandardItem(hospital.name)
                print("item_name=", item_name)

                self.__table_model.setItem(row, 0, item_code)
                self.__table_model.setItem(row, 1, item_name)

                print("self.__table_model=", self.__table_model)
            # self.__table_model.resizeColumnsToContents()

            self.table.resizeColumnsToContents()
            self.table.resizeRowsToContents()
        except Exception as e:
            print("e=", e)

    def create_element(self):
        """ Добавление больницы """

        print(": HospitalsListWidget.create_element()")
        try:
            edit_hospital_widget = DictModelEditCodeNameWidget(parent=self, model=None)

            print("edit_hospital_widget=", edit_hospital_widget)

            edit_dlg = ModelEditDialog(edit_hospital_widget)
            edit_dlg.show()
            result = edit_dlg.exec_()

            if result:
                hospital = edit_dlg.get_model()
                print("hospital=", hospital)

                if self.__controller_hospitals.create_hospital(hospital=hospital):
                    self.refresh()
        except Exception as e:
            print("e=", e)

    def update_element(self):
        """ Обновление больницы """

        print(": HospitalsListWidget.update_element()")

        # hospital = HospitalModel(222, "2", "2", "2")
        curr_index = self.table.currentIndex()
        row = curr_index.row()
        col = curr_index.column()

        code = self.table.model().index(row, 0).data()

        hospital = self.__controller_hospitals.get_hospital(code)

        if not hospital:
            return

        edit_hospital_widget = DictModelEditCodeNameWidget(parent=self, model=hospital)

        edit_dlg = ModelEditDialog(edit_hospital_widget)
        edit_dlg.show()
        result = edit_dlg.exec_()

        if result:
            hospital = edit_dlg.get_model()
            print("hospital=", hospital)

            if self.__controller_hospitals.update_hospital(hospital=hospital):
                self.refresh()

    def delete_element(self):
        """ Удаление больницы """

        print(": HospitalsListWidget.delete_element()")

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

            if self.__controller_hospitals.delete_hospital(code):
                self.refresh()
        except Exception as e:
            print("e=", e)
