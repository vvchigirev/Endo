from ...base_classes.base_sections import BaseSections
from ...consts.Keys import Keys


class SectionComplications(BaseSections):
    """ Наименовая блоков элементов для справочника Приборов """

    def __init__(self):
        """ Конструктор """

        super(SectionComplications, self).__init__(Keys.COMPLICATIONS, Keys.COMPLICATION)
