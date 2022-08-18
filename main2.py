# # #zadaniye 3.4.9
# # class Box3D:
# #     def __init__(self, width, height, depth):
# #         self.width = width
# #         self.height = height
# #         self.depth = depth
# #
# #     def __add__(self, other):
# #         if not isinstance(other, Box3D):
# #             raise ArithmeticError('Складывать только объекты одного класса')
# #
# #         sw = other.width
# #         sh = other.height
# #         sd = other.depth
# #
# #         return Box3D(self.width + sw, self.height + sh, self.depth + sd)
# #
# #     def __mul__(self, other):
# #         if not isinstance(other, int):
# #             raise ArithmeticError('Умножать можно только на целое число')
# #
# #         return Box3D(self.width * other, self.height * other, self.depth * other)
# #
# #     def __rmul__(self, other):
# #         return self * other
# #
# #     def __sub__(self, other):
# #         if not isinstance(other, Box3D):
# #             raise ArithmeticError('Вычитать только объекты одного класса')
# #
# #         sw = other.width
# #         sh = other.height
# #         sd = other.depth
# #
# #         return Box3D(self.width - sw, self.height - sh, self.depth - sd)
# #
# #     def __floordiv__(self, other):
# #         if not isinstance(other, int):
# #             raise ArithmeticError('Целочисленно делить можно только на целое число')
# #
# #         return Box3D(self.width // other, self.height // other, self.depth // other)
# #
# #     def __mod__(self, other):
# #         if not isinstance(other, int):
# #             raise ArithmeticError('Только на целое число делить')
# #
# #         return Box3D(self.width % other, self.height % other, self.depth % other)
# #
# #
# #
# #
# # box1 = Box3D(1, 2, 3)
# # box2 = Box3D(2, 4, 6)
# #
# # box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
# # box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
# # box = 3 * box2    # Box3D: width=6, height=12, depth=18
# # box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
# # box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
# # box = box2 % 3    # Box3D: width=2, height=1, depth=0
# # print(box.width, box.height, box.depth)
#
#
# # zadaniye 3.4.10
# # class MaxPooling:
# #     def __init__(self, step=(2, 2), size=(2, 2)):
# #         self.__step = step
# #         self.__size = size
# #
# #     def __call__(self, matrix):
# #         rows = len(matrix)
# #         cols = len(matrix[0]) if rows > 0 else 0
# #
# #         if rows == 0:
# #             return [[]]
# #
# #         if not all(map(lambda x: len(x) == cols, matrix)) or \
# #                 not all(map(lambda row: all(map(lambda x: type(x) in (int, float), row)), matrix)):
# #             raise ValueError('code 001')
# #
# #         h, w = self.__size[0], self.__size[1]
# #         sh, sw = self.__step[0], self.__step[1]
# #
# #         rows_range = (rows - h) // sh + 1
# #         cols_range = (cols - w) // sw + 1
# #
# #         res = [[0] * cols_range for _ in range(rows_range)]
# #
# #         for i in range(rows_range):
# #             for j in range(cols_range):
# #                 s = (x for r in matrix[i * sh: i * sh + h] for x in r[j * sw: j * sw + w])
# #                 res[i][j] = max(s)
# #
# #         return res
# #
# #
# # mp = MaxPooling(step=(2, 2), size=(2,2))
# # res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]
# # print(res)
#
#
# # zadaniye 3.5.3
# # class Track:
# #     def __init__(self, start_x=0, start_y=0):
# #         self.start_x = start_x
# #         self.start_y = start_y
# #         self.__list_Track = []
# #
# #     def add_track(self, tr):
# #         self.__list_Track.append(tr)
# #
# #     def get_tracks(self):
# #         return tuple(self.__list_Track)
# #
# #     def __eq__(self, other):
# #         return len(self) == len(other)
# #
# #     def __lt__(self, other):
# #         return len(self) < len(other)
# #
# #     def __len__(self):
# #         len_1 = ((self.start_x - self.__list_Track[0].x) ** 2 + (self.start_y - self.__list_Track[0].y) ** 2) ** 0.5
# #         return int(len_1 + sum(self.__get_lenght(i) for i in range(1, len(self.__list_Track))))
# #
# #     def __get_lenght(self, i):
# #         return ((self.__list_Track[i-1].x - self.__list_Track[i].x) ** 2 + (self.__list_Track[i-1].y - self.__list_Track[i].y) ** 2) ** 0.5
# #
# #
# #
# # class TrackLine:
# #     def __init__(self, to_x, to_y, max_speed):
# #         self.to_x = to_x
# #         self.to_y = to_y
# #         self._max_speed = max_speed
# #
# #     @property
# #     def x(self):
# #         return self.to_x
# #
# #     @property
# #     def y(self):
# #         return self.to_y
# #
# #     @property
# #     def max_speed(self):
# #         return self._max_speed
# #
# #
# #
# # track1, track2 = Track(), Track(0, 1)
# # track1.add_track(TrackLine(2, 4, 100))
# # track1.add_track(TrackLine(5, -4, 100))
# # track2.add_track(TrackLine(3, 2, 90))
# # track2.add_track(TrackLine(10, 8, 90))
# # print(len(track1), len(track2))
# # res_eq = track1 == track2
#
#
# # zadaniye 3.5.4
# # class Dimensions:
# #     MIN_DIMENSION = 10
# #     MAX_DIMENSION = 10000
# #
# #     def __init__(self, a, b, c):
# #         self.__a = a
# #         self.__b = b
# #         self.__c = c
# #
# #     @classmethod
# #     def __check_value(cls, value):
# #         return cls.MAX_DIMENSION >= value >= cls.MIN_DIMENSION
# #
# #     @property
# #     def a(self):
# #         return self.__a
# #
# #     @a.setter
# #     def a(self, value):
# #         if self.__check_value(value):
# #             self.__a = value
# #
# #     @property
# #     def b(self):
# #         return self.__b
# #
# #     @b.setter
# #     def b(self, value):
# #         if self.__check_value(value):
# #             self.__b = value
# #
# #     @property
# #     def c(self):
# #         return self.__c
# #
# #     @c.setter
# #     def c(self, value):
# #         if self.__check_value(value):
# #             self.__c = value
# #
# #     def __ge__(self, other):
# #         return self.__a * self.__b * self.__c >= other.__a * other.__b * other.__c
# #
# #     def __gt__(self, other):
# #         return self.__a * self.__b * self.__c >= other.__a * other.__b * other.__c
# #
# #
# # class ShopItem:
# #     def __init__(self, name, price, dim):
# #         self.name = name
# #         self.price = price
# #         self.dim = dim
# #
# #
# # trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
# # umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
# # fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
# # chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
# # lst_shop = [trainers, umbrella, fridge, chair]
# # lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)
#
#
# # zadaniye 3.6.4
# # class Rect:
# #     def __init__(self, x, y, width, height):
# #         self.x = x
# #         self.y = y
# #         self.width = width
# #         self.height = height
# #
# #     def __eq__(self, other):
# #         return self.width == other.width and self.height == other.height
# #
# #     def __hash__(self):
# #         return hash((self.width, self.height))
# #
# #
# # r1 = Rect(10, 5, 100, 50)
# # r2 = Rect(-10, 4, 100, 50)
# #
# # h1, h2 = hash(r1), hash(r2)   # h1 == h2
# # print(h1, h2)
#
#
# # zadaniye 3.6.5
# # class ShopItem:
# #     def __init__(self, name, weight, price):
# #         self.name = name
# #         self.weight = weight
# #         self.price = price
# #
# #     def __hash__(self):
# #         return hash((self.name.lower(), self.weight, self.price))
# #
# #     def __eq__(self, other):
# #         return self.name.lower() == other.name.lower() and self.weight == other.weight and self.price == other.price
# #
# #
# # lst_in = ["Системный блок: 1500 75890.56", "Монитор Samsung: 2000 34000", "Клавиатура: 200.44 545", "Монитор Samsung: 2000 34000"]
# # shop_items = {}
# #
# # list_total = []
# # for i in lst_in:
# #     obj = ShopItem(i.split(":")[0], i.split(":")[-1].strip().split(" ")[0], i.split(":")[-1].strip().split(" ")[1])
# #     list_total.append(obj)
# #     total = [i.split(":")[0] for i in lst_in]
# #     shop_items[obj] = [obj, total.count(obj.name)]
# #     obj = None
# #
# # print(shop_items)
#
#
# # zadaniye 3.6.9
# # import ast
# #
# #
# # class Dimensions:
# #     def __init__(self, a, b, c):
# #         if self.__check_value(a):
# #             self.a = a
# #         if self.__check_value(b):
# #             self.b = b
# #         if self.__check_value(c):
# #             self.c = c
# #
# #     def __hash__(self):
# #         return hash((self.a, self.b, self.c))
# #
# #     def __eq__(self, other):
# #         return self.a == other.a and self.b == other.b and self.c == other.c
# #
# #     def __gt__(self, other):
# #         return hash((self.a, self.b, self.c)) > hash((other.a, other.b, other.c))
# #
# #     @classmethod
# #     def __check_value(cls, value):
# #         if value < 0:
# #             raise ValueError("габаритные размеры должны быть положительными числами")
# #
# #
# # lst_dims = []
# # for i in input().split(";"):
# #     coord = i.strip().split()
# #     lst_dims.append(Dimensions(ast.literal_eval(coord[0]), ast.literal_eval(coord[1]), ast.literal_eval(coord[2])))
# #
# # lst_dims = sorted(lst_dims, key=lambda x: hash(x))
#
#
# # zadaniye 3.7.3
# # class Player:
# #     def __init__(self, name, old, score):
# #         self.name = name
# #         self.old = old
# #         self.score = score
# #
# #     def __bool__(self):
# #         return self.score > 0
# #
# #
# # players = []
# # lst_xyu = [i.strip().split(";") for i in lst_in]
# # for i in lst_xyu:
# #     players.append(Player(i[0], int(i[1]), int(i[2])))
# # players_filtered = list(filter(bool, players))
#
#
# # zadaniye 3.8.2
# # class Record:
# #     def __init__(self, **kwargs):
# #         self.__dict__.update(kwargs)
# #         self.__total_attrs = len(kwargs)
# #         self.__attrs = tuple(self.__dict__.keys())
# #
# #     def __ckeck_index(self, index):
# #         if type(index) != int or not (-self.__total_attrs <= index < self.__total_attrs):
# #             raise IndexError('неверный индекс поля')
# #
# #
# #     def __getitem__(self, item):
# #         self.__ckeck_index(item)
# #         return getattr(self, self.__attrs[item])
# #
# #     def __setitem__(self, key, value):
# #         self.__ckeck_index(key)
# #         setattr(self, self.__attrs[key], value)
#
# # class Track:
# #     def __init__(self, start_x, start_y):
# #         self.start_x = start_x
# #         self.start_y = start_y
# #         self.points = []
# #
# #     def add_point(self, x, y, speed):
# #         self.points.append([x, y, speed])
# #
# #     def __getitem__(self, item):
# #         return (self.points[item][0], self.points[item][1]), self.points[item][-1]
# #
# #     def __setitem__(self, key, value):
# #         self.points[key][-1] = value
# #
# #
# #
# #
# #
# # tr = Track(10, -5.4)
# # tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
# # tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
# # tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2
# #
# # tr[2] = 60
# # c, s = tr[2]
# # print(c, s)
# # class Person:
# #     def __init__(self, fio, job, old, salary, year_job):
# #         self.fio = fio
# #         self.job = job
# #         self.old = old
# #         self.salary = salary
# #         self.year_job = year_job
# #         self._attrs = tuple(self.__dict__)
# #         self._len_attrs = len(self._attrs)
# #         self._iter_index = -1
# #
# #     @staticmethod
# #     def __check_index(index):
# #         if index < 0 or index > 4:
# #             raise IndexError('неверный индекс')
# #
# #     def __getitem__(self, item):
# #         self.__check_index(item)
# #         return self.__dict__[self._attrs[item]]
# #
# #     def __setitem__(self, key, value):
# #         self.__dict__[self._attrs[key]] = value
# #
# #     def __iter__(self):
# #         self._iter_index = -1
# #         return self
# #
# #     def __next__(self):
# #         if self._iter_index < self._len_attrs - 1:
# #             self._iter_index += 1
# #             return getattr(self, self._attrs[self._iter_index])
# #         raise StopIteration
# #
# #
# # pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
# # pers[0] = 'Балакирев С.М.'
# # for v in pers:
# #     print(v)
#
#
# # zadaniye 3.9.6
# # class TriangleListIterator:
# #     def __init__(self, lst):
# #         self._lst = lst
# #
# #     def __iter__(self):
# #         for i in range(len(self._lst)):
# #             for j in range(i+1):
# #                 yield self._lst[i][j]
#
#
# #
# # class FRange:
# #     def __init__(self, start=0.0, stop=0.0, step=1.0):
# #         self.start = start
# #         self.stop = stop
# #         self.step = step
# #         self.value = self.start - self.step
# #
# #     def __next__(self):
# #         if self.value + self.step < self.stop:
# #             self.value += self.step
# #             return self.value
# #         else:
# #             raise StopIteration
# #
# #
# # fr = FRange(0, 5, 1)
# # print(fr.__next__())
# # print(fr.__next__())
# # print(fr.__next__())
# # print(fr.__next__())
# # print(fr.__next__())
#
#
# # zadaniye 3.9.10
#
# # class IterColum:
# #     def __init__(self, lst, col_indx):
# #         self._lst = lst
# #         self._col_indx = col_indx
# #
# #     def __iter(self):
# #         for row in self._lst:
# #             yield row[self._col_indx]
#
#
# # zadaniye 3.9.13
#
# # class StackObj:
# #     def __init__(self, data):
# #         self.data = data
# #         self.next = None
# #
# #     def __repr__(self):
# #         return str(self.data)
# #
# #
# # class Stack:
# #     def __init__(self):
# #         self.top = None
# #         self.__last = None
# #
# #     def push_back(self, obj):
# #         if self.top is None:
# #             self.top = obj
# #         else:
# #             self.__last.next = obj
# #         self.__last = obj
# #
# #     def push_front(self, obj):
# #         if self.top is None:
# #             self.__last = self.top = obj
# #         else:
# #             obj.next = self.top
# #             self.top = obj
# #
# #     def __iter__(self):
# #         h = self.top
# #         while h:
# #             yield h
# #             h = h.next
# #
# #     def __len__(self):
# #         return sum(1 for _ in self)
# #
# #     def _get_obj(self, indx):
# #         if type(indx) != int or not (0 <= indx < len(self)):
# #             raise IndexError('неверный индекс')
# #         for i, obj in enumerate(self):
# #             if i == indx:
# #                 return obj
# #
# #     def __getitem__(self, item):
# #         return self._get_obj(item).data
# #
# #     def __setitem__(self, key, value):
# #         self._get_obj(key).data = value
#
#
# # zadaniye 4.1.1
# # class Animal:
# #     def __init__(self, name, old):
# #         self.name = name
# #         self.old = old
# #
# #
# # class Cat(Animal):
# #     def __init__(self, name, old, color, weight):
# #         super().__init__(name, old)
# #         self.color = color
# #         self.weight = weight
# #
# #     def get_info(self):
# #         out = [self.__dict__[i] for i in self.__dict__.keys()]
# #         return f"{out[0]}: {out[1]}, {out[2]}, {out[3]}"
# #
# #
# # class Dog(Animal):
# #     def __init__(self, name, old, breed, size):
# #         super().__init__(name, old)
# #         self.breed = breed
# #         self.size = size
# #
# #     def get_info(self):
# #         out = [self.__dict__[i] for i in self.__dict__.keys()]
# #         return f"{out[0]}: {out[1]}, {out[2]}, {out[3]}"
#
#
# # zadaniye 4.1.5
# # class Thing:
# #     __id = 0
# #
# #     def __init__(self, name, price):
# #         self.id = self.__get_id()
# #         self.name = name
# #         self.price = price
# #         self.weight = None
# #         self.dims = None
# #         self.memory = None
# #         self.frm = None
# #
# #     @classmethod
# #     def __get_id(cls):
# #         Thing.__id += 1
# #         return Thing.__id
# #
# #     def get_data(self):
# #         list_tuple = [self.__dict__[i] for i in self.__dict__.keys()]
# #         list_tuple = tuple(list_tuple)
# #         return list_tuple
# #
# #
# # class Table(Thing):
# #     def __init__(self, name, price, weight, dims):
# #         super().__init__(name, price)
# #         self.weight = weight
# #         self.dims = dims
# #
# #
# # class ElBook(Thing):
# #     def __init__(self, name, price, memory, frm):
# #         super().__init__(name, price)
# #         self.memory = memory
# #         self.frm = frm
# #
# #
# # table = Table("Круглый", 1024, 812.55, (700, 750, 700))
# # book = ElBook("Python ООП", 2000, 2048, 'pdf')
# # print(*table.get_data())
# # print(*book.get_data())
#
#
# # zadaniye 4.1.6
# # class GenericView:
# #     def __init__(self, methods=('GET',)):
# #         self.methods = methods
# #
# #     def get(self, request):
# #         return ""
# #
# #     def post(self, request):
# #         pass
# #
# #     def put(self, request):
# #         pass
# #
# #     def delete(self, request):
# #         pass
# #
# #
# # class DetailView(GenericView):
# #     def render_request(self, request, method):
# #         if method.upper() not in self.methods:
# #             raise TypeError('данный запрос не может быть выполнен')
# #         if getattr(self, method.lower(), False):
# #             return getattr(self, method.lower(), False)(request)
# #
# #     def get(self, request):
# #         if type(request) != dict:
# #             raise TypeError('request не является словарем')
# #         if 'url' not in request:
# #             raise TypeError('request не содержит обязательного ключа url')
# #         return f"url: {request['url']}"
# #
# #
# # dv = DetailView()
# # html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')   # url: https://site.ru/home
# # print(html)
#
#
# # zadaniye 4.1.7
# # class Singleton:
# #     __obj = None
# #     __obj_base = None
# #
# #     def __new__(cls, *args, **kwargs):
# #         if cls == Singleton:
# #             if cls.__obj_base is None:
# #                 cls.__obj_base = object.__new__(cls)
# #             return cls.__obj_base
# #
# #         if cls.__obj is None:
# #             cls.__obj = super().__new__(cls)
# #         return cls.__obj
# #
# #
# # class Game(Singleton):
# #     def __init__(self, name):
# #         if 'name' not in self.__dict__:
# #             self.name = name
# #
# #
# # g = Game("game")
# # g1 = Game('game1')
#
#
#
#
# #zadaniye 4.1.8
# # class Validator:
# #     def _is_valid(self, data):
# #         return True
# #
# #     def __call__(self, data):
# #         if not self._is_valid(data):
# #             raise ValueError('данные не прошли валидацию')
# #
# #
# # class IntegerValidator(Validator):
# #     def __init__(self, min_value, max_value):
# #         self.min_value = min_value
# #         self.max_value = max_value
# #
# #     def _is_valid(self, data):
# #         return type(data) == int and self.min_value <= data <= self.max_value
# #
# #
# # class FloatValidator(Validator):
# #     def __init__(self, min_value, max_value):
# #         self.min_value = min_value
# #         self.max_value = max_value
# #
# #     def _is_valid(self, data):
# #         return type(data) == float and self.min_value <= data <= self.max_value
# #
# #
# # integer_validator = IntegerValidator(-10, 10)
# # float_validator = FloatValidator(-1, 1)
# # res1 = integer_validator(10)  # исключение не генерируется (проверка проходит)
# # res2 = float_validator(0.2)    # исключение ValueError
# # print(res2, res1)
#
#
# #zadaniye 4.1.9
# # class Layer:
# #     def __init__(self, name='Layer'):
# #         self.next_layer = None
# #         self.name = name
# #
# #     def __call__(self, layer):
# #         self.next_layer = layer
# #         return layer
# #
# #
# # class Input(Layer):
# #     def __init__(self, inputs):
# #         self.inputs = inputs
# #         super().__init__(name='Input')
# #
# #
# # class Dense(Layer):
# #     def __init__(self, inputs, outputs, activation):
# #         self.inputs = inputs
# #         self.outputs = outputs
# #         self.activation = activation
# #         super().__init__(name='Dense')
# #
# #
# # class NetworkIterator:
# #     def __init__(self, network):
# #         self.network = network
# #
# #     def __iter__(self):
# #         while self.network:
# #             yield self.network
# #             self.network = self.network.next_layer
#
#
# #zadaniye 4.1.10
#
#
# # class Vector:
# #     _all_type = (int, float)
# #
# #     def __init__(self, *args):
# #         self.__check_args(args)
# #         self._args = args
# #
# #     def __check_args(self, args):
# #         if not all(type(x) in self._all_type for x in args):
# #             raise ValueError('неверный тип координат')
# #
# #     def __len__(self):
# #         return len(self._args)
# #
# #     def __make_vector(self, args):
# #         try:
# #             return self.__class__(*args)
# #         except ValueError:
# #             return __class__(*args)
# #
# #     def __add__(self, other):
# #         if len(self) == len(other):
# #             args = tuple(a + b for a, b in zip(self._args, other.get_coords()))
# #             return self.__make_vector(args)
# #         else:
# #             raise TypeError('размерности векторов не совпадают')
# #
# #     def __sub__(self, other):
# #         if len(self) == len(other):
# #             args = tuple(a - b for a, b in zip(self._args, other.get_coords()))
# #             return self.__make_vector(args)
# #         else:
# #             raise TypeError('размерности векторов не совпадают')
# #
# #     def get_coords(self):
# #         return tuple(self._args)
# #
# #
# # class VectorInt(Vector):
# #     _all_type = (int,)
# #
# #
# #
# #
# #
# # v1 = Vector(1, 2, 3)
# # v2 = Vector(3, 4, 5)
# # v = v1 + v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
# # v = v1 - v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
# # v3 = VectorInt(1, 2, 3, 4)
# # v4 = VectorInt(1, 1, 3, 4) # ошибка: генерируется исключение raise ValueError('координаты должны быть целыми числами')
# # v = v3 + v4
# # print(v)
#
#
# #zadaniye 4.2.4
# # class ListInteger(list):
# #     def __init__(self, value):
# #         for i in value:
# #             self.__check_type(i)
# #
# #         super().__init__(value)
# #
# #     @staticmethod
# #     def __check_type(value):
# #         if type(value) != int:
# #             raise TypeError('можно передавать только целочисленные значения')
# #
# #     def __setitem__(self, key, value):
# #         self.__check_type(value)
# #         super().__setitem__(key, value)
# #
# #     def append(self, value):
# #         self.__check_type(value)
# #         super().append(value)
# # s = ListInteger((1, 2, 3))
# # s[1] = 10
# # s.append(11)
# # print(s)
# # # s[0] = 10.5 # TypeError
#
#
#
#
# #zadaniye 4.2.4
# # class Thing:
# #     def __init__(self, name, price, weight):
# #         self.name = name
# #         self.price = price
# #         self.weight = weight
# #
# #     def __hash__(self):
# #         return hash((self.name, self.price, self.weight))
# #
# #
# # class DictShop(dict):
# #     def __init__(self, things=None):
# #         things = {} if things is None else things
# #
# #         if not isinstance(things, dict):
# #             raise TypeError('аргумент должен быть словарем')
# #         if things and not all(isinstance(key, Thing) for key in things):
# #             raise TypeError('ключами могут быть только объекты класса Thing')
# #         super().__init__(things)
# #
# #     def __setitem__(self, key, value):
# #         if not isinstance(key, Thing):
# #             raise TypeError('ключами могут быть только объекты класса Thing')
# #         super().__setitem__(key, value)
#
#
# #zadaniye 4.2.5
# # class Protists:
# #     def __init__(self, name, weight, old):
# #         self.name = name
# #         self.weight = weight
# #         self.old = old
# #
# #
# # class Plants(Protists): pass
# #
# #
# # class Animals(Protists): pass
# #
# #
# # class Mosses(Plants): pass
# #
# #
# # class Flowering(Plants): pass
# #
# #
# # class Worms(Animals): pass
# #
# #
# # class Mammals(Animals): pass
# #
# #
# # class Human(Mammals): pass
# #
# #
# # class Monkeys(Mammals): pass
# #
# #
# # class Monkey(Monkeys):
# #     def __init__(self, name, weight, old):
# #         super().__init__(name, weight, old)
# #
# #
# # class Person(Human):
# #     def __init__(self, name, weight, old):
# #         super().__init__(name, weight, old)
# #
# #
# # class Flower(Flowering):
# #     def __init__(self, name, weight, old):
# #         super().__init__(name, weight, old)
# #
# #
# # class Worm(Worms):
# #     def __init__(self, name, weight, old):
# #         super().__init__(name, weight, old)
# #
# #
# # lst_objs = [Monkey("мартышка", 30.4, 7), Monkey("шимпанзе", 24.6, 8),
# #             Person("Балакирев", 88, 34), Person("Верховный жрец", 67.5, 45),
# #             Flower("Тюльпан", 0.2, 1), Flower("Роза", 0.1, 2),
# #             Worm("червь", 0.01, 1), Worm("червь 2", 0.02, 1)]
# #
# # lst_animals = list(filter(lambda x: isinstance(x, Animals), lst_objs))
# # lst_plants = list(filter(lambda x: isinstance(x, Plants), lst_objs))
# # lst_mammals = list(filter(lambda x: isinstance(x, Mammals), lst_objs))
#
#
#
# #zadaniye 4.2.6
# class Tuple(tuple):
#     def __add__(self, other):
#         obj = list(self)
#         for i in other:
#             obj.append(i)
#         return Tuple(obj)
#
# t = Tuple([1, 2, 3])
# print(t)
# t = t + "Python"
# print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
# t = (t + "Python") + "ООП"


