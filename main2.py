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


# zadaniye 4.3.5
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



# zadaniye 4.3.6
# class Router:
#     app = {}
#
#     @classmethod
#     def get(cls, path):
#         return cls.app.get(path)
#
#     @classmethod
#     def add_callback(cls, path, func):
#         cls.app[path] = func
#
#
# class Callback:
#     def __init__(self, path, router_cls):
#         self.__path = path
#         self.__router_cls = router_cls
#
#     def __call__(self, func):
#         self.__router_cls.add_callback(self.__path, func)
#
#
# @Callback('/', Router)
# def index():
#     return '<h1>Главная</h1>'
#
#
# route = Router.get('/')
# if route:
#     ret = route()
#     print(ret)

# Разобраться с этим заданием!!!!!!!


# zadaniye 4.3.7
# def integer_params_decorated(func):
#     print(f'func-----{func}')
#     def wrapper(self, *args, **kwargs):
#         if not all(type(x) == int for x in args):
#             raise TypeError("аргументы должны быть целыми числами")
#         if not all(type(x) == int for x in kwargs.values()):
#             raise TypeError("аргументы должны быть целыми числами")
#         return func(self, *args, **kwargs)
#     return wrapper
#
# def integer_params(cls):
#     methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
#     print(f'cls.__dict__{cls.__dict__}')
#     print(methods)
#     for k, v in methods.items():
#         print(f'key ----{k}', f'value -----{v}')
#         setattr(cls, k, integer_params_decorated(v))
#
#     return cls
#
#
# @integer_params
# class Vector:
#     def __init__(self, *args):
#         self.__coords = list(args)
#
#     def __getitem__(self, item):
#         return self.__coords[item]
#
#     def __setitem__(self, key, value):
#         self.__coords[key] = value
#
#     def set_coords(self, *coords, reverse=False):
#         c = list(coords)
#         self.__coords = c if not reverse else c[::-1]
#
#     def get_coords(self):
#         return self.__coords
#
#
# vector = Vector(1, 2)
# print(vector[1])
# Важное задание обязательно его нужно разобрать!!!


# zadaniye 4.3.8
# class SoftList(list):
#     def __getitem__(self, item):
#         try:
#             return super().__getitem__(item)
#         except IndexError:
#             return False
#
#
# sl = SoftList("python")
# sl[0]  # 'p'
# print(sl[-1])  # 'n'
# print(sl[6])  # False
# print(sl[-7])  # False


# zadaniye 4.3.9
# import string
#
#
# class StringDigit(str):
#     def __init__(self, string_d):
#         self.__check_string(string_d)
#         super().__init__()
#
#     @staticmethod
#     def __check_string(value):
#         if not all(x in string.digits for x in value):
#             raise ValueError("в строке должны быть только цифры")
#
#     def __add__(self, other):
#         self.__check_string(other)
#         return __class__(super().__add__(other))
#
#     def __radd__(self, other):
#         self.__check_string(other)
#
#         return __class__(other).__add__(self)
#
#
# sd = StringDigit("123")
# print(sd)       # 123
# sd = sd + "456" # StringDigit: 123456
# print(sd)
# sd = "789" + sd # StringDigit: 789123456
# print(sd)
# sd = sd + "12f" # ValueError
# print(sd)


# #zadaniye 4.3.11
# class ItemAttrs:
#     def __getitem__(self, item):
#         return self.coords[item]
#
#     def __setitem__(self, key, value):
#         self.coords[key] = value
#
#
# class Point(ItemAttrs):
#     def __init__(self, x, y):
#         self.coords = [x, y]
#
#
# pt = Point(1, 2.5)
# x = pt[0]   # 1
# print(x)
# y = pt[1]   # 2.5
# print(y)
# pt[0] = 10
# print(pt.coords)

# class Animal:
#     def __init__(self, name, kind, old):
#         self.__name = name
#         self.__kind = kind
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     @property
#     def kind(self):
#         return self.__kind
#
#     @kind.setter
#     def kind(self, value):
#         self.__kind = value
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, value):
#         self.__old = value
#
#
# s = """Васька; дворовый кот; 5
# Рекс; немецкая овчарка; 8
# Кеша; попугай; 3"""
#
# animals = [Animal(*line.split('; ')) for line in s.splitlines()]
# print(animals)


