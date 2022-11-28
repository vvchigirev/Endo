import os
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

from ...dict.doctors.model.doctor_model import DoctorModel
from ...common.controllers.dict_doctor_controller import ControllerDictDoctor
from ...common.data.xml_data_provider import XmlDataProvider


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), '_main_window.ui'))


class MainWindow(QMainWindow, FORM_CLASS):
    """ Главное окно """

    __xml_provider = None                                    # Провайдер xml документа
    __controller_doctors: ControllerDictDoctor = None   # Контроллер справочника  врачей

    def __init__(self):
        """ Конструктор """

        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.__init_ui()

        self.__xml_provider = XmlDataProvider()
        self.__xml_provider.read()

        self.__controller_doctors = ControllerDictDoctor(self.__xml_provider)

    def __init_ui(self):
        """ Инициализания интерфейса """

        print(": MainWindow.__init_ui()")

        self.setWindowTitle("Система эндоскопического отделения")

        self.__create_menu()
        self.statusBar().showMessage('Ready')

        self.puchBtn.clicked.connect(self.__on_puchBtn_clicked)
        self.toolBtn.clicked.connect(self.__on_toolBtn_clicked)

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

        menu_dict = menubar.addMenu('Справочники')

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exit_action)

    def closeEvent(self, event):
        print(": MainWindow.closeEvent()")

        # xml = XmlDataPrivider()
        # xml.add_pribors()
        # xml.add_doctors()

        # XmlDataProvider.write()
        # self.__xmlData.write()

    def __on_click_menu_item_data_load(self):
        print("Загрузить данные")

        doctor = DoctorModel(1, "Иванов", "Иван", "Иванови")
        self.__controller_doctors.add_el(doctor)

        doctor = DoctorModel(5, "Сидоров", "Сидр", "Сидорови")
        self.__controller_doctors.add_el(doctor)

        # XmlDataPrivider.add_doctor(doctor)

    def __on_click_menu_item_data_save(self):
        print("Сохранить данные")

        # self.xmlData.write()

    def __on_puchBtn_clicked(self):
        print(": MainWindow.__on_puchBtn_clicked()")

        self.__xml_provider.write()

    def __on_toolBtn_clicked(self):
        print(": MainWindow.__on_puchBtn_clicked()")

        # doctor = DoctorModel(1, "Иванов", "Иван", "Иванови")
        # self.__controller_doctors.add_el(doctor)

        # doctor = DoctorModel(5, "Петров", "Петр", "Петрович")
        # self.__controller_doctors.add_el(doctor)
        #
        # doctor = DoctorModel(19, "Иванов", "Петр", "Сидорович")
        # print("doctor= ", doctor)

        doctor = DoctorModel(10, "Сергеев", "Сергей", "Сергееч")
        self.__controller_doctors.add_el(doctor)

        self.__controller_doctors.add_el(doctor)
