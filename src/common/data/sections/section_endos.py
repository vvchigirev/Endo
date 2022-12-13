from ...base_classes.base_sections import BaseSections
from ...consts.Keys import Keys


class SectionEndos(BaseSections):
    """ Наименовая блоков элементов для справочника Эндоскопий """

    def __init__(self):
        """ Конструктор """

        self.group_name: str = Keys.ENDOS
        self.element_name: str = Keys.ENDO
