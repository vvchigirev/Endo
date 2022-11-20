from ....common.base_classes.models.person import Person


class DoctorModel(Person):
    """ Модель. Доктор"""

    def __init__(self, code, l_name: str = "", f_name: str = "", m_name: str = ""):
        """ Конструктор
        :param code: Код
        :param l_name: Фамилия
        :param f_name: Имя
        :param m_name: Отчество
        """

        super().__init__(code, first_name=f_name, last_name=l_name, middle_name=m_name)

    # region Свойства

    @property
    def code(self):
        """ Свойство. Код врача """
        return self.id
    # endregion

    def __str__(self):
        """ Строковое представление модели врача
        :return:
        """

        s = f'({self.code}) {self.fam_io}'

        return s
