from ....base_classes.base_sections import BaseSections
from ....consts.Keys import Keys


class SectionPathologys(BaseSections):
    """ Наименовая блоков элементов для справочника Паталогий """

    def __init__(self):
        """ Конструктор """

        super(SectionPathologys, self).__init__(Keys.PATHOLOGYS, Keys.PATHOLOGY)
