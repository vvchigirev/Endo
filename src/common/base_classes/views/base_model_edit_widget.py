from PyQt5.QtWidgets import QWidget


class BaseModelEditWidget(QWidget):
    """ Базовый виджет для редактирования моделей """

    __parent = None     # Родительский элемент

    def __init__(self, parent):
        """ Конструктор
        :param parent: Родитель
        """

        super(BaseModelEditWidget, self).__init__()
        self.setupUi(self)

        self.__parent = parent

    @property
    def parent(self):
        """ Свойство. Родитель """

        return self.__parent

    def get_model(self):
        """ Получени модели """

        print(": BaseModelEditWidget.get_model()")

        return None

    def check_input_values(self):
        """ Проверка введенных значений """

        print("Метод check_input_values() не перегружен!")

        return True

    def get_value_fields(self):
        """ Получение """
        pass

