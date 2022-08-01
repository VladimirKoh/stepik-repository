# #Степик курс задание 1.4
# class Video:
#     def create(self, name):
#         self.name = name
#
#     def play(self):
#         print(f'воспроизведение видео {self.name}')
#
#
# class YouTube:
#     new_list = []
#     @classmethod
#     def add_video(cls, video):
#         cls.new_list.append(video)
#
#     @classmethod
#     def play(cls, video_indx):
#         cls.new_list[video_indx].play()
#
#
# v1 = Video()
# v2 = Video()
#
# v1.create('Python')
# v2.create('Python ООП')
#
# YouTube.add_video(v1)
# YouTube.add_video(v2)
# YouTube.play(1)
# #задание переводчик
# class Translator:
#     dict_translate = {}
#     def add(self, eng, rus):
#         if eng in Translator.dict_translate.keys() and rus not in Translator.dict_translate[eng]:
#             Translator.dict_translate[eng].append(rus)
#         else:
#             Translator.dict_translate[eng] = [rus]
#
#     def remove(self, eng):
#         del Translator.dict_translate[eng]
#
#     def translate(self, eng):
#         return Translator.dict_translate[eng]
#
#
# tr = Translator()
# tr.add("tree", "дерево")
# tr.add("car", "машина")
# tr.add("car", "автомобиль")
# tr.add("leaf", "лист")
# tr.add("river", "река")
# tr.add("go", "идти")
# tr.add("go", "ехать")
# tr.add("go", "ходить")
# tr.add("milk", "молоко")
# tr.remove('car')
# print(*tr.translate('go'))
# #Задание 1000 точек
# class Point:
#     def __init__(self, x, y, color='black'):
#         self.x = x
#         self.y = y
#         self.color = color
#
#
# points = [Point(i, i) if i != 3 else Point(i, i, 'yellow') for i in range(1, 2000, 2)]
# print(points[1].color)


# # Задание 3 класса геометрических фигур
# import random
#
# class Line:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# class Rect:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# class Ellipse:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# random_a_b_c_d = random.choices([i for i in range(100)], k=4)
# list_class = [Line(0, 0, 0, 0), Rect(*random_a_b_c_d), Ellipse(*random_a_b_c_d)]
# elements = [random.choice(list_class) for i in range(217)]

# Задание триангуляр
# import numbers
# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         if type(a) != int:
#             return 1
#         elif not sorted([a,b,c])[2] < sorted([a,b,c])[0] + sorted([a,b,c])[1]:
#             return 2
#         else:
#             return 3
#
#
#
#
# a, b, c = input().split()
# tr = TriangleChecker(a, b, c)
# print(tr.is_triangle())
# Задание-----
# class Graph:
#     def __init__(self, data, is_show=True):
#         self.data = data
#         self.is_show = is_show
#
#     def set_data(self, data):
#         self.data = data
#
#     def show_table(self):
#         if not self.is_show:
#             print('Отображение данных закрыто')
#         else:
#             print(*self.data)
#
#     def show_graph(self):
#         if not self.is_show:
#             print('Отображение данных закрыто')
#         else:
#             print('Графическое отображение данных:', *self.data)
#
#     def show_bar(self):
#         if not self.is_show:
#             print('Отображение данных закрыто')
#         else:
#             print('Столбчатая диаграмма:', *self.data)
#
#     def set_show(self, fl_show):
#         self.is_show = fl_show
#
#
# data_graph = list(map(int, input().split()))
#
# gr = Graph(data_graph)
# gr.show_bar()
# gr.set_show(False)
# gr.show_table()


# Задание 15.7
# class CPU:
#     def __init__(self, name, fr):
#         self.name = name
#         self.fr = fr
#
#
# class Memory:
#     def __init__(self, name, volume):
#         self.name = name
#         self.volume = volume
#
#
#
# class MotherBoard:
#     total_mem_slots = 4
#     def __init__(self, name, cpu, *args):
#         self.name = name
#         self.cpu = cpu
#         self.mem_slots = args
#
#     def get_config(self):
#         list_config = []
#         list_config.append(f'Материнская плата: {self.name}')
#         list_config.append(f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}')
#         list_config.append(f'Слотов памяти {MotherBoard.total_mem_slots}')
#         list_config.append(f"Память: {'; '.join([f'{i.name} - {i.volume}' for i in self.mem_slots])}")
#         return list_config
#
#
# mb = MotherBoard('Zalupa', CPU('RAYZEN', 5000), Memory('Kingston', 1333), Memory('Kingston', 1333))
# print(mb.get_config())

# Задание 15-8
# class Cart:
#     def __init__(self):
#         self.goods = []
#
#     def add(self, gd):
#         """#- добавление товара в корзину, представленного объектом gd;"""
#         self.goods.append(gd)
#
#     def remove(self, indx):
#         """- удаление товара из корзины по индексу indx;"""
#         del self.goods[indx]
#
#     def get_list(self):
#         """- получение товаров корзины в виде списка из строк:"""
#         return [f"{g.name}: {g.price}" for g in cart.goods]
#
#
# class Table:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class TV:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Notebook:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Cup:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# cart = Cart()
#
# cart.add(TV('Сосунг', 56000))
# cart.add(TV('ЛДЖО', 145000))
# cart.add(Table('Дубок', 14000))
# cart.add(Notebook('Macbook', 145000))
# cart.add(Notebook('Рашенбук', 500000))
# cart.add(Cup('Кружка для пива', 300))
#
# print([f"{g.name}: {g.price}" for g in cart.goods])
# import sys
#
# class ListObject:
#     def __init__(self, data):
#         self.next_obj = None
#         self.data = data
#
#     def link(self, obj):
#         self.next_obj = obj
#
# lst_in = 'a b c d'.split()
#
# head_obj = ListObject(lst_in[0])
# obj = head_obj
# for i in range(1, len(lst_in)):
#     obj_new = ListObject(lst_in[i])
#     obj.link(obj_new)
#     obj = obj_new

# задание 15-11
# import random
#
# class Cell:
#     def __init__(self, mine=False, around_mines=0, fl_open=False):
#         self.around_mines = around_mines
#         self.mine = mine
#         self.fl_open = fl_open
#
#
# class GamePole:
#     def __init__(self, N, M):
#         self.M = M
#         self.N = N
#         self.pole = [[Cell()] * N for _ in range(N)]
#
#     def init(self):
#         self.pole = [[Cell()] * self.N for _ in range(self.N)]
#         for i in range(self.M):
#             random_list = []
#             random_i = random.randint(0, self.N - 1)
#             random_j = random.randint(0, self.N - 1)
#             # print(random_i)
#             # print(random_j)
#             self.pole[random_i][random_j] = Cell(True, 5, False)
#
#     def show(self):
#         for row in self.pole:
#             for cell in row:
#                 if cell.mine:
#                     print('*', end=' ')
#                 else:
#                     print(cell.around_mines, end=' ')
#             print()
#
#
# pole_game = GamePole(11, 12)
# pole_game.init()
# pole_game.show()


