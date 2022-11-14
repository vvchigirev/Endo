import os
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), '_main_window.ui'))

class MainWindow(QMainWindow, FORM_CLASS):
    """ Главное окно """

    def __init__(self):
        """ Конструктор """

        super().__init__()
        self.setupUi(self)

        self.__init_ui()

    def __init_ui(self):
        """ Инициализания интерфейса """

        print(": MainWindow.__init_ui()")

        self.setWindowTitle("Система эндоскопического отделения")

        self.__create_menu()
        self.statusBar().showMessage('Ready')

    def __create_menu(self):
        """ Создание меню """

        exit_action = QAction(QIcon('door2.png'), '&Выход', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Закрыть приложение')
        exit_action.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        menu_file = menubar.addMenu('Файл')
        menu_file.addAction(exit_action)

        menu_dict = menubar.addMenu('Справочники')

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exit_action)

    # def setupUi(self):
    #     print(": MainWindow.setupUi()")
    #
    #     self.setWindowTitle("Система эндоскопического отделения")