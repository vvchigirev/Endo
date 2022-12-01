from ...base_classes.base_sections import BaseSections
from ...consts.Keys import Keys


class SectionDoctors(BaseSections):
    """ Наименовая блоков элементов для справочника Враче """

    def __init__(self):
        """ Конструктор """

        self.group_name = Keys.DOCTORS
        self.element_name = Keys.DOCTOR
