from ....base_classes.base_sections import BaseSections
from ....consts.Keys import Keys


class SectionMedManipulations(BaseSections):
    """ Наименовая блоков элементов для справочника Приборов """

    def __init__(self):
        """ Конструктор """

        super(SectionMedManipulations, self).__init__(Keys.MED_MANIPULATIONS, Keys.MED_MANIPULATION)
