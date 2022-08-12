# #zadaniye 3.4.9
# class Box3D:
#     def __init__(self, width, height, depth):
#         self.width = width
#         self.height = height
#         self.depth = depth
#
#     def __add__(self, other):
#         if not isinstance(other, Box3D):
#             raise ArithmeticError('Складывать только объекты одного класса')
#
#         sw = other.width
#         sh = other.height
#         sd = other.depth
#
#         return Box3D(self.width + sw, self.height + sh, self.depth + sd)
#
#     def __mul__(self, other):
#         if not isinstance(other, int):
#             raise ArithmeticError('Умножать можно только на целое число')
#
#         return Box3D(self.width * other, self.height * other, self.depth * other)
#
#     def __rmul__(self, other):
#         return self * other
#
#     def __sub__(self, other):
#         if not isinstance(other, Box3D):
#             raise ArithmeticError('Вычитать только объекты одного класса')
#
#         sw = other.width
#         sh = other.height
#         sd = other.depth
#
#         return Box3D(self.width - sw, self.height - sh, self.depth - sd)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, int):
#             raise ArithmeticError('Целочисленно делить можно только на целое число')
#
#         return Box3D(self.width // other, self.height // other, self.depth // other)
#
#     def __mod__(self, other):
#         if not isinstance(other, int):
#             raise ArithmeticError('Только на целое число делить')
#
#         return Box3D(self.width % other, self.height % other, self.depth % other)
#
#
#
#
# box1 = Box3D(1, 2, 3)
# box2 = Box3D(2, 4, 6)
#
# box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
# box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
# box = 3 * box2    # Box3D: width=6, height=12, depth=18
# box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
# box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
# box = box2 % 3    # Box3D: width=2, height=1, depth=0
# print(box.width, box.height, box.depth)


# zadaniye 3.4.10
# class MaxPooling:
#     def __init__(self, step=(2, 2), size=(2, 2)):
#         self.__step = step
#         self.__size = size
#
#     def __call__(self, matrix):
#         rows = len(matrix)
#         cols = len(matrix[0]) if rows > 0 else 0
#
#         if rows == 0:
#             return [[]]
#
#         if not all(map(lambda x: len(x) == cols, matrix)) or \
#                 not all(map(lambda row: all(map(lambda x: type(x) in (int, float), row)), matrix)):
#             raise ValueError('code 001')
#
#         h, w = self.__size[0], self.__size[1]
#         sh, sw = self.__step[0], self.__step[1]
#
#         rows_range = (rows - h) // sh + 1
#         cols_range = (cols - w) // sw + 1
#
#         res = [[0] * cols_range for _ in range(rows_range)]
#
#         for i in range(rows_range):
#             for j in range(cols_range):
#                 s = (x for r in matrix[i * sh: i * sh + h] for x in r[j * sw: j * sw + w])
#                 res[i][j] = max(s)
#
#         return res
#
#
# mp = MaxPooling(step=(2, 2), size=(2,2))
# res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]
# print(res)


# zadaniye 3.5.3
# class Track:
#     def __init__(self, start_x=0, start_y=0):
#         self.start_x = start_x
#         self.start_y = start_y
#         self.__list_Track = []
#
#     def add_track(self, tr):
#         self.__list_Track.append(tr)
#
#     def get_tracks(self):
#         return tuple(self.__list_Track)
#
#     def __eq__(self, other):
#         return len(self) == len(other)
#
#     def __lt__(self, other):
#         return len(self) < len(other)
#
#     def __len__(self):
#         len_1 = ((self.start_x - self.__list_Track[0].x) ** 2 + (self.start_y - self.__list_Track[0].y) ** 2) ** 0.5
#         return int(len_1 + sum(self.__get_lenght(i) for i in range(1, len(self.__list_Track))))
#
#     def __get_lenght(self, i):
#         return ((self.__list_Track[i-1].x - self.__list_Track[i].x) ** 2 + (self.__list_Track[i-1].y - self.__list_Track[i].y) ** 2) ** 0.5
#
#
#
# class TrackLine:
#     def __init__(self, to_x, to_y, max_speed):
#         self.to_x = to_x
#         self.to_y = to_y
#         self._max_speed = max_speed
#
#     @property
#     def x(self):
#         return self.to_x
#
#     @property
#     def y(self):
#         return self.to_y
#
#     @property
#     def max_speed(self):
#         return self._max_speed
#
#
#
# track1, track2 = Track(), Track(0, 1)
# track1.add_track(TrackLine(2, 4, 100))
# track1.add_track(TrackLine(5, -4, 100))
# track2.add_track(TrackLine(3, 2, 90))
# track2.add_track(TrackLine(10, 8, 90))
# print(len(track1), len(track2))
# res_eq = track1 == track2


