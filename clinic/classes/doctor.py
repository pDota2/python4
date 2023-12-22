from .User import User
from clinic.utilit import valid


class Doctor(User):
    def __init__(self, sql):
        super().__init__(sql)
        self.__id, self.__login = super().get()

    def showAppointments(self, id):
        print("Все приемы к Вам:")
        appointments = self.sql.select_where("appointments", {"doc_id": id, "close": False})
        ids = []
        patients = []
        if appointments:
            for apnms in appointments:
                ids.append(apnms[0])
                patients.append(apnms[1])
                patient = self.sql.select_where("patients", {"id": apnms[1]})[-1]
                print(f"Номер записи: {apnms[0]}\n"
                      f"На {apnms[3]}\n"
                      f"Кто: {patient[3]}\n"
                      f"Информация о пациенте:\n"
                      f"Пол: {patient[4]}\n"
                      f"Полных лет: {patient[6]}\n"
                      f"-------------------")
        else:
            print("К Вам никто не записан")
        return ids, patients

    def startAppoinments(self, id):
        ids, patients = self.showAppointments(id)
        if ids:
            print("Для начала приема введите номер записи")
            appointmentID = valid("Введите номер записи: ", "int", parametrs=ids)
            diagnosis = valid("Введите диагноз: ", "str")
            treatment = valid("Введите все лечение для пациента: ", "str")
            data = {
                "diagnosis": diagnosis,
                "treatment": treatment,
                "appointment_id": appointmentID
            }
            self.sql.add("med_histories", data)
            appointment = {
                "close": True
            }
            self.sql.update("appointments", appointment, {"doc_id": id})
            print("Прием завершен")
        else:
            print("Вы не можете начать прием")



