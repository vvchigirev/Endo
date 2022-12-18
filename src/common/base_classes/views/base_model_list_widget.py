from PyQt5.QtWidgets import QWidget


class BaseDictModelListWidget(QWidget):
    """ Базовый виджет для визуализации списка моделей """

    __parent = None  # Родительский элемент

    def __init__(self, parent):
        """ Конструктор
        :param parent: Родитель
        """

        super(BaseDictModelListWidget, self).__init__()
        self.setupUi(self)

        self.__parent = parent

    @property
    def parent(self):
        """ Свойство. Родитель """

        return self.__parent

    def refresh(self):
        """ Обновление списка элементов массива"""

        print(": BaseDictModelListWidget.refresh()")

    def create_element(self):
        """ Добавление элемента справочника """

        print(": BaseDictModelListWidget.create_element()")

    def update_element(self):
        """ Обновление элемента справочника """

        print(": BaseDictModelListWidget.update_element()")

    def delete_element(self):
        """ Удаление элемента справочника """

        print(": BaseDictModelListWidget.delete_element()")