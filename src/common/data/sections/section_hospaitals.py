from ...base_classes.base_sections import BaseSections
from ...consts.Keys import Keys


class SectionHospitals(BaseSections):
    """ Наименовая блоков элементов для справочника Больниц """

    def __init__(self):
        """ Конструктор """

        super(SectionHospitals, self).__init__(Keys.HOSPITALS, Keys.HOSPITAL)

