import os
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QMessageBox
from PyQt5.QtGui import QIcon

from ...dict.doctors.views.doctors_list_widget import DoctorsListWidget
from ...dict.endos.views.endos_list_widget import EndosListWidget
from ...dict.organs.views.organ_list_widget import OrgansListWidget
from ...dict.organs.model.organ_model import OrganModel
from ...dict.device.model.device_model import DeviceModel
from ...dict.doctors.model.doctor_model import DoctorModel
from ...common.base_classes.views.base_dict_model_list_widget import BaseDictModelListWidget
from ...common.controllers.dict_doctor_controller import ControllerDictDoctor
from ...common.controllers.dict_organ_controller import ControllerDictOrgan
from ...common.controllers.dict_device_controller import ControllerDictDevice
from ...common.data.xml_data_provider import XmlDataProvider


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), '_main_window.ui'))


class MainWindow(QMainWindow, FORM_CLASS):
    """ Главное окно """

    __xml_provider = None  # Провайдер xml документа
    __controller_doctors: ControllerDictDoctor = None  # Контроллер справочника врачей
    __controller_organs: ControllerDictOrgan = None
    __controller_devices: ControllerDictDevice = None
    __current_widget_dict:BaseDictModelListWidget = None        # Текущий виджет показывающий справочник

    def __init__(self):
        """ Конструктор """

        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.__prepare_ui()

        self.__xml_provider = XmlDataProvider()
        self.__xml_provider.read()

        print("XmlDataProvider.root=", XmlDataProvider.root)
        print("self.__xml_provider.root=", self.__xml_provider.root)

        # ***
        # self.__controller_doctors = ControllerDictDoctor(self.__xml_provider)
        self.__controller_doctors = ControllerDictDoctor()
        self.__controller_organs = ControllerDictOrgan(self.__xml_provider)
        self.__controller_devices = ControllerDictDevice(self.__xml_provider)

        self.__current_widget_dict = None

        # list_organs_widget = OrgansListWidget(self.__xml_provider, parent=self)
        # self.layoutContaner_2.addWidget(list_organs_widget)

    def __prepare_ui(self):
        """ Подготовка интерфейса """

        print(": MainWindow.__prepare_ui()")

        self.setWindowTitle("Система эндоскопического отделения")

        self.__create_menu()
        self.statusBar().showMessage('Ready')

        self.menuItemDictDoctors.triggered.connect(self.__on_triggered_menuItemDictDoctors)
        self.menuItemDictOrgans.triggered.connect(self.__on_triggered_menuItemDictOrgans)
        self.menuItemDictEndoskop.triggered.connect(self.__on_triggered_menuItemDictEndos)

        self.pushButtonDictRefresh.clicked.connect(self.__on_clicked_pushButtonDictRefresh)
        self.pushButtonDictCreate.clicked.connect(self.__on_clicked_pushButtonDictCreate)
        self.pushButtonDictUpdate.clicked.connect(self.__on_clicked_pushButtonDictUpdate)
        self.pushButtonDictDelete.clicked.connect(self.__on_clicked_pushButtonDictDelete)

        self.pushBtn.clicked.connect(self.__on_pushBtn_clicked)
        # self.toolBtn.clicked.connect(self.__on_toolBtn_clicked)

    def __create_menu(self):
        """ Создание меню """

        exit_action = QAction(QIcon('door2.png'), '&Выход', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Закрыть приложение')
        exit_action.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        menu_file = menubar.addMenu('Файл')
        menu_file.addAction(exit_action)

        load_action = QAction('Загрузить', self)
        load_action.setStatusTip("Загрузить данные")
        load_action.triggered.connect(self.__on_click_menu_item_data_load)

        save_action = QAction('Сохранить', self)
        save_action.setStatusTip("Сохранить данные")
        save_action.triggered.connect(self.__on_click_menu_item_data_save)

        menu_operation = menubar.addMenu("Операции")
        menu_operation.addAction(load_action)
        menu_operation.addAction(save_action)

        # menu_dict = menubar.addMenu('Справочники')

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exit_action)

    def closeEvent(self, event):
        print(": MainWindow.closeEvent()")

        # self.__xmlData.write()

    def __on_click_menu_item_data_load(self):
        print("Загрузить данные")

        doctor = DoctorModel(1, "Иванов", "Иван", "Иванови")
        self.__controller_doctors.create_doctor(doctor)

        # doctor = DoctorModel(5, "Сидоров", "Сидр", "Сидорови")
        # self.__controller_doctors.create_doctor(doctor)

    def __on_click_menu_item_data_save(self):
        print("Сохранить данные")

        # self.xmlData.write()

    def __on_triggered_menuItemDictDoctors(self):
        """ Обработчик нажатия на кнопку 'Справочник' """

        print(": MainWindow.__on_triggered_menuItemDictDoctors")

        list_doctors_widget = DoctorsListWidget(self.__xml_provider, parent=self)
        self.__current_widget_dict = list_doctors_widget

        self.layoutContaner.addWidget(list_doctors_widget)

    def __on_triggered_menuItemDictOrgans(self):
        """ Обработчик выбора пункта меню 'Справочник Органов' """

        print(": MainWindow.__on_triggered_menuItemDictOrgans")

        # list_organs = self.__controller_organs.select_organs()
        # for organ in list_organs:
        #     print(f'- {organ}')

        list_organs_widget = OrgansListWidget(self.__xml_provider, parent=self)
        print('list_organs_widget:', list_organs_widget)

        self.__current_widget_dict = list_organs_widget

        # self.layoutContaner_2.addWidget(list_organs_widget)
        self.layoutContaner.addWidget(list_organs_widget)

    def __on_triggered_menuItemDictEndos(self):
        """ Обработчик выбора пункта меню 'Справочник 'Эндоскопий'' """

        print(": MainWindow.__on_triggered_menuItemDictEndos")

        list_endos_widget = EndosListWidget()

        self.__current_widget_dict = list_endos_widget

        # self.layoutContaner_2.addWidget(list_endos_widget)
        self.layoutContaner.addWidget(list_endos_widget)

    # def __on_pushBtnDict_device_clicked(self):
    #     """ Обработчик нажатия на кнопку 'Справочник' """
    #
    #     list_devices = self.__controller_devices.select_devices()
    #     for device in list_devices:
    #         print(f'- {device}')

    def __on_pushBtn_clicked(self):
        print(": MainWindow.__on_puchBtn_clicked()")
        self.__xml_provider.write()

    def __on_clicked_pushButtonDictRefresh(self):
        """ Обработчик события нажатия на кнопку 'Обновить' """

        print(": MainWindow.pushButtonDictRefresh()")

        if self.__current_widget_dict:
            self.__current_widget_dict.refresh()

    def __on_clicked_pushButtonDictCreate(self):
        """ Обработчик события нажатия на кнопку 'Добавить' """

        print(": MainWindow.__on_clicked_pushButtonDictCreate()")

        # # QMessageBox.information(self, "Инфо", "Добавим модель", QMessageBox.Ok)
        #
        # doctor = DoctorModel(55, "Иванов", "Иван", "Иванович")
        # edit_doctor_widget = DoctorEditWidget(doctor, self)
        # print("edit_doctor_widget=", edit_doctor_widget)
        #
        # edit_dlg = ModelEditDialog(edit_doctor_widget)
        # edit_dlg.show()
        # result = edit_dlg.exec_()
        # if result:
        #     model_edit = edit_dlg.get_model()
        #     print("model_edit=", model_edit)
        #
        #     print("Форма закрылась положительно")
        # else:
        #     print("Форма закрылась отрицательно!")

        if self.__current_widget_dict:
            self.__current_widget_dict.create_element()

    def __on_clicked_pushButtonDictUpdate(self):
        """ Обработчик события нажатия на кнопку 'Изменить' """

        print(": MainWindow.__on_clicked_pushButtonDictUpdate()")

        if self.__current_widget_dict:
            self.__current_widget_dict.update_element()

    def __on_clicked_pushButtonDictDelete(self):
        """ Обработчик события нажатия на кнопку 'Удалить' """

        print(": MainWindow.__on_clicked_pushButtonDictDelete()")

        if self.__current_widget_dict:
            self.__current_widget_dict.delete_element()