from ...base_classes.base_sections import BaseSections
from ...consts.Keys import Keys


class SectionCompanys(BaseSections):
    """ Наименовая блоков элементов для справочника Страховых компаний """

    def __init__(self):
        """ Конструктор """

        super(SectionCompanys, self).__init__(Keys.COMPANYS, Keys.COMPANY)