# Задание 1.6 подвиги------------
# class AbstractClass:
#     def __new__(cls, *args, **kwargs):
#         return 'Ошибка: нельзя создавать объекты абстрактного класса'
#
#
# #Задание 1.6.7
#
# class SingletonFive:
#     __instance = None
#     count = 0
#
#     def __new__(cls, *args, **kwargs):
#         if cls.count < 5:
#             cls.__instance = super().__new__(cls)
#             cls.count += 1
#         return cls.__instance
#
#     def __init__(self, name):
#         self.name = name
#
# objs = [SingletonFive(str(n)) for n in range(10)]
#
#
# #Задание 1.6.9
# TYPE_OS = 1 # 1 - Windows; 2 - Linux
#
# class DialogWindows:
#     name_class = "DialogWindows"
#
#     def __init__(self, name):
#         self.name = name
#
#
# class DialogLinux:
#     name_class = "DialogLinux"
#
#     def __init__(self, name):
#         self.name = name
#
#
# class Dialog:
#     def __new__(cls, *args, **kwargs):
#         name = args[0]
#         if TYPE_OS == 1:
#             return DialogWindows(name)
#         else:
#             return DialogLinux(name)
#
#
# zhopa = Dialog('пидр')
#
#
# #Задание 1.6.10
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def clone(self):
#         return Point(self.x, self.y)
#
#
# pt = Point(1, 5)
# pt_clone = pt.clone()
#
# #Задание 1.6.11
# class Factory:
#     @staticmethod
#     def build_sequence():
#         return []
#
#     @staticmethod
#     def build_number(string):
#         return float(string)
#
#
# class Loader:
#     def parse_format(self, string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq
#
#
# ld = Loader()
# res = ld.parse_format("4, 5, -6.5", Factory())
#
#
#  #Задание 1.7
# # Здесь объявляется класс Factory
# class Factory:
#     @classmethod
#     def build_sequence(cls):
#         return []
#
#     @classmethod
#     def build_number(cls, string):
#         return int(string)
#
#
# class Loader:
#     @staticmethod
#     def parse_format(string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq
#
#
# res = Loader.parse_format("1, 2, 3, -5, 10", Factory)
# print(res)
#
# #Задание 1.7.2
# from string import ascii_lowercase, digits
#
#
# class TextInput:
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
#     def __init__(self, name, size=10):
#         if self.check_name(name):
#             self.name = name
#             self.size = size
#
#     def get_html(self):
#         return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"
#
#     @classmethod
#     def check_name(cls, name):
#         if not 3 <= len(name) <= 50: raise ValueError('некорректное имя поля')
#         for i in name:
#             if i not in cls.CHARS_CORRECT: raise ValueError('некорректное имя поля')
#         return True
#
#
# class PasswordInput:
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
#     def __init__(self, name, size=10):
#         if self.check_name(name):
#             self.name = name
#             self.size = size
#
#     def get_html(self):
#         return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"
#
#     @classmethod
#     def check_name(cls, name):
#         if not 3 <= len(name) <= 50: raise ValueError('некорректное имя поля')
#         for i in name:
#             if i not in cls.CHARS_CORRECT: raise ValueError('некорректное имя поля')
#         return True
#
#
# class FormLogin:
#     def __init__(self, lgn, psw):
#         self.login = lgn
#         self.password = psw
#
#     def render_template(self):
#         return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
#
#
# # эти строчки не менять
# login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
# html = login.render_template()
#
# #Задание 1.7.9
# from string import ascii_lowercase, digits
#
# class CardCheck:
#     CHARS_FOR_NAME = ascii_lowercase.upper() + digits + ' '
#
#     @staticmethod
#     def check_card_number(number):
#         list_true = []
#         for i in number.split('-'):
#             for j in i:
#                 if j in digits:
#                     list_true.append(True)
#                 else:
#                     list_true.append(False)
#         return all(list_true)
#
#
#
#     @classmethod
#     def check_name(cls, name):
#         list_true = []
#         if len(name.split(' ')) == 2:
#             for i in name:
#                 if i in cls.CHARS_FOR_NAME:
#                     list_true.append(True)
#                 else:
#                     list_true.append(False)
#             return all(list_true)
#         else:
#             return False
#
#
# is_number = CardCheck.check_card_number("1234-5678-9012-0000")
# is_name = CardCheck.check_name("SERGEI BALAKIREV")
# print(is_name)
# print(is_number)

# Задание 1.7.9
# class Video:
#     def create(self, name):
#         self.name = name
#
#     def play(self):
#         print(f"воспроизведение видео {self.name}")
#

# class YouTube:
#     videos = []
#     @classmethod
#     def add_video(cls, video):
#         cls.videos.append(video)
#
#     @classmethod
#     def play(cls, video_indx):
#         cls.videos[video_indx].play()
#
#
#
# v1 = Video()
# v1.create('Python')
# v2 = Video()
# v2.create('Python ООП')
# a = YouTube()
# a.add_video(v1)
# a.play(0)
# a1 = YouTube()
# a1.add_video(v2)
# a1.play(1)
#
# #Задание 1.7.10
# class AppStore:
#     LIST_APLICATIONS = []
#
#     @classmethod
#     def add_application(cls, app):
#         cls.LIST_APLICATIONS.append(app)
#
#     @classmethod
#     def remove_application(cls, app):
#         cls.LIST_APLICATIONS.remove(app)
#
#     @classmethod
#     def block_application(cls, app):
#         for i in cls.LIST_APLICATIONS:
#             if i == app:
#                 i.blocked = True
#
#     @classmethod
#     def total_apps(cls):
#         return len(cls.LIST_APLICATIONS)
#
#
# class Application:
#     def __init__(self, name, blocked=False):
#         self.name = name
#         self.blocked = blocked
# class Viber:
#     list_msg = []
#
#     @classmethod
#     def add_message(cls, msg):
#         cls.list_msg.append(msg)
#
#     @classmethod
#     def remove_message(cls, msg):
#         cls.list_msg.remove(msg)
#
#     @classmethod
#     def set_like(cls, msg):
#         msg.fl_like = not msg.fl_like
#
#     @classmethod
#     def show_last_message(cls, number):
#         print(cls.list_msg[-number:])
#
#     @classmethod
#     def total_messages(cls):
#         return len(cls.list_msg)
#
#
# class Message:
#     def __init__(self, text, fl_like=False):
#         self.text = text
#         self.fl_like = fl_like
#
#
# msg = Message("Всем привет!")
# Viber.add_message(msg)
# Viber.set_like(msg)
# Viber.remove_message(msg)