# решить данное задание через дескрипторы #ПЕРЕРЕШАТЬ
# class Furniture:
#     def __init__(self, name, weight):
#         self.__verify_name(name)
#         self._name = name
#         self.__verify_weight(weight)
#         self._weight = weight
#
#     def __setattr__(self, key, value):
#         # print(f"__setattr__{self}")
#         if key == 'name':
#             self.__verify_name(value)
#         if key == 'weight':
#             self.__verify_weight(value)
#         object.__setattr__(self, key, value)
#
#     def __verify_name(self, value):
#         if type(value) != str:
#             raise TypeError('название должно быть строкой')
#
#     def __verify_weight(self, value):
#         if not isinstance(value, (int, float)) or not value > 0:
#             raise TypeError('вес должен быть положительным числом')
#
#
# class Closet(Furniture):
#     def __init__(self, name, weight, tp, doors):
#         super().__init__(name, weight)
#         self._tp = tp
#         self._doors = doors
#
#     def get_attrs(self) -> tuple:
#         return tuple(self.__dict__.values())
#
#
# class Chair(Furniture):
#     def __init__(self, name, weight, height):
#         super().__init__(name, weight)
#         self._height = height
#
#     def get_attrs(self) -> tuple:
#         return tuple(self.__dict__.values())
#
#
# class Table(Furniture):
#     def __init__(self, name, weight, height, square):
#         super().__init__(name, weight)
#         self._height = height
#         self._square = square
#
#     def get_attrs(self) -> tuple:
#         return tuple(self.__dict__.values())
#
# cl = Closet('шкаф-купе', 342.56, True, 3)
# chair = Chair('стул', 14, 55.6)
# tb = Table('стол', 4, 75, 10)
# print(tb.get_attrs())


# zadaniye 4.4.7
# class Observer:
#     def update(self, data):
#         pass
#
#     def __hash__(self):
#         return hash(id(self))
#
#
# class Subject:
#     def __init__(self):
#         self.__observers = {}
#         self.__data = None
#
#     def add_observer(self, observer):
#         self.__observers[observer] = observer
#
#     def remove_observer(self, observer):
#         if observer in self.__observers:
#             self.__observers.pop(observer)
#
#     def __notify_observer(self):
#         for ob in self.__observers:
#             ob.update(self.__data)
#
#     def change_data(self, data):
#         self.__data = data
#         self.__notify_observer()
#
#
# class Data:
#     def __init__(self, temp, press, wet):
#         self.temp = temp    # температура
#         self.press = press  # давление
#         self.wet = wet      # влажность
#
#
# class TemperatureView(Observer):
#     def update(self, data):
#         if data:
#             print(f'Текущая температура {data.temp}')
#
#
# class PressureView(Observer):
#     def update(self, data):
#         if data:
#             print(f'Текущее давление {data.press}')
#
#
# class WetView(Observer):
#     def update(self, data):
#         if data:
#             print(f'Текущая влажность {data.wet}')
#
# subject = Subject()
# tv = TemperatureView()
# pr = PressureView()
# wet = WetView()
#
# subject.add_observer(tv)
# subject.add_observer(pr)
# subject.add_observer(wet)
# subject.change_data(Data(23, 150, 83))
# subject.remove_observer(wet)
# subject.change_data(Data(24, 148, 80))
# ВАЖНОЕ ЗАДАНИЕ!!! РАЗОБРАТЬСЯ #ВАЖНОЕ


# zadaniye 4.4.8
# class Aircraft:
#     def __init__(self, model, mass, speed, top):
#         self._model = model
#         self._mass = mass
#         self._speed = speed
#         self._top = top
#
#     def __setattr__(self, key, value):
#         if key == "_model" and type(value) != str:
#             raise TypeError('неверный тип аргумента')
#         if key == "_mass" or key == "_speed" or key == "_top":
#             if not isinstance(value, (int, float)) or value < 0:
#                 raise TypeError('неверный тип аргумента')
#         object.__setattr__(self, key, value)
#
#
# class PassengerAircraft(Aircraft):
#     def __init__(self, model, mass, speed, top, chairs):
#         super().__init__(model, mass, speed, top)
#         if type(chairs) != int:
#             raise TypeError('неверный тип аргумента')
#         self._chairs = chairs
#
#
# class WarPlane(Aircraft):
#     def __init__(self, model, mass, speed, top, weapons):
#         super().__init__(model, mass, speed, top)
#         if type(weapons) != dict:
#             raise TypeError('неверный тип аргумента')
#         self._weapons = weapons
#
#
# planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
#           PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
#           WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
#           WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]
#
#
# print(planes[0].__dict__)


