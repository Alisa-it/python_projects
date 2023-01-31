#  34. Класс пациент и доктор, расписание
class Hospital:
    def __init__(self, dtype):
        self.__dtype = dtype

    @property
    def dtype(self):
        return self.__dtype

    @dtype.setter
    def dtype(self, t):
        self.__dtype = t


class Doctor(Hospital):
    def __init__(self, dtype, name, room, time):
        super().__init__(dtype)
        self.__name = name
        self.__room = room
        self.__time = time

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    @property
    def room(self):
        return self.__room

    @room.setter
    def room(self, r):
        if r > 0:
            self.__room = r

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, t):
        if len(t) > 0:
            self.__time = t

    def to_sign_up(self):
        return f'{pat.name}, Вы записаны к {self.dtype}у {self.name} на {pat.time}. Кабинет {self.room}'


class Patient(Hospital):
    def __init__(self, name, dtype, time):
        self.__name = name
        super().__init__(dtype)
        self.__time = time

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, t):
        self.__time = t


docs = {
    0: Doctor("терапевт", "Анастасия П.", 21, ["8:00", "10:00", "12:00", "13:00", "17:00"]),
    1: Doctor("хирург", "Александр А.", 13, ["9:00", "11:00", "12:00", "13:00"]),
    2: Doctor("педиатор", "Ольга О.", 4, ["10:00", "13:00", "15:00", "19:00"]),
    3: Doctor("офтальмолог", "Семён Л.", 10, ["9:00", "10:00", "12:00", "18:00"]),
    4: Doctor("стоматолог", "Юрий Т.", 29, ["10:00", "13:00", "15:00", "16:00"])
}

pats = {
    0: Patient("Алексей", "терапевт", '10:00'),
    1: Patient("Анна", "педиатор", '15:00'),
    2: Patient("Георгий", "стоматолог", '13:00')
}

while True:

    your_name = input('Введите своё имя: ')

    doc_list = []
    for i in range(len(docs)):
        if docs.get(i).dtype not in doc_list:
            doc_list.append(docs.get(i).dtype)
    your_doc = input(f'Выберите направление из списка: {", ".join(doc_list)}\n- ')
    for i in range(len(docs)):
        if your_doc == docs.get(i).dtype:
            doc_id = i
            break

    time_list = []
    d = docs.get(doc_id)
    for i in range(len(d.time)):
        time_list.append(d.time[i])

    for j in range(len(pats)):
        if (pats.get(j).dtype == d.dtype) and (pats.get(j).time in time_list):
            time_list.remove(pats.get(j).time)

    your_time = input(f'Выберите время из списка: {" - ".join(time_list)}\n- ')

    pat = Patient(your_name, your_doc, your_time)
    pats[len(pats)] = pat
    print(docs.get(doc_id).to_sign_up())