# class Server:
#     """для описания работы серверов в сети
#     Соответственно в объектах класса Server должны быть локальные свойства:
#     buffer - список принятых пакетов (изначально пустой);
#     ip - IP-адрес текущего сервера.
#     """
#     ip_list = []
#
#     def __init__(self, ip=None):
#         self.buffer = []
#         self.ip = ip
#         self.ip_list.append(self)
#         self.ip = self.ip_list.index(self)
#
#     @staticmethod
#     def send_data(data):
#         """для отправки информационного пакета data (объекта класса Data)
#         с указанным IP-адресом получателя (пакет отправляется роутеру и
#         сохраняется в его буфере - локальном свойстве buffer);
#         """
#         router.buffer.append(data)
#
#     def get_data(self):
#         """возвращает список принятых пакетов (если ничего принято не было,
#         то возвращается пустой список) и очищает входной буфер;
#         """
#         temp_buffer = self.buffer.copy()
#         self.buffer.clear()
#         return temp_buffer
#
#     def get_ip(self):
#         """возвращает свой IP-адрес.
#         """
#         return self.ip
#
#
# class Router:
#     """для описания работы роутеров в сети (в данной задаче полагается один роутер).
#     И одно обязательное локальное свойство (могут быть и другие свойства):
#     buffer - список для хранения принятых от серверов пакетов (объектов класса Data).
#     """
#
#     def __init__(self):
#         self.server_list = []
#         self.buffer = []
#
#     def link(self, server):
#         """для присоединения сервера server (объекта класса Server) к роутеру
#         """
#         self.server_list.append(server)
#
#
#     def unlink(self, server):
#         """для отсоединения сервера server (объекта класса Server) от роутера
#         """
#         self.server_list.remove(server)
#
#     def send_data(self):
#         """для отправки всех пакетов (объектов класса Data) из буфера роутера
#         соответствующим серверам (после отправки буфер должен очищаться)
#         """
#         for i in self.buffer:
#             Server.ip_list[i.ip].buffer.append(i)
#         self.buffer.clear()
#
#
# class Data:
#     """для описания пакета информации
#     Наконец, объекты класса Data должны содержать, два следующих локальных свойства:
#     data - передаваемые данные (строка);
#     ip - IP-адрес назначения.
#     """
#
#     def __init__(self, data, ip):
#         self.data = data
#         self.ip = ip
#
#
#
# router = Router()
# sv_from = Server()
# router.link(sv_from)
# router.link(Server())
# router.link(Server())
# sv_to = Server()
# router.link(sv_to)
# sv_from.send_data(Data("Hello", sv_to.get_ip()))
# router.send_data()
# sv_to.send_data(Data("Hi", sv_from.get_ip()))
# router.send_data()
# msg_lst_from = sv_from.get_data()
# msg_lst_to = sv_to.get_data()
# Задание 1.8
#
# class Clock:
#     def __init__(self, time=0):
#         self.__time = time
#
#     def set_time(self, tm):
#         if self.__check_time(tm):
#             self.__time = tm
#
#     def get_time(self):
#         return self.__time
#
#     @classmethod
#     def __check_time(cls, tm):
#         return type(tm) is int and 100000 > tm >= 0
#
#
# clock = Clock(4530)


# Задание 2.1.4
# class Money:
#     def __init__(self, money):
#         self.__money = money
#
#     def set_money(self, money):
#         if self.__check_money(money):
#             self.__money = money
#
#     def get_money(self):
#         return self.__money
#
#     def add_money(self, mn):
#         self.__money = self.__money + mn.__money
#
#     @classmethod
#     def __check_money(cls, money):
#         return type(money) is int and money >= 0
# class Book:
#     def __init__(self, author, title, price):
#         self.__author = author
#         self.__title = title
#         self.__price = price
#
#     def set_title(self, title):
#         self.__title = title
#
#     def set_author(self, author):
#         self.__author = author
#
#     def set_price(self, price):
#         self.__price = price
#
#     def get_title(self):
#         return self.__title
#
#     def get_author(self):
#         return self.__author
#
#     def get_price(self):
#         return self.__price
#
#
# #задание 2.1.7
# class Line:
#     def __init__(self, x1, y1, x2, y2):
#         self.__x1 = x1
#         self.__y1 = y1
#         self.__x2 = x2
#         self.__y2 = y2
#
#     def set_coords(self, x1, y1, x2, y2):
#         self.__x1 = x1
#         self.__y1 = y1
#         self.__x2 = x2
#         self.__y2 = y2
#
#     def get_coords(self):
#         return (self.__x1, self.__y1, self.__x2, self.__y2)
#
#     def draw(self):
#         print([self.__x1, self.__y1, self.__x2, self.__y2])
#
# #Задание 2.1.8
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def get_coords(self):
#         return self.__x, self.__y
#
# class Rectangle:
#     def __init__(self, *args):
#         self.__sp = Point(args[0], args[1])
#         self.__ep = Point(args[2], args[3])
#
#     def set_coords(self, sp, ep):
#         self.__sp = sp
#         self.__ep = ep
#
#     def get_coords(self):
#         return self.__sp, self.__ep
#
#     def draw(self):
#         print(f"Прямоугольник с координатами: ({self.__sp.get_coords()}) ({self.__ep.get_coords()})")
#
#
# rect = Rectangle(0, 0, 20, 34)
#
# #Задание 2.1.9
# #Задание 2.1.9
# class LinkedList:
#     """объявите класс LinkedList, который будет представлять связный список в целом
#     и иметь набор следующих методов:
#     И локальные публичные атрибуты:
#     head - ссылка на первый объект связного списка (если список пустой, то head = None);
#     tail - ссылка на последний объект связного списка (если список пустой, то tail = None).
#     """
#
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def add_obj(self, obj):
#         """добавление нового объекта obj класса ObjList в конец связного списка;
#         """
#         if self.tail:
#             self.tail.set_next(obj)
#         obj.set_prev(self.tail)
#         self.tail = obj
#         if not self.head:
#             self.head = obj
#
#     def remove_obj(self):
#         """удаление последнего объекта из связного списка;
#         """
#         if self.tail is None:
#             return
#         prev = self.tail.get_prev()
#         if prev :
#             prev.set_next(None)
#         self.tail = prev
#         if self.tail is None:
#             self.head = None
#
#     def get_data(self):
#         """получение списка из строк локального свойства __data всех объектов связного списка.
#         """
#         s = []
#         h = self.head
#         while h:
#             s.append(h.get_data())
#             h = h.get_next()
#         return s
#
#
# class ObjList:
#     """Объекты класса ObjList должны иметь следующий набор приватных локальных свойств:
#     __next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
#     __prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
#     __data - строка с данными.
#     Также в классе ObjList должны быть реализованы следующие сеттеры и геттеры:
#     """
#     def __init__(self, data):
#         self.__next = None
#         self.__prev = None
#         self.__data = data
#
#     def set_next(self, obj):
#         """изменение приватного свойства __next на значение obj;
#         """
#         self.__next = obj
#
#     def set_prev(self, obj):
#         """изменение приватного свойства __prev на значение obj;
#         """
#         self.__prev = obj
#
#     def get_next(self):
#         """получение значения приватного свойства __next;
#         """
#         return self.__next
#
#     def get_prev(self):
#         """получение значения приватного свойства __prev;
#         """
#         return self.__prev
#
#     def set_data(self, data):
#         """изменение приватного свойства __data на значение data;
#         """
#         self.__data = data
#
#     def get_data(self):
#         """получение значения приватного свойства __data.
#         """
#         return self.__data
#
#
# ob = ObjList("данные 11")
# lst = LinkedList()
# lst.add_obj(ObjList("данные 1"))
# lst.add_obj(ObjList("данные 2"))
# lst.add_obj(ObjList("данные 3"))
# res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']


