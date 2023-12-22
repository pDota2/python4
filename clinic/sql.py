import sqlite3


docs = {"id": "integer primary key autoincrement",
        "fullname": "text unique",
        "login": "varchar(20) unique",
        "password": "varchar(20)",
        "specialty": "text"}
patients = {
    "id": "integer primary key autoincrement",
    "login": "varchar(20) unique",
    "password": "varchar(20)",
    "fullname": "text unique",
    "sex": "varchar(10)",
    "birthday": "text",
    "age": "integer"
}
appointments = {"id": "integer primary key autoincrement",
                "patient_id": "integer",
                "doc_id": "integer",
                "date_time": "date",
                "close": "boolean",
                "foreign key (patient_id) references patients(id)": "",
                "foreign key (doc_id) references docs(id)": ""}
med_history = {
    "id": "integer primary key autoincrement",
    "diagnosis": "text",
    "treatment": "text",
    "appointment_id": "integer",
    "foreign key": "(appointment_id) references appointments"
}

docs_data = [{
    "login": "agg",
    "password": "agg",
    "fullname": "Аязов Геогр Геворгянович",
    "specialty": "терапевт"
}, {
    "login": "tlp",
    "password": "tlp",
    "fullname": "Требов Леван Петрович",
    "specialty": "окулист"
}, {
    "login": "vpi",
    "password": "vpi",
    "fullname": "Виноградов Петр Иванович",
    "specialty": "кардиолог"
}, {
    "login": "psl",
    "password": "psl",
    "fullname": "Перов Сергей Леонидович",
    "specialty": "трихолог"
}, {
    "login": "sda",
    "password": "sda",
    "fullname": "Шопов Дмитрий Андреевич",
    "specialty": "психиатр"
}, {
    "login": "laa",
    "password": "laa",
    "fullname": "Леопов Алексей Алексеич",
    "specialty": "оториналоринголог"
}, {
    "login": "vna",
    "password": "vna",
    "fullname": "Вастенов Никита Александрович",
    "specialty": "офтальмолог"
}]


class SQL:
    def __init__(self, db_file):
        self.connect = sqlite3.connect(db_file)
        self.cursor = self.connect.cursor()

    def table(self, table, params):
        columns = ', '.join(f"{column} {param}" for column, param in params.items())
        query = f"create table if not exists {table}({columns});"
        try:
            with self.connect:
                self.cursor.execute(query)
        except Exception as e:
            pass

    def select(self, table, columns='*'):
        try:
            column = ", ".join(columns)
            query = f"select {column} from {table}"
            with self.connect:
                return self.cursor.execute(query).fetchall()
        except:
            pass

    def select_where(self, table, where, columns='*'):
        try:
            column = ', '.join(columns)
            parametrs = ' and '.join(f"{key} = ?" for key in where.keys())
            query = f"select {column} from {table} where {parametrs}"
            with self.connect:
                return self.cursor.execute(query, list(where.values())).fetchall()
        except:
            pass

    def update(self, table, columns, where):
        try:
            column = ', '.join(f"{value} = ?" for value in columns.keys())
            parametrs = " and ".join(f"{param} = ?" for param in where.keys())
            values = list(columns.values())
            values += list(where.values())
            query = f"update {table} set {column} where {parametrs}"
            with self.connect:
                self.cursor.execute(query, values)
        except:
            pass

    def add(self, table, columns):
        try:
            holders = ", ".join("?" for _ in columns.keys())
            column = ", ".join(f"{key}" for key in columns.keys())
            query = f"insert into {table} ({column}) values ({holders})"
            with self.connect:
                self.cursor.execute(query, list(columns.values()))
        except:
            pass

    def remove(self, table, columns):
        try:
            column = " and ".join(f"{key} = ?" for key in columns.keys())
            query = f"delete from {table} where {column}"
            with self.connect:
                self.cursor.execute(query, list(columns.values()))
        except:
            pass