# zadaniye 4.2.7
# class VideoItem:
#     def __init__(self, title, descr, path):
#         self.title = title
#         self.descr = descr
#         self.path = path
#         self.rating = VideoRating()
#
#
# class VideoRating:
#     def __init__(self):
#         self.__rating = 0
#
#     @property
#     def rating(self):
#         return self.__rating
#
#     @rating.setter
#     def rating(self, value):
#         if 0 <= value <= 5:
#             self.__rating = value
#         else:
#             raise ValueError('неверное присваиваемое значение')
#
# v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
# print(v.rating.rating) # 0
# v.rating.rating = 5
# print(v.rating.rating) # 5
# title = v.title
# descr = v.descr


# zadaniye 4.2.9
# class IteratorAttrs:
#     def __iter__(self):
#         for x in self.__dict__.items():
#             yield x
#
#
#
# class SmartPhone(IteratorAttrs):
#     def __init__(self, model, size, memory):
#         self.model = model
#         self.size = size
#         self.memory = memory
#
#
# phone = SmartPhone("IChlen", (12, 15), 2046)
#
# for attr, value in phone:
#     print(attr, value)


# zadaniye 4.3.4
# class Thing:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#
#
# class ArtObject(Thing):
#     def __init__(self, name, weight, author, date):
#         super().__init__(name, weight)
#         self.author = author
#         self.date = date
#
#
# class Computer(Thing):
#     def __init__(self, name, weight, memory, cpu):
#         super().__init__(name, weight)
#         self.memory = memory
#         self.cpu = cpu
#
#
# class Auto(Thing):
#     def __init__(self, name, weight, dims):
#         super().__init__(name, weight)
#         self.dims = dims
#
#
# class Mercedes(Auto):
#     def __init__(self, name, weight, dims, model, old):
#         super().__init__(name, weight, dims)
#         self.model = model
#         self.old = old
#
#
# class Toyota(Auto):
#     def __init__(self, name, weight, dims, model, wheel):
#         super().__init__(name, weight, dims)
#         self.model = model
#         self.wheel = wheel