# Задание 2.1.10
# import string
# import random
#
#
# class EmailValidator:
#     EMAIL_CHARS = string.ascii_letters + string.digits + '_.@'
#     EMAIL_RANDOM_CHARS = string.ascii_letters + string.digits + '_'
#
#     def __new__(cls, *args, **kwargs):
#         return None
#
#     @classmethod
#     def check_email(cls, email):
#         if not cls.__is_email_str(email):
#             return False
#
#         if not set(email) < set(cls.EMAIL_CHARS):
#             return False
#
#         s = email.split('@')
#         if len(s) != 2:
#             return False
#
#         if len(s[0]) > 100 or len(s[1]) > 50:
#             return False
#
#         if '.' not in s[1]:
#             return False
#
#         if email.count('..') > 0:
#             return False
#
#     @classmethod
#     def get_random_email(cls):
#         n = random.randint(4, 20)
#         length = len(cls.EMAIL_RANDOM_CHARS) - 1
#         return ''.join(cls.EMAIL_RANDOM_CHARS[random.randint(0, length)] for i in range(n)) + '@gmail.com'
#
#     @staticmethod
#     def __is_email_str(email):
#         if not email is str:
#             return False
#
#
# res = EmailValidator.check_email("sc_lib@list.ru")  # True
# res = EmailValidator.check_email("sc_lib@list_ru")  # False
#
# #
# # assert EmailValidator.check_email(f"{'a' * 100}@{'b' * 45}.aaaa") == True
# # assert EmailValidator.check_email("i.like.this.course@my.stepik.domen.org") == True
# # assert EmailValidator.check_email('name.surname@mail.com') == True
# # assert EmailValidator.check_email(1342) == False
# # assert EmailValidator.check_email('a+a@m.c') == False
# # assert EmailValidator.check_email('aabda..kkk@m.c') == False
# # assert EmailValidator.check_email('aaaa@bbb..cc') == False
# # assert EmailValidator.check_email(f"{'a' * 100}@{'b' * 45}.aaaaa") == False
# # assert EmailValidator.check_email(f"{'a' * 101}@{'b' * 45}.aaaa") == False
# # assert EmailValidator.check_email(f"{'a'}@{'b' * 45}aaaa") == False
# # assert EmailValidator.check_email('name.surnamemail.com') == False
# # assert EmailValidator.check_email('name@mail') == False
# Задание 2.2.4
# class Car:
#     def __init__(self):
#         self.__model = None
#
#     @property
#     def model(self):
#         return self.__model
#
#     @model.setter
#     def model(self, value):
#         if type(value) == str and 2 < len(value) < 100:
#             self.__model = value
# zadaniye 2.2.5


# class WindowDlg:
#     def __init__(self, title, width, height):
#         self.__title = title
#         self.__width = width
#         self.__height = height
#
#     def show(self):
#         return f"{self.__title}:{self.__width}, {self.__height}"
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, value):
#         if self.__check_value(value):
#             self.__width = value
#             self.show()
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, value):
#         if self.__check_value(value):
#             self.__height = value
#             self.show()
#
#     @staticmethod
#     def __check_value(value):
#         return 0 <= value <= 10000

# Zadaniye 2.2.6
# class StackObj:
#     def __init__(self, data):
#         self.__data = data
#         self.__next = None
#
#     @property
#     def next(self):
#         return self.__next
#
#     @next.setter
#     def next(self, obj):
#         if self.__check_obj(obj):
#             self.__next = obj
#
#     @staticmethod
#     def __check_obj(obj):
#         return type(obj) == StackObj or obj is None
#
#     @property
#     def data(self):
#         return self.__data
#
#     @data.setter
#     def data(self, value):
#         self.__data = value
#
# class Stack:
#     def __init__(self):
#         self.top = None
#         self.last = None
#
#     def push(self, obj):
#         if not self.top:
#             self.top = obj
#         if self.last:
#             self.last.next = obj
#         self.last = obj
#
#     def pop(self):
#         if self.last is None:
#             return
#         s = []
#         h = self.top
#         while h:
#             s.append(h)
#             h = h.next
#         last_obj = s.pop()
#         if len(s) > 0:
#             s[-1].next = None
#         if len(s) == 0:
#             self.top = None
#
#     def get_data(self):
#         s = []
#         h = self.top
#         while h:
#             s.append(h.data)
#             h = h.next
#         return s
#
#
# st = Stack()
# st.push(StackObj("obj1"))
# print(st.get_data())
# st.push(StackObj("obj2"))
# print(st.get_data())
# st.push(StackObj("obj3"))
# print(st.get_data())
# st.pop()
# st.pop()
# print(st.get_data())
# res = st.get_data()    # ['obj1', 'obj2']


# zadaniye 2.2.7
# class RadiusVector2D:
#     MIN_COORD = -100
#     MAX_COORD = 1024
#
#     def __init__(self, x=0, y=0):
#         #self.__x = self.__y = 0
#         if self.__check_value(x) and self.__check_value(y):
#             self.__x = x
#             self.__y = y
#         self.__x = self.__y = 0
#
#     @classmethod
#     def __check_value(cls, value):
#         return cls.MIN_COORD <= value <= cls.MAX_COORD and type(value) in (int, float)
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         if self.__check_value(x):
#             self.__x = x
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, y):
#         if self.__check_value(y):
#             self.__y = y
#
#     @staticmethod
#     def norm2(vector):
#         return vector.x * vector.x + vector.y * vector.y


# zadaniye 2.2.8
# class TreeObj:
#     def __init__(self, indx, value=None):
#         self.index = indx
#         self.value = value
#         self.__left = None
#         self.__right = None
#
#     @property
#     def left(self):
#         return self.__left
#
#     @left.setter
#     def left(self, value):
#         self.__left = value
#
#     @property
#     def right(self):
#         return self.__right
#
#     @right.setter
#     def right(self, value):
#         self.__right = value
#
#
# class DecisionTree:
#
#     @classmethod
#     def predict(cls, root, x):
#         obj = root
#         while obj:
#             obj_next = cls.get_next(obj, x)
#             if obj_next is None:
#                 break
#             obj = obj_next
#         return obj.value
#
#     @classmethod
#     def get_next(cls, obj, x):
#         if x[obj.index] == 1:
#             return obj.left
#         return obj.right
#
#     @classmethod
#     def add_obj(cls, obj, node=None, left=True):
#         if node:
#             if left:
#                 node.left = obj
#             else:
#                 node.right = obj
#         return obj
#
#
# root = DecisionTree.add_obj(TreeObj(0))
# v_11 = DecisionTree.add_obj(TreeObj(1), root)
# v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
# DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
# DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
# DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
# DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)
#
# x = [1, 1, 0]
# res = DecisionTree.predict(root, x) # будет программистом


