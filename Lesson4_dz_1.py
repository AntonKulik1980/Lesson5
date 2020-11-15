# Создайте класс ПЕРСОНА с абстрактным методом, позволяющим вывести
# на экран информацию о персоне, а также реализовать обычный метод
# определения возраста (в текущем году). Создайте дочерние классы:
# АБИТУРИЕНТ (фамилия, дата рождения, факультет), СТУДЕНТ (фамилия,
# дата рождения, факультет, курс), ПРЕПОДАВАТЕЛЬ (фамилия, дата
# рождения, факультет, должность, стаж), со своими методами возврата
# информации. Создайте список из объектов персон, вывести информацию о
# каждом объекте, а также организуйте поиск персон, чей возраст попадает в
# заданный с клавиатуры диапазон.

from abc import ABC, abstractmethod
from datetime import date


class Person(ABC):
    person_list = list()

    def __init__(self, date, surname, faculty):
        self.time = date
        self.surname = surname
        self.faculty = faculty
        self.age = Person.calculate_age(self)
        Person.person_list.append(dict(date=self.time.year, surname=self.surname, faculty=self.faculty, age=self.age))

    def calculate_age(self):
        today = date.today()
        date_this_year = date(today.year, self.time.month, self.time.day)
        return today.year - self.time.year - (date_this_year > today)

    def search_by_age(self, value):
        if self.age == value:
            print(Person)

    @abstractmethod
    def get_person_data(self):
        pass

    def get_person_data(self):
        print(f'{__class__.__name__} surmane is {self.surname} year of birth is {self.time.year}  month number '
              f'is {self.time.month} '
              f'and desiered faculty is {self.faculty} ')
    @classmethod
    def search_by_age(cls, value_min,value_max):
        return list(filter(lambda n: value_max >= n['age'] >= value_min, cls.person_list))

    @classmethod
    def all_persons_list(cls):
        print(cls.person_list)


class Abiturient(Person, ABC):

    def get_person_data(self):
        print(f'{__class__.__name__} surmane is {self.surname} year of birth is {self.time.year}  month number '
              f'is {self.time.month} '
              f'and desiered faculty is {self.faculty} ')


class Student(Person, ABC):

    def __init__(self, date, surname, faculty, kurs):
        super().__init__(surname, faculty, date)
        self.kurs = kurs

    def get_person_data(self):
        print(f'{__class__.__name__} surmane is {self.surname} year of birth is {self.time.year}  month number is '
              f'{self.time.month} '
              f' faculty is {self.faculty} kurs is {self.kurs} ')


class Profesor(Person, ABC):

    def __init__(self, date, surname, faculty, kurs, position, work_years):
        super(Profesor, self).__init__(date, surname, faculty)
        self.position = position
        self.work_years = work_years
        self.kurs = kurs

    def get_person_data(self):
        print(f'{__class__.__name__} surmane is {self.surname} year of birth is {self.time.year}  month number is '
              f'{self.time.month} '
              f' faculty is {self.faculty} kurs is {self.kurs}, on possition of {self.position}, '
              f'for {self.work_years} years ')


me = Person(date(1980, 10, 12), 'Petrov', 'FTTS')
me1 = Person(date(1985, 10, 12), 'Sidorov', 'FTTS')
me2 = Person(date(1982, 10, 12), 'Ivanov', 'FTTS')

print(Person.search_by_age(40,50))

Person.all_persons_list()



# Profesor(date(1980,1,22),'Sidorov','FTTS',3,'master Yoda',30).get_person_data()


# me = Abiturient(date(1980, 11, 4), 'Ivanov', 'FTTS')
# print(me.get_person_data())
#
# me2 = Student(date(1980, 11, 4), 'Ivanov', 3, 'FTTS')
# print(me2.get_person_data())


#
# me = Person(date(1980, 10, 2), 'Kulik', 'FTTS')
# print(me.calculate_age())
