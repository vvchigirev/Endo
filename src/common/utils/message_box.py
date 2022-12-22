from PyQt5.QtWidgets import QMessageBox, QSpacerItem, QSizePolicy


class MessageBox:
    """ Окно сообщений """

    @staticmethod
    def __show_message(message, title, icon, buttons=QMessageBox.Ok):
        """ Показать окно
        :param message: Сообщение
        :param title: Заголовок окна
        :param icon: Иконка
        :param buttons: Кнопки в окне сообщения
        """

        msg_bx = QMessageBox()

        if icon:
            msg_bx.setIcon(icon)
        msg_bx.setWindowTitle(title)
        msg_bx.setText(message)
        msg_bx.setStandardButtons(buttons)

        if msg_bx.button(QMessageBox.Yes):
            msg_bx.button(QMessageBox.Yes).setText("&Да")
        if msg_bx.button(QMessageBox.No):
            msg_bx.button(QMessageBox.No).setText("&Нет")

        msg_bx.exec_()

    @staticmethod
    def show_info(message, title="Информация"):
        """ Сообщение информации
        :param message: Текст сообщения
        :param title: Заголовок
        """

        MessageBox.__show_message(message, title, QMessageBox.Information)

    @staticmethod
    def show_warning(message, title="Предупреждение"):
        """ Сообщение предупреждения
        :param message: Текст сообщения
        :param title: Заголовок
        """

        MessageBox.__show_message(message, title, QMessageBox.Warning)

    @staticmethod
    def show_error(message, title="Ошибка"):
        """ Сообщение об ошибке
        :param message: Текст сообщения
        :param title: Заголовок
        """

        MessageBox.__show_message(message, title, QMessageBox.Critical)

    @staticmethod
    def show_question(message, title=""):
        """ Сообщение об ошибке
        :param message: Текст сообщения
        :param title: Заголовок
        """

        MessageBox.__show_message(message, title, QMessageBox.Question, buttons=(QMessageBox.Yes | QMessageBox.No))