# zadaniye 4.4.9
# def class_log(log_lst):
#     def log_method(cls):
#         methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
#         for k, v in methods.items():
#             setattr(cls, k, log_method_decorator(v))
#
#         return cls
#
#     def log_method_decorator(func):
#         def wrapper(*args, **kwargs):
#             log_lst.append(func.__name__)
#             return func(*args, **kwargs)
#         return wrapper
#     return log_method
#
#
#
# vector_log = []
#
# @class_log(vector_log)
# class Vector:
#     def __init__(self, *args):
#         self.__coords = list(args)
#
#     def __getitem__(self, item):
#         return self.__coords[item]
#
#     def __setitem__(self, key, value):
#         self.__coords[key] = value
#
#
# v = Vector(1, 2, 3)
# v[0] = 10
# print(vector_log)

# CURRENT_OS = 'windows'   # 'windows', 'linux'
#
#
# class WindowsFileDialog:
#     def __init__(self, title, path, exts):
#         self.__title = title # заголовок диалогового окна
#         self.__path = path  # начальный каталог с файлами
#         self.__exts = exts  # кортеж из отображаемых расширений файлов
#
#
# class LinuxFileDialog:
#     def __init__(self, title, path, exts):
#         self.__title = title # заголовок диалогового окна
#         self.__path = path  # начальный каталог с файлами
#         self.__exts = exts  # кортеж из отображаемых расширений файлов
#
#
# class FileDialogFactory:
#     def __new__(cls, *args, **kwargs):
#         if CURRENT_OS == 'windows':
#             return FileDialogFactory.create_windows_filedialog(args[0], args[1], args[2])
#         else:
#             return FileDialogFactory.create_linux_filedialog(args[0], args[1], args[2])
#
#     @classmethod
#     def create_windows_filedialog(cls, title, path, exts):
#         return WindowsFileDialog(title, path, exts)
#
#     @classmethod
#     def create_linux_filedialog(cls, title, path, exts):
#         return LinuxFileDialog(title, path, exts)
# dlg = FileDialogFactory('Изображения', 'd:/images/', ('jpg', 'gif', 'bmp', 'png'))


# zadaniye 4.5.3
# class Student:
#     def __init__(self, fio, group):
#         self._fio = fio
#         self._group = group
#         self._lect_marks = []  # оценки за лекции
#         self._house_marks = []  # оценки за домашние задания
#
#     def add_lect_marks(self, mark):
#         self._lect_marks.append(mark)
#
#     def add_house_marks(self, mark):
#         self._house_marks.append(mark)
#
#     def __str__(self):
#         return f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; оценки за д/з: {str(self._house_marks)}"
#
#
# class Mentor:
#     def __init__(self, fio, subject):
#         self._fio = fio
#         self._subject = subject
#
#
# class Lector(Mentor):
#     def set_mark(self, student, mark):
#         Student.add_lect_marks(student, mark)
#
#     def __str__(self):
#         return f"Лектор {self._fio}: предмет {self._subject}"
#
#
# class Reviewer(Mentor):
#     def set_mark(self, student, mark):
#         Student.add_house_marks(student, mark)
#
#     def __str__(self):
#         return f"Эксперт {self._fio}: предмет {self._subject}"
#
#
# lector = Lector("Балакирев С.М.", "Информатика")
# reviewer = Reviewer("Гейтс Б.", "Информатика")
# students = [Student("Иванов А.Б.", "ЭВМд-11"), Student("Гаврилов С.А.", "ЭВМд-11")]
# persons = [lector, reviewer]
# lector.set_mark(students[0], 4)
# lector.set_mark(students[1], 2)
# reviewer.set_mark(students[0], 5)
# reviewer.set_mark(students[1], 3)
# for p in persons + students:
#     print(p)
# # в консоли будет отображено:
# # Лектор Балакирев С.М.: предмет Информатика
# # Эксперт Гейтс Б.: предмет Информатика
# # Студент Иванов А.Б.: оценки на лекциях: [4]; оценки за д/з: [5]
# # Студент Гаврилов С.А.: оценки на лекциях: [2]; оценки за д/з: [3]


