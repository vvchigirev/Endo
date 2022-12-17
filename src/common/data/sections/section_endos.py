from ...base_classes.base_sections import BaseSections
from ...consts.Keys import Keys


class SectionEndos(BaseSections):
    """ Наименовая блоков элементов для справочника Эндоскопий """

    def __init__(self):
        """ Конструктор """

        super(SectionEndos, self).__init__(Keys.ENDOS, Keys.ENDO)

