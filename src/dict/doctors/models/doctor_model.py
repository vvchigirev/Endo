from ....common.base_classes.models.person import Person


class DoctorModel(Person):
    """ Модель. Доктор"""

    def __init__(self, kode, l_name="", f_name="", m_name=""):
        """ Конструктор
        :param kode: Код
        :param l_name: Фамилия
        :param f_name: Имя
        :param m_name: Отчество
        """

        super().__init__(kode, first_name=f_name, last_name=l_name, middle_name=m_name)

    # region Свойства

    @property
    def kode(self):
        """ Свойство. Код врача """

    # endregion

    def __str__(self):
        """ Строковое представление модели врача
        :return:
        """

        s = f'({self.kode}) {self.fam_io}'

        return s
