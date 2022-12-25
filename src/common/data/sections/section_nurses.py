from ...base_classes.base_sections import BaseSections
from ...consts.Keys import Keys


class SectionNurses(BaseSections):
    """ Наименовая блоков элементов для справочника Мед Сестер """

    def __init__(self):
        """ Конструктор """

        super(SectionNurses, self).__init__(el_group_name=Keys.NURSES, el_name=Keys.NURSE)
