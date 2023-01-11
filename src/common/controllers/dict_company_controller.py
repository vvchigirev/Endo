from ..Exceptions.business_exception import BusinеssException
from ...dict.insuranсe_company.model.company_model import CompanyModel
from ...common.data.xml.entitys.xml_companys import XmlCompanys


class ControllerDictCompany:
    """ Контроллер Справочник страховых компаний """

    __xml_companys: XmlCompanys = None  # Xml структур для Страховых компаний

    def __init__(self):
        """ Конструктор """

        print(": ControllerDictCompany.__init__()")

        self.__xml_companys = XmlCompanys()

    def select_companys(self):
        """Получение списка страховых компаний
        :return список страховых компаний
        """

        print(": ControllerDictCompanys.select_companys()")

        companys = []

        try:
            return self.__xml_companys.select_companys()
        except Exception as e:
            message = "Ошибка получения списка страховых компаний!"
            print(message, e)
            raise BusinеssException(message)

        return companys

    def get_company(self, code):
        """ Получение Страховой компании по коду
        :param code: Код страховой компании
        :return: Модель. Страховая компания
        """

        try:
            if code != "" or code is not None:
                company = self.__xml_companys.get_company(code)
                return company

            return None
        except Exception as e:
            message = "Ошибка получения страховой компании!"
            print(message, e)
            raise BusinеssException(message)

    def create_company(self, company: CompanyModel):
        """ Добавление сущности Страховая компания
        :param company: Модель - Страховая компания
        :return: Результат выполнения
        """

        print(": ControllerDictCompany.create_company()")

        print(f"Добавления страховой компании f{company}")

        try:
            if self.__xml_companys.get_company(company.code):
                print(f"Страховая компания с кодом f{company.code} уже существует")
                return False

            if not self.__xml_companys.creat_company(company):
                print("Страховая компания не добавлен")
                return False

            return True
        except Exception as e:
            message = "Ошибка ошибка добавления страховой компании!"
            print(message, e)
            raise BusinеssException(message)

    def update_company(self, company: CompanyModel):
        """ Обновление сущности Страховая компания
        :param company: Модель - Страховая компания
        :return: Результат выполнения
        """

        print(": ControllerDictCompany.update_company()")
        try:
            if not self.get_company(company.code):
                print(f"Страховой компании с кодом f{company.code} не существует")
                return False

            if not self.__xml_companys.update_company(company):
                print("страховая компания не изменен")
                return False

            return True
        except Exception as e:
            message = "Ошибка изменения страховой компании!"
            print(message, e)
            raise BusinеssException(message)

    def delete_company(self, code):
        """ Удаление сущности Страховая компания
        :param code: Код страховой компании
        :return: Результат выполнения
        """
        print(": ControllerDictDoctor.delete_doctor()")

        try:
            company = self.get_company(code)
            if not company:
                print(f"Страховой компании с кодом f{company} не найдено")

            try:
                if company and self.__xml_companys.delete_company(code):
                    return True
                return False

            except Exception as e:
                message = "Ошибка удаления страховой компании"
                print(message + ": ", e)
                raise BusinеssException(message)

        except Exception as e:
            message = "Ошибка удаления страховой компании!"
            print(message, e)
            raise BusinеssException(message)
