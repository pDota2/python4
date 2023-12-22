from datetime import datetime


def valid(prompt, paramType, parametrs=None, constr=None):
    while True:
        if constr:
            answer = input(prompt)
            validor = checkType(answer, paramType, constr)
            if validor:
                return answer
        elif parametrs:
            answer = input(prompt)
            validor = checkType(answer, paramType)
            if validor:
                answer = int(answer)
                if answer in parametrs:
                    return answer
                else:
                    print("Нет такого ответа")
        else:
            answer = input(prompt)
            validor = checkType(answer, paramType)
            if validor:
                if paramType == "int":
                    return int(answer)
                elif paramType == "date":
                    return datetime.strptime(answer, "%d.%m.%Y").strftime("%d.%m.%Y")
                elif paramType == "time":
                    return datetime.strptime(answer, "%H:%M").strftime("%H:%M")
                else:
                    return answer


def checkType(string, paramType, constr=None):
    if paramType == "str":
        if constr:
            if (len(string) > 0) and (len(string) < constr):
                return True
            else:
                print(f"Ввод должен быть меньше {constr}")
                return False
        else:
            if len(string) > 0:
                return True
            else:
                print("Вы не можете оставить значние пустым")
                return False
    elif paramType == "int":
        try:
            num = int(string)
            return True
        except:
            print("Ввод должен быть числом")
            return False
    elif paramType == "date":
        try:
            datetime.strptime(string, "%d.%m.%Y")
            return True
        except:
            print("Необходимо ввести дату в формате дд.мм.гггг")
    elif paramType == "time":
        try:
            datetime.strptime(string, "%H:%M")
            return True
        except:
            print("Необходимо ввести время в формате 16:30/чч:мм")
            return False



