import os
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QMessageBox
from PyQt5.QtGui import QIcon

from ...dict.doctors.views.doctors_list_widget import DoctorsListWidget
from ...dict.endos.views.endos_list_widget import EndosListWidget
from ...dict.organs.views.organ_list_widget import OrgansListWidget
from ...dict.device.views.devices_list_widget import DevicesListWidget
from ...dict.hospital.views.hospital_list_widget import HospitalsListWidget
from ...dict.pathology.views.pathologys_list_widget import PathologysListWidget
from ...dict.insuranсe_company.views.company_list_widget import CompanysListWidget

from ...dict.organs.model.organ_model import OrganModel
from ...dict.device.model.device_model import DeviceModel
from ...dict.doctors.model.doctor_model import DoctorModel

from ...common.base_classes.views.base_model_list_widget import BaseDictModelListWidget

from ...common.controllers.dict_doctor_controller import ControllerDictDoctor
from ...common.controllers.dict_organ_controller import ControllerDictOrgan
from ...common.controllers.dict_device_controller import ControllerDictDevice

from ...common.data.xml_data_provider import XmlDataProvider


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), '_main_window.ui'))


class MainWindow(QMainWindow, FORM_CLASS):
    """ Главное окно """

    __xml_provider = None                               # Провайдер xml документа
    __current_widget_dict: BaseDictModelListWidget = None        # Текущий виджет показывающий справочник

    def __init__(self):
        """ Конструктор """

        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.__prepare_ui()

        self.__xml_provider = XmlDataProvider()
        self.__xml_provider.read()

        print("XmlDataProvider.root=", XmlDataProvider.root)
        print("self.__xml_provider.root=", self.__xml_provider.root)

        self.__current_widget_dict = None

    def __prepare_ui(self):
        """ Подготовка интерфейса """

        print(": MainWindow.__prepare_ui()")

        self.setWindowTitle("Система эндоскопического отделения")

        self.__create_menu()
        self.statusBar().showMessage('Ready')
        # sys.setrecursionlimit(limit)

        self.menuItemDictDoctors.triggered.connect(self.__on_triggered_menuItemDictDoctors)
        self.menuItemDictOrgans.triggered.connect(self.__on_triggered_menuItemDictOrgans)
        self.menuItemDictDevices.triggered.connect(self.__on_triggered_menuItemDictDevices)
        self.menuItemDictEndoskop.triggered.connect(self.__on_triggered_menuItemDictEndos)
        self.menuItemDictHospital.triggered.connect(self.__on_triggered_menuItemDictHospitals)
        self.menuItemDictPathology.triggered.connect(self.__on_triggered_menuItemDictPathologys)
        self.menuItemDictCompany.triggered.connect(self.__on_triggered_menuItemDictCompanys)

        self.pushButtonDictRefresh.clicked.connect(self.__on_clicked_pushButtonDictRefresh)
        self.pushButtonDictCreate.clicked.connect(self.__on_clicked_pushButtonDictCreate)
        self.pushButtonDictUpdate.clicked.connect(self.__on_clicked_pushButtonDictUpdate)
        self.pushButtonDictDelete.clicked.connect(self.__on_clicked_pushButtonDictDelete)

        self.pushBtn.clicked.connect(self.__on_pushBtn_clicked)

    def __create_menu(self):
        """ Создание меню """

        exit_action = QAction(QIcon('door2.png'), '&Выход', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Закрыть приложение')
        exit_action.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        menu_file = menubar.addMenu('Файл')
        menu_file.addAction(exit_action)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exit_action)

    def closeEvent(self, event):
        print(": MainWindow.closeEvent()")

        # self.__xmlData.write()

    def __on_triggered_menuItemDictDoctors(self):
        """ Обработчик нажатия на кнопку 'Справочник' """

        print(": MainWindow.__on_triggered_menuItemDictDoctors")

        if self.__current_widget_dict:
            self.__current_widget_dict.hide()

        list_doctors_widget = DoctorsListWidget(parent=self)
        self.__current_widget_dict = list_doctors_widget

        self.layoutContaner.addWidget(list_doctors_widget)

    def __on_triggered_menuItemDictOrgans(self):
        """ Обработчик выбора пункта меню 'Справочник Органов' """

        print(": MainWindow.__on_triggered_menuItemDictOrgans")

        if self.__current_widget_dict:
            self.__current_widget_dict.hide()

        list_organs_widget = OrgansListWidget(parent=self)
        self.__current_widget_dict = list_organs_widget

        # self.layoutContaner_2.addWidget(list_organs_widget)
        self.layoutContaner.addWidget(list_organs_widget)

    def __on_triggered_menuItemDictEndos(self):
        """ Обработчик выбора пункта меню 'Справочник 'Эндоскопий'' """

        print(": MainWindow.__on_triggered_menuItemDictEndos")

        if self.__current_widget_dict:
            self.__current_widget_dict.hide()

        list_endos_widget = EndosListWidget(parent=self)

        self.__current_widget_dict = list_endos_widget

        self.layoutContaner.addWidget(list_endos_widget)

    def __on_triggered_menuItemDictDevices(self):
        """ Обработчик выбора пункта меню 'Справочник Приборов' """

        print(": MainWindow.__on_triggered_menuItemDictDevices")

        if self.__current_widget_dict:
            self.__current_widget_dict.hide()

        list_devices_widget = DevicesListWidget(parent=self)
        self.__current_widget_dict = list_devices_widget

        self.layoutContaner.addWidget(list_devices_widget)

    def __on_triggered_menuItemDictHospitals(self):
        """ Обработчик выбора пункта меню 'Справочник Больниц' """

        print(": MainWindow.__on_triggered_menuItemDictDevices")

        if self.__current_widget_dict:
            self.__current_widget_dict.hide()

        list_hospitals_widget = HospitalsListWidget(parent=self)
        self.__current_widget_dict = list_hospitals_widget

        self.layoutContaner.addWidget(list_hospitals_widget)

    def __on_triggered_menuItemDictPathologys(self):
        """ Обработчик выбора пункта меню 'Справочник Патологий' """

        print(": MainWindow.__on_triggered_menuItemDictPathologys")

        if self.__current_widget_dict:
            self.__current_widget_dict.hide()

        list_pathologys_widget = PathologysListWidget(parent=self)
        self.__current_widget_dict = list_pathologys_widget

        self.layoutContaner.addWidget(list_pathologys_widget)

    def __on_triggered_menuItemDictCompanys(self):
        """ Обработчик выбора пункта меню 'Справочник Страховых компаний' """

        print(": MainWindow.__on_triggered_menuItemDictCompanys")

        if self.__current_widget_dict:
            self.__current_widget_dict.hide()

        list_companys_widget = CompanysListWidget(parent=self)
        self.__current_widget_dict = list_companys_widget

        self.layoutContaner.addWidget(list_companys_widget)

    def __on_pushBtn_clicked(self):
        print(": MainWindow.__on_puchBtn_clicked()")
        self.__xml_provider.write()

    def __on_clicked_pushButtonDictRefresh(self):
        """ Обработчик события нажатия на кнопку 'Обновить' """

        # print(": MainWindow.pushButtonDictRefresh()")

        if self.__current_widget_dict:
            self.__current_widget_dict.refresh()

    def __on_clicked_pushButtonDictCreate(self):
        """ Обработчик события нажатия на кнопку 'Добавить' """

        # print(": MainWindow.__on_clicked_pushButtonDictCreate()")

        if self.__current_widget_dict:
            self.__current_widget_dict.create_element()

    def __on_clicked_pushButtonDictUpdate(self):
        """ Обработчик события нажатия на кнопку 'Изменить' """

        # print(": MainWindow.__on_clicked_pushButtonDictUpdate()")

        if self.__current_widget_dict:
            self.__current_widget_dict.update_element()

    def __on_clicked_pushButtonDictDelete(self):
        """ Обработчик события нажатия на кнопку 'Удалить' """

        # print(": MainWindow.__on_clicked_pushButtonDictDelete()")

        if self.__current_widget_dict:
            self.__current_widget_dict.delete_element()