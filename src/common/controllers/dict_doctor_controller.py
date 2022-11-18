from ...dict.doctors.models.doctor_model import DoctorModel


class ControllerDictDoctor:
    """ Контроллерю Справочник докторов """

    def select(self):
        """ Получение списка вречей
        :return: Список моделей врачей
        """

        return None

    def get(self, kode):
        """ Получение врача по коду
        :param kode: Код врача
        :return: Модель. Врач
        """

        try:
            doctor = DoctorModel(1, "Иванов", "Иван", "Иванович")

            print(f"Добавление врача: f{doctor}")
            return True
        except Exception as e:
            message = "Ошибка добавления врача"
            print(message, e)
            raise Exception(message)


        return doc

    def create(self, doctor: DoctorModel):
        """ Добавление сущности Врач
        :param doctor: Модель - Врач
        :return: Результат выполнения
        """

        try:
            print(f"Добавление врача: f{doctor}")
            return True
        except Exception as e:
            message = "Ошибка добавления врача"
            print(message, e)
            raise Exception(message)

    def update(self, doctor: DoctorModel):
        """ Обновление сущности Врач
        :param doctor: Модель - Врач
        :return: Результат выполнения
        """

        try:
            print(f"Изменим врача: f{doctor}")
            return True
        except Exception as e:
            message = "Ошибка изменения врача"
            print(message, e)
            raise Exception(message)

    def delete(self, doctor: DoctorModel):
        """ Удаление сущности Врач
        :param doctor: Модель - Врач
        :return: результат выполнения
        """

        try:
            print(f"Удалим врача: f{doctor}")
            return True
        except Exception as e:
            message = "Ошибка удаления врача"
            print(message, e)
            raise Exception(message)



