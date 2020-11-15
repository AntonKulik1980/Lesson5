# Создать подобие социальной сети.
# 1) Создать класс авторизации, в котором описать методы регистрации, аутентификации, добавить
# методы проверки на валидность пароля (содержание символов и цифр), "проверка на уникальность
# логина пользователя". В классовых переменных хранить всех пользователей сети. (Отдельно
# объекты этого класса создаваться не будут, такие классы называются миксинами)
# 2) Создать класс пользователя, наследующий класс авторизации. который будет разделять роли
# админа и простого пользователя (этот вопрос можно решить с помощью флага is_admin, либо
# создав 2 разных класса для админа и обычного пользователя и наследовать их). Класс
# пользователя должен наследовать класс авторизации. На момент создания каждого объекта этого
# класса, в переменную объекта сохранять время и дату его создания.
# 3) Создать класс поста, который имеет дату публикации и её содержимое.
# Что должно быть в клиентском коде:
# Человек заходит, и имеет возможность зарегистрироваться (ввод логин, пароль, подтверждение
# пароля), далее входит в свою учетную запись. Добавить возможность выхода из учетной записи, и
# вход в новый аккаунт.
# При входе под обычным пользователем мы можем создать новый пост, с определённым
# содержимым. Под учётной записью администратора мы можем увидеть всех пользователей нашей
# системы, дату их регистрации, и их посты.

from abc import ABC, abstractmethod
from datetime import datetime


class autho(ABC):
    users = []

    SpecialSym = ['$', '@', '#', '%']
    val = True

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @classmethod
    def login_pop(cls):
        users_logins = dict([x for x in cls.users])
        return users_logins

    def register(self):

        if len(self.password) < 6:
            print('length should be at least 6')

        if len(self.password) > 20:
            print('length should be not be greater than 8')

        if not any(char.isdigit() for char in self.password):
            print('Password should have at least one numeral')

        if not any(char.isupper() for char in self.password):
            print('Password should have at least one uppercase letter')

        if not any(char.islower() for char in self.password):
            print('Password should have at least one lowercase letter')

        if not any(char in self.SpecialSym for char in self.password):
            print('Password should have at least one of the symbols $@#')

        if list(filter(lambda i: i['login'] == self.login, self.users)):
            raise ValueError('Login is duplicate existing records, please try again')
        else:
            j = input('Please retype your password')
            if j == self.password:
                autho.users.append(dict(login=self.login, password=self.password))
                post.post_from_input()


class User(autho, ABC):
    actual_users = []

    def __init__(self, login, password, isadmin):
        super().__init__(login, password)
        self.isadmin = isadmin
        self.actual_users.append(dict(login=self.login, password=self.password, isadmin=self.isadmin,
                                      timestamp=datetime.timestamp(datetime.now())))

    @classmethod
    def reg_from_input(cls):
        return cls(
            input('Login:'),
            input('password:'),
            input('Is admin ?: ')
        )

    @classmethod
    def is_admin(cls):
        return list(filter(lambda i: i['isadmin'] == 1, cls.actual_users))

    @classmethod
    def enter(cls, login, password):

        if filter(lambda i: i['login'] == cls.login, User.actual_users) and filter(
                lambda i: i['password'] == cls.password, User.actual_users):
            post.post_from_input()
        else:
            raise ValueError('No such login and passowrd combination')

    @classmethod
    def enter_from_input(cls):
        return cls(
            input('Login:'),
            input('password:')
        )

class post(User):

    def __init__(self, text, date=datetime.now()):

        self.text = text
        self.date = datetime.now()

    @classmethod
    def post_from_input(cls):
        return cls(input('enter your text: '))

    def get_post(self):
        return self.text, self.date


User.reg_from_input().register()

# User('Anton', '121@asQW', 1).register()
# User('Anton1', '122@asQW', 0).register()
# User('Anton2', '123@asQW', 0).register()
# User('Anton3', '124@asQW', 1).register()
# User('Anton4', '125@asQW', 0).register()
# User('Anton4', '125@asQW', 0).register()
# print(autho.users)
# # print(autho.login_pop())
# print(User.is_admin())
#
# i = post('spknaoldfn')
# print(post.get_post(i))
