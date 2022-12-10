from ....common.base_classes.models.person import Person


class DoctorModel(Person):
    """ Модель. Доктор"""

    def __init__(self, code, last_name: str = "", first_name: str = "", middle_name: str = ""):
        """ Конструктор
        :param code: Код
        :param last_name: Фамилия
        :param first_name: Имя
        :param middle_name: Отчество
        """

        super().__init__(code, first_name=first_name, last_name=last_name, middle_name=middle_name)

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

        # s = f'["DoctorModel"] ({self.code}) {self.fam_io}'
        s = f'["DoctorModel"] ({self.code}) {self.fio}'

        return s
