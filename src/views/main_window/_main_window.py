import os
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QMessageBox
from PyQt5.QtGui import QIcon

from ...dict.doctors.views.doctors_list_widget import DocktorListWidget
from ...dict.organs.model.organ_model import OrganModel
from ...dict.device.model.device_model import DeviceModel
from ...dict.doctors.model.doctor_model import DoctorModel
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
    __current_widget_dict = None        # Текущий виджет показывающий справочник

    def __init__(self):
        """ Конструктор """

        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.__prepare_ui()

        self.__xml_provider = XmlDataProvider()
        self.__xml_provider.read()

        self.__controller_doctors = ControllerDictDoctor(self.__xml_provider)
        self.__controller_organs = ControllerDictOrgan(self.__xml_provider)
        self.__controller_devices = ControllerDictDevice(self.__xml_provider)

        self.__current_widget_dict = None

    def __prepare_ui(self):
        """ Подготовка интерфейса """

        print(": MainWindow.__prepare_ui()")

        self.setWindowTitle("Система эндоскопического отделения")

        self.__create_menu()
        self.statusBar().showMessage('Ready')

        self.pushBtnDoctorDict.clicked.connect(self.__on_pushBtnDict_doctor_clicked)
        self.pushBtnDoctorFind.clicked.connect(self.__on_pushBtnFind_doctor_clicked)
        self.pushButtonDoctorCreate.clicked.connect(self.__on_pushButton_create_doctor_clicked)
        self.pushButtonDoctorUpdate.clicked.connect(self.__on_pushButton_update_doctor_clicked)
        self.pushButtonDoctorDelete.clicked.connect(self.__on_pushButton_delete_doctor_clicked)

        self.pushBtnOrganDict.clicked.connect(self.__on_pushBtnDict_organ_clicked)
        self.pushBtnOrganFind.clicked.connect(self.__on_pushBtnFind_organ_clicked)
        self.pushButtonOrganAdd.clicked.connect(self.__on_pushButtonAdd_organ_clicked)
        self.pushButtonOrganUpdate.clicked.connect(self.__on_pushButtonUpdate_organ_clicked)
        self.pushButtonOrganRemove.clicked.connect(self.__on_pushButtonRemove_organ_clicked)

        self.pushBtnDeviceDict.clicked.connect(self.__on_pushBtnDict_device_clicked)
        self.pushBtnDeviceFind.clicked.connect(self.__on_pushBtnFind_device_clicked)
        self.pushButtonDeviceAdd.clicked.connect(self.__on_pushButtonAdd_device_clicked)
        self.pushButtonDeviceUpdate.clicked.connect(self.__on_pushButtonUpdate_device_clicked)
        self.pushButtonDeviceRemove.clicked.connect(self.__on_pushButtonRemove_device_clicked)

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

    def __on_pushBtnDict_doctor_clicked(self):
        """ Обработчик нажатия на кнопку 'Справочник' """


        # list_doctors: list[DoctorModel] = self.__controller_doctors.select_doctors()
        # for doctor in list_doctors:
        #     print(f'- {doctor}')

        list_doctors_widget = DocktorListWidget(self.__xml_provider)
        self.__current_widget_dict = list_doctors_widget

        # list_doctors_widget.set_data(list_doctors)

        # print("list_doctors_widget=", list_doctors_widget)
        # print("self.layoutContaner=", self.layoutContaner)

        self.layoutContaner.addWidget(list_doctors_widget)

        print("hello")


    def __on_pushBtnFind_doctor_clicked(self):
        """ Обработчик нажатия на кнопку 'Найти' """

        code = None

        if self.lineEditDoctorCode.text():
            code = int(self.lineEditDoctorCode.text())
            print(code)

        elif not self.lineEditDoctorCode.text():
            QMessageBox.critical(self, "Ошибка ", "Заполните все поля!", QMessageBox.Ok)
            return False

        doctor = self.__controller_doctors.get_doctor(code)
        if doctor:
            print(f'- {doctor}')
        else:
            print(f'Врач под кодом-{code} не найден!')

    def __on_pushButton_create_doctor_clicked(self):
        """ Обработчик нажатия на кнопку 'Добавить' """

        code = None

        if self.lineEditDoctorCode.text():
            code = int(self.lineEditDoctorCode.text())
            print(code)

        elif not self.lineEditDoctorCode.text():
            QMessageBox.critical(self, "Ошибка ", "Заполните все поля!", QMessageBox.Ok)
            return False

        doctor = DoctorModel(code, "1", "1", "1")

        if self.__controller_doctors.create_doctor(doctor):
            print(f'Врач {doctor} успешно добавлен')
        else:
            print(f'Врач {doctor} НЕ добавлен !!!')

        # if self.__current_widget_dict:
        #     self.__current_widget_dict.create_elements()
        # else:
        #     print("- Виджет текущего справочника не определен !!!")

    def __on_pushButton_update_doctor_clicked(self):
        """ Обработчик нажатия на кнопку 'Обновить' """
        code = None

        if self.lineEditDoctorCode.text():
            code = int(self.lineEditDoctorCode.text())
            print(code)

        elif not self.lineEditDoctorCode.text():
            QMessageBox.critical(self, "Ошибка ", "Заполните все поля!", QMessageBox.Ok)
            return False

        doctor = DoctorModel(code, "3", "3", "3")

        if self.__controller_doctors.update_doctor(doctor):
            print(f'Врач {doctor} успешно обновлен')
        else:
            print(f'Врач {doctor} НЕ обновлен !!!')

    def __on_pushButton_delete_doctor_clicked(self):
        """ Обработчик нажатия на кнопку 'Удалить' """

        code = None

        if self.lineEditDoctorCode.text():
            code = int(self.lineEditDoctorCode.text())
            print(code)

        elif not self.lineEditDoctorCode.text():
            QMessageBox.critical(self, "Ошибка ", "Заполните все поля!", QMessageBox.Ok)
            return False

        if self.__controller_doctors.delete_doctor(code):
            self.statusbar.showMessage(f'Врач с кодом-{code} успешно удален!', 3000)
            print(f'Врач с кодом-{code} успешно удален!')
        else:
            self.statusbar.showMessage(f'Врач с кодом: {code} не удален!', 3000)
            print(f'Врач с кодом: {code} не удален!')

        # if self.__current_widget_dict:
        #     self.__current_widget_dict.delete_element()


    def __on_pushBtnDict_organ_clicked(self):
        """ Обработчик нажатия на кнопку 'Справочник' """

        list_organs = self.__controller_organs.select_organs()
        for organ in list_organs:
            print(f'- {organ}')

    def __on_pushBtnFind_organ_clicked(self):
        """ Обработчик нажатия на кнопку 'Найти' """

        code = None
        name = None

        if self.lineEditOrganCode.text() and self.lineEditOrganName.text():
            code = int(self.lineEditOrganCode.text())
            name = self.lineEditOrganName.text()
            print(code, name)

        elif not self.lineEditOrganCode.text() or not self.lineEditOrganName.text():
            QMessageBox.critical(self, "Ошибка ", "Заполните все поля!", QMessageBox.Ok)
            return False
        organ = self.__controller_organs.get_organ(code)
        if organ:
            print(organ)
        else:
            print(f'Орган под кодом-{code} не найден!')

    def __on_pushButtonAdd_organ_clicked(self):
        """ Обработчик нажатия на кнопку 'Добавить' """

        code = None
        name = None

        if self.lineEditOrganCode.text() and self.lineEditOrganName.text():
            code = int(self.lineEditOrganCode.text())
            name = self.lineEditOrganName.text()
            print(code, name)

        elif not self.lineEditOrganCode.text() or not self.lineEditOrganName.text():
            QMessageBox.critical(self, "Ошибка ", "Заполните все поля!", QMessageBox.Ok)
            return False

        organ = OrganModel(code, name)

        print(organ)

        if self.__controller_organs.creat_organ(organ):
            print(f'Орган {name} успешно добавлен')
        else:
            print(f'Орган {name} НЕ добавлен !!!')

    def __on_pushButtonUpdate_organ_clicked(self):
        """ Обработчик нажатия на кнопку 'Обновить' """

        code = None
        name = None

        if self.lineEditOrganCode.text() and self.lineEditOrganName.text():
            code = int(self.lineEditOrganCode.text())
            name = self.lineEditOrganName.text()
            print(code, name)

        elif not self.lineEditOrganCode.text() or not self.lineEditOrganName.text():
            QMessageBox.critical(self, "Ошибка ", "Заполните все поля!", QMessageBox.Ok)
            return False

        organ = OrganModel(code, name)
        if self.__controller_organs.update_organ(organ):
            print(f'Орган {organ} успешно обновлен')
        else:
            print(f'Орган {organ} НЕ обновлен !!!')

    def __on_pushButtonRemove_organ_clicked(self):
        """ Обработчик нажатия на кнопку 'Удалить' """
        print("123")

        code = None
        name = None

        if self.lineEditOrganCode.text() and self.lineEditOrganName.text():
            code = int(self.lineEditOrganCode.text())
            name = self.lineEditOrganName.text()
            print(code, name)

        elif not self.lineEditOrganCode.text() or not self.lineEditOrganName.text():
            QMessageBox.critical(self, "Ошибка ", "Заполните все поля!", QMessageBox.Ok)
            return False

        if self.__controller_organs.delet_organ(code):
            self.statusbar.showMessage(f'Орган с кодом-{code} успешно удален!', 3000)
            print(f'Орган с кодом-{code} успешно удален!')
        else:
            self.statusbar.showMessage(f'Орган с кодом: {code} не удален!', 3000)
            print(f'Орган с кодом: {code} не удален!')

    def __on_pushBtnDict_device_clicked(self):
        """ Обработчик нажатия на кнопку 'Справочник' """

        list_devices = self.__controller_devices.select_devices()
        for device in list_devices:
            print(f'- {device}')

    def __on_pushBtnFind_device_clicked(self):
        """ Обработчик нажатия на кнопку 'Найти' """

        code = None
        name = None

        if self.lineEditDeviceCode.text() and self.lineEditDeviceName.text():
            code = int(self.lineEditDeviceCode.text())
            name = self.lineEditDeviceName.text()
            print(code, name)

        elif not self.lineEditDeviceCode.text() or not self.lineEditDeviceName.text():
            QMessageBox.critical(self, "Ошибка ", "Заполните все поля!", QMessageBox.Ok)
            return False
        device = self.__controller_devices.get_device(code)
        if device:
            print(device)
        else:
            print(f'Прибор под кодом-{code} не найден!')

    def __on_pushButtonAdd_device_clicked(self):
        """ Обработчик нажатия на кнопку 'Добавить' """

        code = None
        name = None

        if self.lineEditDeviceCode.text() and self.lineEditDeviceName.text():
            code = int(self.lineEditDeviceCode.text())
            name = self.lineEditDeviceName.text()
            print(code, name)

        elif not self.lineEditDeviceCode.text() or not self.lineEditDeviceName.text():
            QMessageBox.critical(self, "Ошибка ", "Заполните все поля!", QMessageBox.Ok)
            return False

        device = DeviceModel(code, name)

        print(device)

        if self.__controller_devices.creat_device(device):
            print(f'Прибор {name} успешно добавлен')
        else:
            print(f'Прибор {name} НЕ добавлен !!!')

    def __on_pushButtonUpdate_device_clicked(self):
        """ Обработчик нажатия на кнопку 'Обновить' """

        code = None
        name = None

        if self.lineEditDeviceCode.text() and self.lineEditDeviceName.text():
            code = int(self.lineEditDeviceCode.text())
            name = self.lineEditDeviceName.text()
            print(code, name)

        elif not self.lineEditDeviceCode.text() or not self.lineEditDeviceName.text():
            QMessageBox.critical(self, "Ошибка ", "Заполните все поля!", QMessageBox.Ok)
            return False

        device = DeviceModel(code, name)
        if self.__controller_devices.update_device(device):
            print(f'Прибор {device} успешно обновлен')
        else:
            print(f'Прибор {device} НЕ обновлен !!!')

    def __on_pushButtonRemove_device_clicked(self):
        """ Обработчик нажатия на кнопку 'Удалить' """
        print("123")

        code = None
        name = None

        if self.lineEditDeviceCode.text() and self.lineEditDeviceName.text():
            code = int(self.lineEditDeviceCode.text())
            name = self.lineEditDeviceName.text()
            print(code, name)

        elif not self.lineEditDeviceCode.text() or not self.lineEditDeviceName.text():
            QMessageBox.critical(self, "Ошибка ", "Заполните все поля!", QMessageBox.Ok)
            return False

        if self.__controller_devices.delet_device(code):
            self.statusbar.showMessage(f'Прибор с кодом-{code} успешно удален!', 3000)
            print(f'Прибор с кодом-{code} успешно удален!')
        else:
            self.statusbar.showMessage(f'Прибор с кодом: {code} не удален!', 3000)
            print(f'Прибор с кодом: {code} не удален!')
    def __on_pushBtn_clicked(self):
        print(": MainWindow.__on_puchBtn_clicked()")
        self.__xml_provider.write()