# zadaniye 2.2.9
# import math
#
# class LineTo:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# class PathLines:
#     list_obj = []
#
#     def __init__(self, *args):
#         self.list_obj = list(args)
#         self.list_obj.insert(0, LineTo(0, 0))
#
#
#     def get_path(self):
#         return self.list_obj
#
#     def get_length(self):
#         all_dist = 0
#         for i in range(1, len(self.list_obj)):
#             all_dist += math.sqrt((self.list_obj[i].x - self.list_obj[i-1].x) ** 2 + (self.list_obj[i].y - self.list_obj[i-1].y) ** 2)
#         return all_dist
#
#
#     def add_line(self, line):
#         self.list_obj.append(line)
#
#
# p = PathLines(LineTo(10, 20), LineTo(10, 30))
# p.add_line(LineTo(20, -10))
# dist = p.get_length()
# print(dist)


# zadaniye 2.2.10
# class PhoneBook:
#     list_book = []
#
#     def add_phone(self, phone):
#         self.list_book.append(phone)
#
#     def remove_phone(self, indx):
#         self.list_book.pop(indx)
#
#     def get_phone_list(self):
#         return self.list_book
#
#
# class PhoneNumber:
#     def __init__(self, number, fio):
#         self.number = number
#         self.fio = fio


# zadaniye 3.1.3
# class Book:
#     d = {'title': str, 'author': str, 'pages': int, 'year': int}
#
#     def __init__(self, title='', author='', pages=0, year=0):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.year = year
#
#     def __setattr__(self, key, value):
#         if key in self.d and self.d[key] == type(value):
#             super().__setattr__(key, value)
#         else:
#             raise TypeError('Неверный тип присваиваемых данных')
#
# book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)


# zadaniye 3.1.4
# class Shop:
#     def __init__(self, name):
#         self.name = name
#         self.goods = []
#
#     def add_product(self, product):
#         self.goods.append(product)
#
#     def remove_product(self, product):
#         self.goods.remove(product)
#
#
# class Product:
#     _id_instance = 1
#     type_product = {'name': (str,), 'weight': (int, float), 'price': (int, float), 'id': (int,)}
#     def __init__(self, name, weight, price):
#         self.id = Product._id_instance
#         Product._id_instance += 1
#         self.name = name
#         self.weight = weight
#         if self.__check_value(price) and self.__check_value(weight):
#             self.weight = weight
#             self.price = price
#         else:
#             raise TypeError("Неверный тип присваиваемых данных.")
#
#
#     @classmethod
#     def __check_value(cls, item):
#         return item > 0
#
#     def __delattr__(self, item):
#         if item == 'id':
#             raise AttributeError("Атрибут id удалять запрещено.")
#         else:
#             super().__delattr__(self, item)
#
#     def __setattr__(self, key, value):
#         if key in self.type_product and type(value) in self.type_product[key]:
#             super().__setattr__(key, value)
#         else:
#             raise TypeError('Неверный тип присваиваемых данных.')
#
#
#
#
# shop = Shop("Балакирев и К")
# book = Product("Python ООП", 100, 1024)
# shop.add_product(book)
# shop.add_product(Product("Python", 150, 512))
# for p in shop.goods:
#     print(f"{p.name}, {p.weight}, {p.price}")


# zadaniye 3.1.5
# class LessonItem:
#     type_key = {'title': str, 'practices': int, 'duration': int}
#
#     @classmethod
#     def __check_value(cls, item):
#         return item > 0
#
#     def __init__(self, title, practices, duration):
#         self.title = title
#         if self.__check_value(practices) and self.__check_value(duration):
#             self.practices = practices
#             self.duration = duration
#         else:
#             raise TypeError("Неверный тип присваиваемых данных.")
#
#     def __setattr__(self, key, value):
#         if key in self.type_key and self.type_key[key] == type(value):
#             super().__setattr__(key, value)
#         else:
#             raise TypeError('Неверный тип присваиваемых данных.')
#
#     def __getattr__(self, item):
#         return False
#
#
#     def __delattr__(self, item):
#         if item in ('title', 'practices', 'duration'):
#             raise AttributeError("Атрибут id удалять запрещено.")
#         else:
#             super().__delattr__(item)
#
#
# class Module:
#     def __init__(self, name):
#         self.name = name
#         self.lessons = []
#
#     def add_lesson(self, lesson):
#         self.lessons.append(lesson)
#
#     def remove_lesson(self, indx):
#         self.lessons.pop(indx)
#
#
# class Course:
#     def __init__(self, name):
#         self.name = name
#         self.modules = []
#
#     def add_module(self, module):
#         self.modules.append(module)
#
#     def remove_module(self, indx):
#         self.modules.pop(indx)
#
# course = Course("Python ООП")
# module_1 = Module("Часть первая")
# module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
# module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
# module_1.add_lesson(LessonItem("Урок 3", 5, 800))
# course.add_module(module_1)
# module_2 = Module("Часть вторая")
# module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
# module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
# course.add_module(module_2)


# zadaniye 3.1.7
# class Museum:
#     def __init__(self, name):
#         self.name = name
#         self.exhibits = []
#
#     def add_exhibit(self, obj):
#         self.exhibits.append(obj)
#
#     def remove_exhibit(self, obj):
#         self.exhibits.remove(obj)
#
#     def get_info_exhibit(self, indx):
#         return f'Описание экспоната {self.exhibits[indx].name}: {self.exhibits[indx].descr}'
#
# class Picture:
#     def __init__(self, name, author, descr):
#         self.name = name
#         self.author = author
#         self.descr = descr
# class Mummies:
#     def __init__(self, name, location, descr):
#         self.name = name
#         self.location = location
#         self.descr = descr
# class Papyri:
#     def __init__(self, name, date, descr):
#         self.name = name
#         self.date = date
#         self.descr = descr
#
# mus = Museum("Эрмитаж")
# mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор", "Вдохновляющая, устрашающая, волнующая картина"))
# mus.add_exhibit(Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации"))
# p = Papyri("Ученья для, не злата ради", "Древняя Россия", "Самое древнее найденное рукописное свидетельство о языках программирования")
# mus.add_exhibit(p)
# for x in mus.exhibits:
#     print(x.descr)
#
# print(mus.get_info_exhibit(1))


