#  12. Будильник
from datetime import datetime
from playsound import playsound


def validate_time(alarm_time):
    if len(alarm_time) != 8:
        return "Неверный формат"
    if int(alarm_time[0:2]) > 23:
        return "Лишние часы"
    elif int(alarm_time[3:5]) > 59:
        return "Слишком много минут"
    elif int(alarm_time[6:8]) > 59:
        return "Слишком много секунд"
    else:
        return "ok"


while True:
    alarm_time = input("Введи время будильника в формате 'HH:MM:SS' \nВремя будильника: ")
    validate = validate_time(alarm_time)
    if validate != "ok":
        print(validate)
    else:
        print(f"Будильник установлен на {alarm_time}")
        break

alarm_hour = int(alarm_time[0:2])
alarm_min = int(alarm_time[3:5])
alarm_sec = int(alarm_time[6:8])

while True:
    now = datetime.now()

    current_hour = now.hour
    current_min = now.minute
    current_sec = now.second

    if alarm_hour == current_hour:
        if alarm_min == current_min:
            if alarm_sec == current_sec:
                print("О мАй О мАй гАд~~")
                playsound('NewJeans - OMG.mp3')
                break
