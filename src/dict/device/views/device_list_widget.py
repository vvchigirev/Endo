from PyQt5.QtWidgets import QWidget


class DevicesListWidget(QWidget):

    def __init__(self, parent):
        """ Конструктор
            :param parent: Родитель
            """
        super(DevicesListWidget, self).__init__()
        self.setupUi(self)