# zadanie 3.1.8
# class SmartPhone:
#     def __init__(self, model):
#         self.model = model
#         self.apps = []
#
#     def add_app(self, app):
#         if app.name not in list(map(lambda x: x.name, self.apps)):
#             self.apps.append(app)
#
#     def remove_app(self, app):
#         self.apps.remove(app)
#
# class AppVK:
#     def __init__(self):
#         self.name = "ВКонтакте"
#
#
# class AppYouTube:
#     def __init__(self, memory_max):
#         self.name = "YouTube"
#         self.memory_max = memory_max
#
# class AppPhone:
#     def __init__(self, phone_list):
#         self.name = "Phone"
#         self.phone_list = phone_list
#
# sm = SmartPhone("Honor 1.0")
# sm.add_app(AppVK())
# sm.add_app(AppVK())  # второй раз добавляться не должно
# sm.add_app(AppYouTube(2048))
# for a in sm.apps:
#     print(a.name)
#
# xyu = AppPhone({'ffff': 32424, 'wdadadaw': 14124})
#
# print(xyu.phone_list)


# zadaniye 3.1.9

# class Circle:
#     dict_type = {'x': (int, float), 'y': (int, float), 'radius': (int, float)}
#
#     def __init__(self, x, y, radius):
#         self.__x = self.__y = self.__radius = None
#         self.x = x
#         self.y = y
#         self.radius = radius
#
#     def __setattr__(self, key, value):
#         if key in self.dict_type and type(value) not in self.dict_type[key]:
#             raise TypeError("Неверный тип присваиваемых данных.")
#         if key == 'radius' and value <= 0:
#             return
#         else:
#             super().__setattr__(key, value)
#
#     def __getattr__(self, item):
#         return False
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         self.__x = x
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, y):
#         self.__y = y
#
#     @property
#     def radius(self):
#         return self.__radius
#
#     @radius.setter
#     def radius(self, radius):
#         self.__radius = radius
#
# circle = Circle(10.5, 7, 22)
# circle.radius = 10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
# x, y = circle.x, circle.y
# res = circle.name # False, т.к. атрибут name не существует


# zadaniye 3.1.9
# class Dimensions:
#     MIN_DIMENSION = 10
#     MAX_DIMENSION = 1000
#
#     def __init__(self, a, b, c):
#         self.__a = self.__b = self.__c = None
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __setattr__(self, key, value):
#         if key == 'MIN_DIMENSION' and key == 'MAX_DIMENSION':
#             raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
#         else:
#             super().__setattr__(key, value)
#
#     @classmethod
#     def __check_value(cls, value):
#         return type(value) in (int, float) and cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION
#
#     @property
#     def a(self):
#         return self.__a
#
#     @a.setter
#     def a(self, value):
#         if self.__check_value(value):
#             self.__a = value
#
#     @property
#     def b(self):
#         return self.__b
#
#     @b.setter
#     def b(self, value):
#         if self.__check_value(value):
#             self.__b = value
#
#     @property
#     def c(self):
#         return self.__c
#
#     @c.setter
#     def c(self, value):
#         if self.__check_value(value):
#             self.__c = value
#
#
# d = Dimensions(10.5, 20.1, 30)
# d.a = 8
# d.b = 15
# a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
# d.MAX_DIMENSION = 10  # исключение AttributeError


# zadaniye 3.1.11
# import time
#
#
# class GeyserClassic:
#     MAX_DATE_FILTER = 100
#     dict_filter = {'1': None, '2': None, '3': None}
#
#     def __setattr__(self, key, value):
#         if key == 'date' and key in self.__dict__.keys():
#             return
#         else:
#             super().__setattr__(key, value)
#
#     def add_filter(self, slot_num, filter):
#         if slot_num == 1 and self.dict_filter['1'] is None and type(filter) == Mechanical:
#             self.dict_filter['1'] = filter
#         elif slot_num == 2 and self.dict_filter['2'] is None and type(filter) == Aragon:
#             self.dict_filter['2'] = filter
#         elif slot_num == 3 and self.dict_filter['3'] is None and type(filter) == Calcium:
#             self.dict_filter['3'] = filter
#
#     def remove_filter(self, slot_num):
#         self.dict_filter[str(slot_num)] = None
#
#     def get_filters(self):
#         return (self.dict_filter['1'], self.dict_filter['2'], self.dict_filter['3'])
#
#     def water_on(self):
#         end = time.time()
#         for f in self.dict_filter.values():
#             if f is None:
#                 return False
#             start = f.date
#             if end - start > self.MAX_DATE_FILTER:
#                 return False
#         return True
#
#
# class Mechanical:
#     def __init__(self, date):
#         self.date = date
#
#     def __setattr__(self, key, value):
#         if key == 'date' and key in self.__dict__.keys():
#             return
#         else:
#             super().__setattr__(key, value)
#
#
# class Aragon:
#     def __init__(self, date):
#         self.date = date
#
#     def __setattr__(self, key, value):
#         if key == 'date' and key in self.__dict__.keys():
#             return
#         else:
#             super().__setattr__(key, value)
#
#
# class Calcium:
#     def __init__(self, date):
#         self.date = date
#
#     def __setattr__(self, key, value):
#         if key == 'date' and key in self.__dict__.keys():
#             return
#         else:
#             super().__setattr__(key, value)
#
# my_water = GeyserClassic()
# my_water.add_filter(1, Mechanical(22))
# my_water.add_filter(2, Aragon(11))
# w = my_water.water_on() # False
# print(w)
# my_water.add_filter(3, Calcium(26))
# w = my_water.water_on() # True
# print(w)
# f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
# my_water.add_filter(3, Calcium(20)) # повторное добавление в занятый слот невозможно
# my_water.add_filter(2, Calcium(95)) # добавление в "чужой" слот также невозможно
# w = my_water.water_on() # True
# print(w)
# class LinkedList:
#     """объявите класс LinkedList, который будет представлять связный список в целом
#     и иметь набор следующих методов:
#     И локальные публичные атрибуты:
#     head - ссылка на первый объект связного списка (если список пустой, то head = None);
#     tail - ссылка на последний объект связного списка (если список пустой, то tail = None).
#     """
#
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def __len__(self):
#         n = 0
#         h = self.head
#         while h:
#             n += 1
#             h = h.next
#         return n
#
#     def __call__(self, indx, *args, **kwargs):
#         obj = self.__get_obj_by_index(indx)
#         return obj.data if obj else None
#
#     def add_obj(self, obj):
#         """добавление нового объекта obj класса ObjList в конец связного списка;
#         """
#         obj.prev = self.tail
#         if self.tail:
#             self.tail.next = obj
#         self.tail = obj
#         if not self.head:
#             self.head = obj
#
#     def __get_obj_by_index(self, indx):
#         h = self.head
#         n = 0
#         while h and n < indx:
#             h = h.next
#             n += 1
#         return h
#
#     def remove_obj(self, indx):
#         """удаление последнего объекта из связного списка;
#         """
#         obj = self.__get_obj_by_index(indx)
#         if obj is None:
#             return
#
#         p, n = obj.prev, obj.next
#         if p:
#             p.next = n
#         if n:
#             n.prev = p
#         if self.head == obj:
#             self.head = n
#         if self.tail == obj:
#             self.tail = p
#
#     def get_data(self):
#         """получение списка из строк локального свойства __data всех объектов связного списка.
#         """
#         s = []
#         h = self.head
#         while h:
#             s.append(h.data)
#             h = h.next
#         return s
#
#
# class ObjList:
#     """Объекты класса ObjList должны иметь следующий набор приватных локальных свойств:
#     __next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
#     __prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
#     __data - строка с данными.
#     Также в классе ObjList должны быть реализованы следующие сеттеры и геттеры:
#     """
#
#     def __init__(self, data):
#         self.__next = None
#         self.__prev = None
#         self.__data = data
#
#     @property
#     def next(self):
#         """получение значения приватного свойства __next;
#         """
#         return self.__next
#
#     @next.setter
#     def next(self, obj):
#         """изменение приватного свойства __next на значение obj;
#         """
#         self.__next = obj
#
#     @property
#     def prev(self):
#         """получение значения приватного свойства __prev;
#         """
#         return self.__prev
#
#     @prev.setter
#     def prev(self, obj):
#         """изменение приватного свойства __prev на значение obj;
#                 """
#         self.__prev = obj
#
#     @property
#     def data(self):
#         """получение значения приватного свойства __data.
#         """
#         return self.__data
#
#     @data.setter
#     def data(self, data):
#         self.__data = data
#
#
# linked_lst = LinkedList()
# linked_lst.add_obj(ObjList("Sergey"))
# linked_lst.add_obj(ObjList("Balakirev"))
# linked_lst.add_obj(ObjList("Python"))
# linked_lst.remove_obj(2)
# linked_lst.add_obj(ObjList("Python ООП"))
# n = len(linked_lst)  # n = 3
# s = linked_lst(1) # s = Balakirev
# print(n)
# print(s)