# zadaniye 3.5.4
# class Dimensions:
#     MIN_DIMENSION = 10
#     MAX_DIMENSION = 10000
#
#     def __init__(self, a, b, c):
#         self.__a = a
#         self.__b = b
#         self.__c = c
#
#     @classmethod
#     def __check_value(cls, value):
#         return cls.MAX_DIMENSION >= value >= cls.MIN_DIMENSION
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
#     def __ge__(self, other):
#         return self.__a * self.__b * self.__c >= other.__a * other.__b * other.__c
#
#     def __gt__(self, other):
#         return self.__a * self.__b * self.__c >= other.__a * other.__b * other.__c
#
#
# class ShopItem:
#     def __init__(self, name, price, dim):
#         self.name = name
#         self.price = price
#         self.dim = dim
#
#
# trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
# umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
# fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
# chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
# lst_shop = [trainers, umbrella, fridge, chair]
# lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)


# zadaniye 3.6.4
# class Rect:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#
#     def __eq__(self, other):
#         return self.width == other.width and self.height == other.height
#
#     def __hash__(self):
#         return hash((self.width, self.height))
#
#
# r1 = Rect(10, 5, 100, 50)
# r2 = Rect(-10, 4, 100, 50)
#
# h1, h2 = hash(r1), hash(r2)   # h1 == h2
# print(h1, h2)


# zadaniye 3.6.5
# class ShopItem:
#     def __init__(self, name, weight, price):
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def __hash__(self):
#         return hash((self.name.lower(), self.weight, self.price))
#
#     def __eq__(self, other):
#         return self.name.lower() == other.name.lower() and self.weight == other.weight and self.price == other.price
#
#
# lst_in = ["Системный блок: 1500 75890.56", "Монитор Samsung: 2000 34000", "Клавиатура: 200.44 545", "Монитор Samsung: 2000 34000"]
# shop_items = {}
#
# list_total = []
# for i in lst_in:
#     obj = ShopItem(i.split(":")[0], i.split(":")[-1].strip().split(" ")[0], i.split(":")[-1].strip().split(" ")[1])
#     list_total.append(obj)
#     total = [i.split(":")[0] for i in lst_in]
#     shop_items[obj] = [obj, total.count(obj.name)]
#     obj = None
#
# print(shop_items)


# zadaniye 3.6.9
# import ast
#
#
# class Dimensions:
#     def __init__(self, a, b, c):
#         if self.__check_value(a):
#             self.a = a
#         if self.__check_value(b):
#             self.b = b
#         if self.__check_value(c):
#             self.c = c
#
#     def __hash__(self):
#         return hash((self.a, self.b, self.c))
#
#     def __eq__(self, other):
#         return self.a == other.a and self.b == other.b and self.c == other.c
#
#     def __gt__(self, other):
#         return hash((self.a, self.b, self.c)) > hash((other.a, other.b, other.c))
#
#     @classmethod
#     def __check_value(cls, value):
#         if value < 0:
#             raise ValueError("габаритные размеры должны быть положительными числами")
#
#
# lst_dims = []
# for i in input().split(";"):
#     coord = i.strip().split()
#     lst_dims.append(Dimensions(ast.literal_eval(coord[0]), ast.literal_eval(coord[1]), ast.literal_eval(coord[2])))
#
# lst_dims = sorted(lst_dims, key=lambda x: hash(x))


#zadaniye 3.7.3
# class Player:
#     def __init__(self, name, old, score):
#         self.name = name
#         self.old = old
#         self.score = score
#
#     def __bool__(self):
#         return self.score > 0
#
#
# players = []
# lst_xyu = [i.strip().split(";") for i in lst_in]
# for i in lst_xyu:
#     players.append(Player(i[0], int(i[1]), int(i[2])))
# players_filtered = list(filter(bool, players))


#zadaniye 3.8.2
# class Record:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)
#         self.__total_attrs = len(kwargs)
#         self.__attrs = tuple(self.__dict__.keys())
#
#     def __ckeck_index(self, index):
#         if type(index) != int or not (-self.__total_attrs <= index < self.__total_attrs):
#             raise IndexError('неверный индекс поля')
#
#
#     def __getitem__(self, item):
#         self.__ckeck_index(item)
#         return getattr(self, self.__attrs[item])
#
#     def __setitem__(self, key, value):
#         self.__ckeck_index(key)
#         setattr(self, self.__attrs[key], value)

# class Track:
#     def __init__(self, start_x, start_y):
#         self.start_x = start_x
#         self.start_y = start_y
#         self.points = []
#
#     def add_point(self, x, y, speed):
#         self.points.append([x, y, speed])
#
#     def __getitem__(self, item):
#         return (self.points[item][0], self.points[item][1]), self.points[item][-1]
#
#     def __setitem__(self, key, value):
#         self.points[key][-1] = value
#
#
#
#
#
# tr = Track(10, -5.4)
# tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
# tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
# tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2
#
# tr[2] = 60
# c, s = tr[2]
# print(c, s)
class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job

    def __getitem__(self, item):
        return self.__dict__[item]

pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
print(pers.__dict__)