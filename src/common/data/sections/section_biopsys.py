from ...base_classes.base_sections import BaseSections
from ...consts.Keys import Keys


class SectionBiopsys(BaseSections):
    """ Наименовая блоков элементов для справочника Биопсий """

    def __init__(self):
        """ Конструктор """

        super(SectionBiopsys, self).__init__(Keys.BIOPSYS, Keys.BIOPSY)