# zadaniye 3.3.14
# import math
#
#
# class Complex:
#     def __init__(self, real, img):
#         self.__real = real
#         self.__img = img
#
#     @property
#     def real(self):
#         return self.__real
#
#     @real.setter
#     def real(self, value):
#         if self.__check_value(value):
#             self.__real = value
#
#     @property
#     def img(self):
#         return self.__img
#
#     @img.setter
#     def img(self, value):
#         if self.__check_value(value):
#             self.__img = value
#
#     def __abs__(self):
#         return abs(math.sqrt(self.__real * self.__real + self.__img * self.__img))
#
#     @classmethod
#     def __check_value(cls, value):
#         if type(value) not in (int, float):
#             raise ValueError("Неверный тип данных.")
#         else:
#             return value
#
#
# cmp = Complex(7, 8)
# cmp.real = 3
# cmp.img = 4
# c_abs = cmp.__abs__
#
#
# print(c_abs)


# zadaniye 3.3.7
# import math
#
#
# class RadiusVector:
#     def __init__(self, *args):
#         if len(args) == 1:
#             self.__coords = [0] * args[0]
#         else:
#             self.__coords = args
#
#     def set_coords(self, *args):
#         if len(args) < len(self.__coords):
#             for i, j in enumerate(args):
#                 self.__coords[i] = j
#         else:
#             for i, j in enumerate(self.__coords):
#                 self.__coords[i] = args[i]
#
#     def get_coords(self):
#         return self.__coords
#
#     def __len__(self):
#         return len(self.__coords)
#
#     def __abs__(self):
#         out = 0
#         for i in self.__coords:
#             out += i * i
#         return math.sqrt(out)
#
#
# vector3D = RadiusVector(3)
# vector3D.set_coords(3, -5.6, 8)
# a, b, c = vector3D.get_coords()
# vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
# vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
# res_len = len(vector3D) # res_len = 3
# res_abs = abs(vector3D)
# print(res_len)
# print(res_abs)


# zadaniye 3.3.8
# class DeltaClock:
#     def __init__(self, clock1, clock2):
#         self._clock1 = clock1
#         self._clock2 = clock2
#
#     def __str__(self):
#         d = self.__len__()
#         h = d // 3600
#         m = d % 3600 // 60
#         s = d % 3600 % 60
#         return f"{h:02}: {m:02}: {s:02}"
#
#     def __len__(self):
#         diff = self._clock1.get_time() - self._clock2.get_time()
#         return diff if diff > 0 else 0
#
#
# class Clock:
#     def __init__(self, hours, minutes, seconds):
#         self._hours = hours
#         self._minutes = minutes
#         self._seconds = seconds
#
#     def get_time(self):
#         return self._hours * 3600 + self._minutes * 60 + self._seconds
#
#
# dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
# print(dt)  # 01: 30: 00
# len_dt = len(dt)  # 5400
# print(len_dt)
#
#
#
# zadaniye 3.3.9
# class Recipe:
#     def __init__(self, *args):
#         self.ing_list = list(args)
#
#     def add_ingredient(self, ing):
#         self.ing_list.append(ing)
#
#     def remove_ingredient(self, ing):
#         self.ing_list.remove(ing)
#
#     def get_ingredients(self):
#         return tuple(self.ing_list)
#
#     def __len__(self):
#         return len(self.ing_list)
#
#
# class Ingredient:
#     def __init__(self, name, volume, measure):
#         self.name = name
#         self.volume = volume
#         self.measure = measure
#
#     def __str__(self):
#         return f"{self.name}: {self.volume}, {self.measure}"
#
#
# recipe = Recipe()
# recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
# recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
# recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
# ings = recipe.get_ingredients()
# n = len(recipe) # n = 3
# print(n)
# print(recipe.get_ingredients())
# print(str(ings))
# ing = Ingredient("Соль", 1, "столовая ложка")
# s = str(ing) # Соль: 1, столовая ложка
# print(s)
# i1 = Ingredient("Соль", 1, "столовая ложка")
# i2 = Ingredient("Мука", 1, "кг")
# i3 = Ingredient("Мясо баранины", 10, "кг")
# i4 = Ingredient("Масло", 100, "гр")
# recipe = Recipe(i1, i2, i3)
# recipe.add_ingredient(i4)
# recipe.remove_ingredient(i3)
# assert len(recipe) == 3, "функция len вернула неверное значение"
# lst = recipe.get_ingredients()
# print(lst)
# for x in lst:
#     assert isinstance(x, Ingredient), "в списке рецептов должны быть только объекты класса Ingredient"
#     assert hasattr(x, 'name') and hasattr(x, 'volume') and hasattr(x, 'measure'), "объект класса Ingredient должен иметь атрибуты: name, volume, measure"
# assert str(i4) == "Масло: 100, гр", "метод __str__ вернул неверное значение"
# i4 = Ingredient("Масло", 120, "гр")
# recipe.add_ingredient(i4)
# assert len(recipe) == 4, "функция len вернула неверное значение"
#
#
#
#
#
# zadaniye 3.3.10

