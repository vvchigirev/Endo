from ...base_classes.base_sections import BaseSections
from ...consts.Keys import Keys


class SectionReasons(BaseSections):
    """ Наименования блоков элементов для справочника причин обращения """

    def __init__(self):
        """ Конструктор """

        super(SectionReasons, self).__init__(Keys.REASONS, Keys.REASON)