# zadaniye 4.5.4
# class ShopInterface:
#     def get_id(self):
#         raise NotImplementedError('в классе не переопределен метод get_id')
#
#
# class ShopItem(ShopInterface):
#     def __init__(self, name, weight, price):
#         self._name = name
#         self._weight = weight
#         self._price = price
#         self.__id = hash((self._name, self._weight, self._price))
#
#     def get_id(self):
#         return self.__id
#
# item1 = ShopItem("имя1", "вес1", "100")
# item2 = ShopItem("имя1", "вес1", "100")
# print(item1.get_id())
# print(item2.get_id())


# zadaniye 4.5.5
# class Validator:
#     def _is_valid(self, data):
#         raise NotImplementedError('в классе не переопределен метод _is_valid')
#
#     def __call__(self, data):
#         return self._is_valid(data)
#
#
# class FloatValidator(Validator):
#     def __init__(self, min_value, max_value):
#         self.min_value = min_value
#         self.max_value = max_value
#
#     def _is_valid(self, data):
#         return type(data) == float and self.min_value <= data <= self.max_value
#
#
# float_validator = FloatValidator(0, 10.5)
# res_1 = float_validator(10)  # False (целое число, а не вещественное)
# res_2 = float_validator(1.0)  # True
# res_3 = float_validator(-1.0)  # False (выход за диапазон [0; 10.5])
# print(res_1)
# print(res_2)
# print(res_3)


# zadaniye 4.5.6
# from abc import ABC, abstractmethod
#
#
# class Model(ABC):
#     @abstractmethod
#     def get_pk(self):
#         pass
#
#     def get_info(self):
#         return f"Базовый класс Model"
#
#
# class ModelForm(Model):
#     __last_id = 1
#     def __init__(self, login, password):
#         self._login = login
#         self._password = password
#         self._id = self.__last_id
#         type(self).__last_id += 1
#
#     def get_pk(self):
#         return self._id
#
#
# form = ModelForm("Логин", "Пароль")
# print(form.get_pk())


# zadaniye 4.5.7
# from abc import ABC, abstractmethod
#
#
# class StackInterface(ABC):
#     @abstractmethod
#     def push_back(self, obj):
#         pass
#
#     @abstractmethod
#     def pop_back(self):
#         pass
#
#
# class Stack(StackInterface):
#     def __init__(self):
#         self._top = None
#         self.__last = None
#
#     def push_back(self, obj):
#         if self.__last:
#             self.__last.next = obj
#         self.__last = obj
#
#         if self._top is None:
#             self._top = obj
#
#     def pop_back(self):
#         h = self._top
#         if h is None:
#             return
#         last_obj = self.__last
#         while h.next and h.next != self.__last:
#             h = h.next
#
#         if self._top == self.__last:
#             self._top = self.__last = None
#         else:
#             h.next = None
#             self.__last = h
#         return last_obj
#
#
# class StackObj:
#     def __init__(self, data):
#         self._data = data
#         self._next = None
#
#     @property
#     def data(self):
#         return self._data
#
#     @property
#     def next(self):
#         return self._next
#
#     @next.setter
#     def next(self, obj):
#         self._next = obj
#
#
# st = Stack()
# st.push_back(StackObj("obj 1"))
# obj = StackObj("obj 2")
# st.push_back(obj)
# del_obj = st.pop_back() # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
# print(del_obj)


