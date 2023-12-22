from .User import User
from clinic.utilit import valid


class Patient(User):
    def __init__(self, sql):
        super().__init__(sql)
        self.__id, self.__login = super().get()

    def showAppointment(self, id):
        print("Все Ваши приемы:")
        appointments = self.sql.select_where("appointments", {"patient_id": id, "close": False})
        ids = []
        if appointments:
            for apnms in appointments:
                ids.append(apnms[0])
                doc = self.sql.select_where("docs", {"id": apnms[2]})[-1]
                print(f"Номер записи: {apnms[0]}\n"
                      f"К: {doc[4]}\n"
                      f"Врач: {doc[1]}\n"
                      f"Дата: {apnms[3]}"
                      f"-----------------")
        else:
            print("Вы ни к кому не записаны")
        return ids

    def newAppointment(self, id):
        docs = self.sql.select("docs")
        docs_id = []
        print("Выберите врача: ")
        for doc in docs:
            docs_id.append(doc[0])
            print(f"{doc[0]}: {doc[4]}")
        specialty = docs[valid("Выберите врача: ", "int", parametrs=docs_id) - 1][4]
        docs = self.sql.select_where("docs", {"specialty": specialty})
        print("Выберите доктора: ")
        docs_id = []
        for doc in docs:
            docs_id.append(doc[0])
            print(f"{doc[0]} - {doc[2]}")
        doc_id = valid("Выберите доктора: ", "int", parametrs=docs_id)
        date = valid("Введите дату приема: ", "date")
        time = valid("Введите время приема: ", "time")
        date_time = f"{date} {time}"
        print(self.__id)
        data = {
            "doc_id": doc_id,
            "patient_id": id,
            "date_time": date_time,
            "close": False
        }
        self.sql.add("appointments", data)
        doc = self.sql.select_where("docs", {"id": doc_id})[-1]
        print(f"Успешная запись"
              f"\nК врачу: {specialty}\n"
              f"К доктору: {doc[1]}\n"
              f"На дату: {date_time}")

    def cancellation(self, id):
        ids = self.showAppointment(id)
        if ids:
            appointment = valid("Введите номер записи для отмены: ", "int", ids)
            self.sql.remove("appointments", {"id": appointment})
            print("Запись успешно отменена")
        else:
            print("Вы не можете отменить запись")

    def reschedule(self, id):
        ids = self.showAppointment(id)
        if ids:
            appointment = valid("Введите номер записи для переноса: ", "int", ids)
            date = valid("Введите новую дату приема: ", "date")
            time = valid("Введите новое время приема: ", "time")
            date_time = f"{date} {time}"
            data = {
                "date_time": date_time
            }
            self.sql.update("appointments", data, {"id": appointment})
            print(f"Запись успешна перенесена на {date_time}")
        else:
            print("Вы не можете перенести запись")

    def checkHistory(self, id):
        print("Все Ваши приемы:")
        appointments = self.sql.select_where("appointments", {"patient_id": id, "close": True})
        ids = []
        if appointments:
            for apnms in appointments:
                ids.append(apnms[0])
                doc = self.sql.select_where("docs", {"id": apnms[2]})[-1]
                print(f"Номер записи: {apnms[0]}\n"
                      f"К: {doc[4]}\n"
                      f"Врач: {doc[1]}\n"
                      f"Дата: {apnms[3]}\n"
                      f"-----------------")
        else:
            print("Вы не были ни к кому записаны")
        if ids:
            appointment = valid("Введите номер записи для просмотра информации: ", "int", ids)
            history = self.sql.select_where("med_histories", {"appointment_id": appointment})[-1]
            print(f"Информация по записи под номером {appointment}\n"
                  f"Диагноз: {history[1]}\n"
                  f"Лечение: {history[2]}")
        else:
            print("Вы не можете посмотреть историю")




