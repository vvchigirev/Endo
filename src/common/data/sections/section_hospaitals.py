from ...base_classes.base_sections import BaseSections
from ...consts.Keys import Keys


class SectionHospitals(BaseSections):
    """ Наименовая блоков элементов для справочника Больниц """

    def __init__(self):
        """ Конструктор """

        self.group_name = Keys.HOSPITALS
        self.element_name = Keys.HOSPITAL
