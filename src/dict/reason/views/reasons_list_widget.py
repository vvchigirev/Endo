import os

from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from ....common.base_classes.views.base_model_list_widget import BaseDictModelListWidget

from ....common.views.model_edit.dict_model_edit_codename_widget import DictModelEditCodeNameWidget
from ....common.controllers.dict_reason_controller import ControllerDictReason
from ....common.views.model_edit.model_edit_dialog import ModelEditDialog
from ....common.views.model_edit.dict_model_edit_codename_widget import DictModelEditCodeNameWidget

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'reasons_list_widget.ui'))


class ReasonsListWidget(BaseDictModelListWidget, FORM_CLASS):
    """ Виджет. Список причин обращения """

    __table_model = None  # Модель таблицы
    __controller_reasons = None  # Контроллер справочника докторов

    def __init__(self, parent=None):
        """ Конструктор
        :param xml_provider: Провайдер данных xml
        :param parent: Родитель
        """

        print(": ReasonsListWidget.__init__()")

        super(ReasonsListWidget, self).__init__(parent)

        self.__init_table()

        self.__controller_reasons = ControllerDictReason()
        self.refresh()

    def __init_table(self):
        """ Инициализация таблицы данных """

        print(": ReasonsListWidget.__init_table()")

        self.__table_model = QStandardItemModel()

        self.__table_model.setHorizontalHeaderLabels(['Код', 'Наименование'])
        self.table.setModel(self.__table_model)

    def refresh(self):
        """Обновление списка причин обращения"""

        print(": ReasonsListWidget.refresh()")

        self.__table_model.clear()
        self.__table_model.setHorizontalHeaderLabels(['Код', 'Наименование'])


        list_reasons = self.__controller_reasons.select_reasons()

        print("list_reasons=", list_reasons)

        for row, reason in enumerate(list_reasons):
            print("reason=", reason)

            item_code = QStandardItem(str(reason.code))
            print("item_code=", str(item_code))
            item_name = QStandardItem(reason.name)
            print("item_name=", item_name)

            self.__table_model.setItem(row, 0, item_code)
            self.__table_model.setItem(row, 1, item_name)

            print("self.__table_model=", self.__table_model)
        # self.__table_model.resizeColumnsToContents()

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def create_element(self):
        """ Добавление причины обращения """

        print(": ReasonsListWidget.create_element()")
        try:
            edit_reason_widget = DictModelEditCodeNameWidget(parent=self, model=None)

            print("edit_reason_widget=", edit_reason_widget)

            edit_dlg = ModelEditDialog(edit_reason_widget)
            edit_dlg.show()
            result = edit_dlg.exec_()

            if result:
                reason = edit_dlg.get_model()
                print("reason=", reason)

                if self.__controller_reasons.create_reason(reason=reason):
                    self.refresh()
        except Exception as e:
            print("e=", e)

    def update_element(self):
        """ Обновление причины обращения """

        print(": ReasonsListWidget.update_element()")

        # reason = ReasonModel(222, "2", "2", "2")
        curr_index = self.table.currentIndex()
        row = curr_index.row()
        col = curr_index.column()

        code = self.table.model().index(row, 0).data()

        reason = self.__controller_reasons.get_reason(code)

        if not reason:
            return

        edit_reason_widget = DictModelEditCodeNameWidget(parent=self, model=reason)

        edit_dlg = ModelEditDialog(edit_reason_widget)
        edit_dlg.show()
        result = edit_dlg.exec_()

        if result:
            reason = edit_dlg.get_model()
            print("reason=", reason)

            if self.__controller_reasons.update_reason(reason=reason):
                self.refresh()

    def delete_element(self):
        """ Удаление причины обращения """

        print(": ReasonsListWidget.delete_element()")

        try:
            curr_index = self.table.currentIndex()

            row = curr_index.row()
            col = curr_index.column()

            code = self.table.model().index(row, 0).data()

            if self.__controller_reasons.delete_reason(code):
                self.refresh()
        except Exception as e:
            print("e=", e)
