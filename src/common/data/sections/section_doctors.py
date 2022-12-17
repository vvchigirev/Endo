from ...base_classes.base_sections import BaseSections
from ...consts.Keys import Keys


class SectionDoctors(BaseSections):
    """ Наименовая блоков элементов для справочника Враче """

    def __init__(self):
        """ Конструктор """

        super(SectionDoctors, self).__init__(el_group_name=Keys.DOCTORS, el_name=Keys.DOCTOR)
