"""Описать класс, содержащий информацию об одном из понятий реального мира (не менее 4 свойств)
согласно индивидуального задания и примените к нему декоратор @property. Изменение значения
свойств осуществите с помощью сеттеров этих свойств См. Лекция 3_1. Определение классов и
создание экземпляра класса
Продемонстрируйте работу декоратора через задание свойств объекта класса конструктором, сеттером
и непосредственным изменением значения (должно вызвать ошибку).
"""
class Classroom:#новый класс Classroom
    def __init__(self, number, seats, type, projector):#конструктор с параметрами number, seats, type, projector
        self._number = number
        self._seats = seats
        self._type = type
        self._projector = projector#инициализируем параметры

    @property#декторатор property
    def number(self):
        return self._number#функция номера аудитории возвращаем номер

    @number.setter#декторатор setter
    def number(self, value):
        self._number = value#функция номера аудитории возвращаем value

    @property#декторатор property
    def seats(self):
        return self._seats#функция количества мест возвращаем места

    @seats.setter#декторатор setter
    def seats(self, value):
        self._seats = value#функция количества мест возвращаем value

    @property#декторатор property
    def type(self):
        return self._type#функция типа аудитории возвращаем номер

    @type.setter#декторатор setter
    def type(self, value):
        self._type = value#функция типа аудитории возвращаем value

    @property#декторатор property
    def projector(self):
        return self._projector#функция прожектора возвращаем номер

    @projector.setter#декторатор setter
    def projector(self, value):
        self._projector = value#функция прожектора возвращаем value


# Пример использования класса Classroom

# Создаем объект класса Classroom и задаем его свойства через конструктор
classroom1 = Classroom("101", 30, "лекционная", True)

#изменяем свойства объекта с использованием сеттеров
classroom1.number = "102"
classroom1.seats = 35
classroom1.type = "практическая"
classroom1.projector = False

#выводим значения свойств объекта с использованием доступа через геттеры
print(f"Номер аудитории: {classroom1.number}")
print(f"Количество мест: {classroom1.seats}")
print(f"Тип аудитории: {classroom1.type}")
print(f"Наличие проектора: {classroom1.projector}")

#пробуем изменить значение свойств объекта
classroom1._number = "103"  #вызовет ошибку т к доступ к свойству должен осуществляться через сеттер