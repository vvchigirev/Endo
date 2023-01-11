from ....base_classes.base_sections import BaseSections
from ....consts.Keys import Keys


class SectionOrgans(BaseSections):
    """ Наименовая блоков элементов для справочника Органов """

    def __init__(self):
        """ Конструктор """

        super(SectionOrgans, self).__init__(Keys.ORGANS, Keys.ORGAN)

