from sql import docs, patients, appointments, med_history, SQL, docs_data
from classes import Patient, Doctor
from utilit import valid

def patientActions(user, id):
    while True:
        choice = valid("1 - посмотреть все свои записи\n"
                       "2 - новая запись\n"
                       "3 - отменить запись\n"
                       "4 - перенести запись\n"
                       "5 - посмотреть историю болезни\n"
                       "6 - выйти\n"
                       "Выбор: ", "int", [1, 2, 3, 4, 5, 6])
        if choice == 1:
            user.showAppointment(id)
        elif choice == 2:
            user.newAppointment(id)
        elif choice == 3:
            user.cancellation(id)
        elif choice == 4:
            user.reschedule(id)
        elif choice == 5:
            user.checkHistory(id)
        else:
            break


def main(user):
    if type(user) == Doctor:
        doc.authorization()
        id = doc.get()[0]
        while True:
            response = valid("1 - посмотреть все записи\n"
                             "2 - начать прием\n"
                             "3 - выйти\n"
                             "Выбор:", "int", [1, 2, 3])
            if response == 1:
                user.showAppointments(id)
            elif response == 2:
                user.startAppoinments(id)
            else:
                break
    else:
        response = valid("1 - войти\n"
                         "2 - зарегистрироваться\n"
                         "Выбор: ", "int", [1, 2])
        if response == 1:
            user.authorization()
            id = user.get()[0]
            patientActions(user, id)
        else:
            user.registration()
            id = user.get()[0]
            patientActions(user, id)

if __name__ == "__main__":
    sql = SQL("clinic.sqlite")
    sql.table("docs", docs)
    sql.table("patients", patients)
    sql.table("appointments", appointments)
    sql.table("med_histories", med_history)
    for data in docs_data:
        sql.add("docs", data)
    print("Добрый день!")
    user = valid("1 - войти как врач\n"
                 "2 - войти как пациент\n"
                 "Выбор:", "int", parametrs=[1, 2])
    if user == 1:
        doc = Doctor(sql)
        main(doc)
    else:
        patient = Patient(sql)
        main(patient)