# zadaniye 4.5.8
# from abc import ABC, abstractmethod
#
#
# class CountryInterface(ABC):
#     @property
#     @abstractmethod
#     def name(self):
#         pass
#
#     @property
#     @abstractmethod
#     def population(self):
#         pass
#
#     @property
#     @abstractmethod
#     def square(self):
#         pass
#
#     @abstractmethod
#     def get_info(self):
#         pass
#
#
# class Country(CountryInterface):
#     def __init__(self, name, population, square):
#         self._name = name
#         self._population = population
#         self._square = square
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         self._name = value
#
#     @property
#     def population(self):
#         return self._population
#
#     @population.setter
#     def population(self, value):
#         self._population = value
#
#     @property
#     def square(self):
#         return self._square
#
#     @square.setter
#     def square(self, value):
#         self._square = value
#
#     def get_info(self):
#         return f"{self._name}: {self._square}, {self._population}"
#
#
# country = Country("Россия", 140000000, 324005489.55)
# name = country.name
# pop = country.population
# print(name)
# print(pop)
# country.population = 150000000
# country.square = 354005483.0
# print(country.get_info()) # Россия: 354005483.0, 150000000

# class Track:
#     def __init__(self, *args):
#         self.__points = []
#         if len(args) == 2 and isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)):
#             self.__points.append(PointTrack(args[0], args[1]))
#         else:
#             for i in args:
#                 self.__points.append(i)
#
#     def add_back(self, pt):
#         self.__points.append(pt)
#
#     def add_front(self, pt):
#         self.__points.insert(0, pt)
#
#     def pop_back(self):
#         self.__points.pop(-1)
#
#     def pop_front(self):
#         self.__points.pop(0)
#
#     @property
#     def points(self):
#         return tuple(self.__points)
#
#
# class PointTrack:
#     def __init__(self, x, y):
#         if type(x) not in (int, float) or type(y) not in (int, float):
#             raise TypeError('координаты должны быть числами')
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"PointTrack: {self.x}, {self.y}"
#
#
# tr = Track(PointTrack('0', 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
# tr.add_back(PointTrack(1.4, 0))
# tr.pop_front()
# for pt in tr.points:
#     print(pt)


# zadaniye 4.5.10

# class Food:
#     def __init__(self, name, weight, calories):
#         self._name = name
#         self._weight = weight
#         self._calories = calories
#
#
# class BreadFood(Food):
#     def __init__(self, name, weight, calories, white):
#         super().__init__(name, weight, calories)
#         self._white = white
#
#
# class SoupFood(Food):
#     def __init__(self, name, weight, calories, dietary):
#         super().__init__(name, weight, calories)
#         self._dietary = dietary
#
#
# class FishFood(Food):
#     def __init__(self, name, weight, calories, fish):
#         super().__init__(name, weight, calories)
#         self._fish = fish
#
#
# bf = BreadFood("Бородинский хлеб", 34.5, 512, False)
# sf = SoupFood("Черепаший суп", 520, 890.5, False)
# ff = FishFood("Консерва рыбная", 340, 1200, "семга")
# print(bf)

class Digit:
    def __init__(self, value):
        self.__check_digit(value)
        self.value = value

    @staticmethod
    def __check_digit(value):
        if type(value) not in (int, float):
            raise TypeError('значение не соответствует типу объекта')


class Integer(Digit):
    def __init__(self, value):
        super().__init__(value)
        self.__check_digit(value)
        self.value = value

    @staticmethod
    def __check_digit(value):
        if type(value) not in (int, ):
            raise TypeError('значение не соответствует типу объекта')


class Float(Digit):
    def __init__(self, value):
        super().__init__(value)
        self.__check_digit(value)
        self.value = value

    @staticmethod
    def __check_digit(value):
        if type(value) not in (float, ):
            raise TypeError('значение не соответствует типу объекта')


class Positive(Digit):
    def __init__(self, value):
        super().__init__(value)
        self.__check_digit(value)
        self.value = value

    @staticmethod
    def __check_digit(value):
        if value < 0:
            raise TypeError('значение не соответствует типу объекта')


class Negative(Digit):
    def __init__(self, value):
        super().__init__(value)
        self.__check_digit(value)
        self.value = value

    @staticmethod
    def __check_digit(value):
        if value > 0:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass



digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), FloatPositive(1.5), FloatPositive(9.2), FloatPositive(6.5),
          FloatPositive(3.5), FloatPositive(8.9)]


lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))
print(lst_float)
print(lst_positive)
n = Float(1.0)
n = FloatPositive(1.0)