#zadaniye 4.3.5
# class SellItem:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Flat(SellItem):
#     def __init__(self, name, price, size, rooms):
#         super().__init__(name, price)
#         self.size = size
#         self.rooms = rooms
#
#
# class House(SellItem):
#     def __init__(self, name, price, material, square):
#         super().__init__(name, price)
#         self.material = material
#         self.square = square
#
#
# class Land(SellItem):
#     def __init__(self, name, price, square):
#         super().__init__(name, price)
#         self.square = square
#
#
# class Agency:
#     def __init__(self, name):
#         self.name = name
#         self.list_agency = []
#
#     def add_object(self, obj):
#         self.list_agency.append(obj)
#
#     def remove_object(self, obj):
#         self.list_agency.remove(obj)
#
#     def get_objects(self):
#         return self.list_agency
#
# ag = Agency("Рога и копыта")
# ag.add_object(Flat("квартира, 3к", 10000000, 121.5, 3))
# ag.add_object(Flat("квартира, 2к", 8000000, 74.5, 2))
# ag.add_object(Flat("квартира, 1к", 4000000, 54, 1))
# ag.add_object(House("дом, крипичный", price=35000000, material="кирпич", square=186.5))
# ag.add_object(Land("участок под застройку", 3000000, 6.74))
# for obj in ag.get_objects():
#     print(obj.name)
#
# lst_houses = [x for x in ag.get_objects() if isinstance(x, House)] # выделение списка домов



#zadaniye 4.3.6
class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func


class Callback:
    def __init__(self, path, router_cls):
        self.__path = path
        self.__router_cls = router_cls

    def __call__(self, func):
        self.__router_cls.add_callback(self.__path, func)


@Callback('/', Router)
def index():
    return '<h1>Главная</h1>'


route = Router.get('/')
if route:
    ret = route()
    print(ret)

#Разобраться с этим заданием!!!!!!!