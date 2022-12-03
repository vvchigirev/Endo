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

        self.__prepare_ui()

        self.__xml_provider = XmlDataProvider()
        self.__xml_provider.read()

        self.__controller_doctors = ControllerDictDoctor(self.__xml_provider)

    def __prepare_ui(self):
        """ Подготовка интерфейса """

        print(": MainWindow.__prepare_ui()")

        self.setWindowTitle("Система эндоскопического отделения")

        self.__create_menu()
        self.statusBar().showMessage('Ready')

        self.pushBtnDict.clicked.connect(self.__on_puchBtnDict_clicked)
        self.pushFind.clicked.connect(self.__on_puchBtnFind_clicked)

        self.pushButtonAdd.clicked.connect(self.__on_pushButtonAdd_clicked)
        self.pushButtonUpdate.clicked.connect(self.__on_pushButtonUpdate_clicked)
        self.pushButtonRemove.clicked.connect(self.__on_pushButtonRemove_clicked)

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

    def __on_puchBtnDict_clicked(self):
        """ Обработчик нажатия на кнопку 'Справочник' """

        list_doctors = self.__controller_doctors.select_doctors()
        for doctor in list_doctors:
            print(f'- {doctor}')

    def __on_puchBtnFind_clicked(self):
        """ Обработчик нажатия на кнопку 'Найти' """

        code = 100
        doctor = self.__controller_doctors.get_doctor(code)
        if doctor:
            print(f'- {doctor}')
        else:
            print(f'Врач под кодом-{code} не найден!')

    def __on_pushButtonAdd_clicked(self):
        """ Обработчик нажатия на кнопку 'Обновить' """

        # doctor = DoctorModel(25, "Петров", "Петр", "Петрович")
        doctor = DoctorModel(125, "1", "1", "1")

        if self.__controller_doctors.create_doctor(doctor):
            print(f'Врач {doctor} успешно добавлен')
        else:
            print(f'Врач {doctor} НЕ добавлен !!!')

    def __on_pushButtonUpdate_clicked(self):
        """ Обработчик нажатия на кнопку 'Обновить' """

        doctor = DoctorModel(125, "3", "3", "3")
        if self.__controller_doctors.update_doctor(doctor):
            print(f'Врач {doctor} успешно обновлен')
        else:
            print(f'Врач {doctor} НЕ обновлен !!!')


    def __on_pushButtonRemove_clicked(self):
        """ Обработчик нажатия на кнопку 'Удалить' """

        code = int(self.lineEditCodeRemove.text())
        if self.__controller_doctors.delete_doctor(code):
            self.statusbar.showMessage(f'Врач с кодом-{code} успешно удален!', 3000)
            print(f'Врач с кодом-{code} успешно удален!')
        else:
            self.statusbar.showMessage(f'Врач с кодом: {code} не удален!', 3000)
            print(f'Врач с кодом: {code} не удален!')

    def __on_puchBtn_clicked(self):
        print(": MainWindow.__on_puchBtn_clicked()")

        self.__xml_provider.write()

    def __on_toolBtn_clicked(self):
        print(": MainWindow.__on_puchBtn_clicked()")

        # doctor = DoctorModel(1, "Иванов", "Иван", "Иванови")
        # self.__controller_doctors.create_doctor(doctor)

        # doctor = DoctorModel(5, "Петров", "Петр", "Петрович")
        # self.__controller_doctors.create_doctor(doctor)

        # doctor = DoctorModel(19, "Иванов", "Петр", "Сидорович")
        # print("doctor= ", doctor)

        doctor = DoctorModel(150, "Сергеев1", "Сергей1", "Сергееч1")
        self.__controller_doctors.create_doctor(doctor)
