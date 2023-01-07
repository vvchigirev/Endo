from ...base_classes.base_sections import BaseSections
from ...consts.Keys import Keys


class SectionIEndos(BaseSections):
    """ Наименовая блоков элементов для справочника Приборов """

    def __init__(self):
        """ Конструктор """

        super(SectionIEndos, self).__init__(Keys.IENDOS, Keys.IENDO)