# class PolyLine:
#     def __init__(self, *args):
#         self.start_coord = args[0]
#         self.coords = list(args)
#
#     def add_coord(self, x, y):
#         self.coords.append((x, y))
#
#     def remove_coord(self, indx):
#         self.coords.pop(indx)
#
#     def get_coords(self):
#         return self.coords
#
# poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
# print(poly.get_coords())
#
#
#
# zadaniye 3.4.5

# class NewList:
#     def __init__(self, lst=None):
#         self._lst = lst[:] if lst and type(lst) == list else []
#
#     def get_list(self):
#         return self._lst
#
#     def __sub__(self, other):
#         if type(other) not in (list, NewList):
#             raise ArithmeticError('Code 001')
#         other_list = other if type(other) == list else other.get_list()
#         return NewList(self.__diff_list(self._lst, other_list))
#
#     def __rsub__(self, other):
#         if type(other) != list:
#             raise ArithmeticError('code 002')
#         return NewList(self.__diff_list(other, self._lst))
#
#     @staticmethod
#     def __diff_list(lst1, lst2):
#         if len(lst2) == 0:
#             return lst1
#         sub = lst2[:]
#         return [x for x in lst1 if not NewList.__is_elem(x, sub)]
#
#     @staticmethod
#     def __is_elem(x, sub):
#         res = any(map(lambda xx: type(x) == type(xx) and x == xx, sub))
#         if res:
#             sub.remove(x)
#         return res


# hello-git
# HELO VS code git


# mikheev_loh


# class ListMath:
#     def __init__(self, lst=None):
#         self.lst_math = lst if lst and type(lst) == list else []
#         self.lst_math = list(filter(lambda x: type(x) in (int, float), self.lst_math))
#
#     @staticmethod
#     def __verify_value(value):
#         if type(value) not in (int, float):
#             raise ArithmeticError('xyu')
#
#     def __add__(self, other):
#         self.__verify_value(other)
#         return ListMath([x + other for x in self.lst_math])
#
#     def __radd__(self, other):
#         return self + other
#
#     def __sub__(self, other):
#         self.__verify_value(other)
#         return ListMath([x - other for x in self.lst_math])
#
#     def __rsub__(self, other):
#         return ListMath([other - x for x in self.lst_math])
#
#     def __mul__(self, other):
#         self.__verify_value(other)
#         return ListMath([x * other for x in self.lst_math])
#
#     def __rmul__(self, other):
#         return self * other
#
#     def __truediv__(self, other):
#         self.__verify_value(other)
#         return ListMath([x / other for x in self.lst_math])
#
#     def __rtruediv__(self, other):
#         return ListMath([other / x for x in self.lst_math])
#
#     def __iadd__(self, other):
#         self.__verify_value(other)
#         self.lst_math = [x + other for x in self.lst_math]
#         return self
#
#     def __isub__(self, other):
#         self.__verify_value(other)
#         self.lst_math = [x - other for x in self.lst_math]
#         return self
#
#     def __imul__(self, other):
#         self.__verify_value(other)
#         self.lst_math = [x * other for x in self.lst_math]
#         return self
#
#     def __itruediv__(self, other):
#         self.__verify_value(other)
#         self.lst_math = [x / other for x in self.lst_math]
#         return self

#
# class StackObj:
#     def __init__(self, data):
#         self.__data = data
#         self.__next = None
#
#     @property
#     def data(self):
#         return self.__data
#
#     @property
#     def next(self):
#         return self.__next
#
#     @next.setter
#     def next(self, obj):
#         self.__next = obj
#
#
# class Stack:
#     def __init__(self):
#         self.top = None
#         self.__last = None
#
#     def push_back(self, obj):
#         if self.__last:
#             self.__last.next = obj
#         self.__last = obj
#
#         if self.top is None:
#             self.top = obj
#
#     def pop_back(self):
#         h = self.top
#         if h is None:
#             return
#         while h.next and h.next != self.__last:
#             h = h.next
#
#         if self.top == self.__last:
#             self.top = self.__last = None
#         else:
#             h.next = None
#             self.__last = h
#
#     def __add__(self, other):
#         self.push_back(other)
#         return self
#
#     def __iadd__(self, other):
#         return self.__add__(other)
#
#     def __mul__(self, other):
#         for x in other:
#             self.push_back(StackObj(x))
#         return self
#
#     def __imul__(self, other):
#         return self.__mul__(other)


# class Clock:
#     __DAY = 86400
#
#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError("Seconds to be int")
#         self.seconds = seconds % self.__DAY
#
#     def get_time(self):
#         s = self.seconds % 60
#         m = (self.seconds // 60) % 60
#         h = (self.seconds // 3600) % 24
#         return f"{self.__get_formated(h)}:{self.__get_formated(m)}:{self.__get_formated(s)}"
#
#     @classmethod
#     def __get_formated(cls, x):
#         return str(x).rjust(2, "0")
#
#     def __add__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise ArithmeticError("cod 002")
#
#         sc = other
#         if isinstance(other, Clock):
#             sc = other.seconds
#
#         return Clock(self.seconds + sc)
#
#     def __radd__(self, other):
#         return self + other
#
#     def __iadd__(self, other):
#         print('---iadd')
#         if not isinstance(other, (int, Clock)):
#             raise ArithmeticError('code 2')
#         sc = other
#         if isinstance(other, Clock):
#             sc = other.seconds
#
#         self.seconds += sc
#         return self
#
#
# c1 = Clock(1000)
# c1 = 100 + c1
# c1 += 100
# print(c1.get_time())




# #Zadanie 3.4.8
#
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
#
# class Lib:
#     def __init__(self):
#         self.book_list = []
#
#     def __add__(self, other):
#         if not isinstance(other, Book):
#             raise ArithmeticError('cod 001')
#
#         self.book_list.append(other)
#         return self
#
#     def __iadd__(self, other):
#         return self + other
#
#     def __sub__(self, other):
#         if isinstance(other, Book):
#             self.book_list.remove(other)
#             return self
#         if isinstance(other, int):
#             if len(self.book_list) >= other:
#                 self.book_list.pop(other)
#             else:
#                 raise IndexError("В списке нет такого индекса")
#             return self
#
#     def __isub__(self, other):
#         if isinstance(other, Book):
#             if other in self.book_list:
#                 self.book_list.remove(other)
#                 return self
#             else:
#                 print("Список пустой")
#         if isinstance(other, int):
#             if len(self.book_list) >= other:
#                 self.book_list.pop(other)
#             else:
#                 raise IndexError("В списке нет такого индекса")
#             return self
#
#     def __len__(self):
#         return len(self.book_list)
#
#
# book = Book("Clear member", "Mark Zalupsk", 2010)
# book2 = Book("Clear member2", "Mark Zalupsk2", 2015)
# book3 = Book("Clear member23", "Mark Zalupsk2", 2015)
# lib = Lib()
# lib += book
# lib += book2
# lib += book3
# print(lib.book_list)
#
# lib -= book
# print(lib.book_list)
# lib -= 1
# print(lib.book_list)
