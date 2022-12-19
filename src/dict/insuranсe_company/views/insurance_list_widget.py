import os

from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from ....common.base_classes.views.base_model_list_widget import BaseDictModelListWidget

from ....common.views.model_edit.dict_model_edit_codename_widget import DictModelEditCodeNameWidget
from ....common.controllers.dict_company_controller import ControllerDictCompany
from ....common.views.model_edit.model_edit_dialog import ModelEditDialog
from ....common.views.model_edit.dict_model_edit_codename_widget import DictModelEditCodeNameWidget

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'companys_list_widget.ui'))


class CompanysListWidget(BaseDictModelListWidget, FORM_CLASS):
    """ Виджет. Список страховых компаний """

    __table_model = None  # Модель таблицы
    __controller_companys = None  # Контроллер справочника докторов

    def __init__(self, parent=None):
        """ Конструктор
        :param xml_provider: Провайдер данных xml
        :param parent: Родитель
        """

        print(": CompanysListWidget.__init__()")

        super(CompanysListWidget, self).__init__(parent)

        self.__init_table()

        self.__controller_companys = ControllerDictCompany()
        self.refresh()

    def __init_table(self):
        """ Инициализация таблицы данных """

        print(": CompanysListWidget.__init_table()")

        self.__table_model = QStandardItemModel()

        self.__table_model.setHorizontalHeaderLabels(['Код', 'Наименование'])
        self.table.setModel(self.__table_model)

    def refresh(self):
        """Обновление списка страховых компаний"""

        print(": CompanysListWidget.refresh()")

        self.__table_model.clear()
        self.__table_model.setHorizontalHeaderLabels(['Код', 'Наименование'])


        list_companys = self.__controller_companys.select_companys()

        print("list_companys=", list_companys)

        for row, company in enumerate(list_companys):
            print("company=", company)

            item_code = QStandardItem(str(company.code))
            print("item_code=", str(item_code))
            item_name = QStandardItem(company.name)
            print("item_name=", item_name)

            self.__table_model.setItem(row, 0, item_code)
            self.__table_model.setItem(row, 1, item_name)

            print("self.__table_model=", self.__table_model)
        # self.__table_model.resizeColumnsToContents()

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def create_element(self):
        """ Добавление страховой компании """

        print(": CompanysListWidget.create_element()")
        try:
            edit_company_widget = DictModelEditCodeNameWidget(parent=self, model=None)

            print("edit_company_widget=", edit_company_widget)

            edit_dlg = ModelEditDialog(edit_company_widget)
            edit_dlg.show()
            result = edit_dlg.exec_()

            if result:
                company = edit_dlg.get_model()
                print("company=", company)

                if self.__controller_companys.create_company(company=company):
                    self.refresh()
        except Exception as e:
            print("e=", e)

    def update_element(self):
        """ Обновление страховой компании """

        print(": CompanysListWidget.update_element()")

        # company = CompanyModel(222, "2", "2", "2")
        curr_index = self.table.currentIndex()
        row = curr_index.row()
        col = curr_index.column()

        code = self.table.model().index(row, 0).data()

        company = self.__controller_companys.get_company(code)

        if not company:
            return

        edit_company_widget = DictModelEditCodeNameWidget(parent=self, model=company)

        edit_dlg = ModelEditDialog(edit_company_widget)
        edit_dlg.show()
        result = edit_dlg.exec_()

        if result:
            company = edit_dlg.get_model()
            print("company=", company)

            if self.__controller_companys.update_company(company=company):
                self.refresh()

    def delete_element(self):
        """ Удаление страховой компании """

        print(": CompanysListWidget.delete_element()")

        try:
            curr_index = self.table.currentIndex()

            row = curr_index.row()
            col = curr_index.column()

            code = self.table.model().index(row, 0).data()

            if self.__controller_companys.delete_company(code):
                self.refresh()
        except Exception as e:
            print("e=", e)
