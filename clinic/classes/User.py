from clinic.utilit import valid


class User:
    def __init__(self, sql):
        self.__id = None
        self.__login = None
        self.sql = sql

    def authorization(self):
        while True:
            login = valid("Логин: ", "str", constr=20)
            password = valid("Пароль: ", "str", constr=20)
            patients = self.sql.select("patients")
            docs = self.sql.select("docs")
            d_logins = []
            p_logins = []
            for p in patients:
                p_logins.append(p[1])
            for d in docs:
                d_logins.append(d[2])
            if login in p_logins:
                p = self.sql.select_where("patients", {"login": login})[-1]
                if password == p[2]:
                    print(f"Приветствуем {p[3]}!")
                    self.__id = p[0]
                    self.__login = p[1]
                    break
                else:
                    print("Неверный пароль")
            elif login in d_logins:
                d = self.sql.select_where("docs", {"login": login})[-1]
                if password == d[3]:
                    print(f"Приветствуем {d[1]}!")
                    self.__id = d[0]
                    self.__login = d[2]
                    break
                else:
                    print("Неверный пароль")
            else:
                print("Такого логина не существует")

    def registration(self):
        login = ""
        while True:
            print("Добрый день! Давайте зарегистрируемся!")
            login = valid("Придумайте логин: ", "str", constr=20)
            patients = self.sql.select("patients")
            docs = self.sql.select("docs")
            logins = []
            for p in patients:
                logins.append(p[1])
            for d in docs:
                logins.append(d[2])
            if login not in logins:
                break
            else:
                print("Этот логин уже занят")
        password = valid("Придумайте пароль: ", "str", constr=20)
        fullname = valid("Введите Ваше ФИО: ", "str")
        response = valid("Укажите Ваш пол: \n"
                        "1 - мужской\n"
                        "2 - женский\n"
                        "Пол: ", "int", parametrs=[1, 2])
        sex = ""
        if response == 1:
            sex = "мужской"
        else:
            sex = "женский"
        birthday = valid("Введите Вашу дату рождения: ", "date")
        age = valid("Введите количество полных лет: ", "int")
        data = {
            "login": login,
            "password": password,
            "fullname": fullname,
            "sex": sex,
            "birthday": birthday,
            "age": age
        }
        self.sql.add("patients", data)
        print(f"{fullname}, добро пожаловать!")

    def get(self):
        return self.__id, self.__login


