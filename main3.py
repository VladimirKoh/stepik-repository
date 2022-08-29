# hi, this 3 part!# class Person:#     __slots__ = '_fio', '_old', '_job',##     def __init__(self, fio, old, job):#         self._fio = fio#         self._old = old#         self._job = job## persons = [Person('Суворов', 52, 'полководец'),#            Person('Рахманинов', 50, 'пианист, композитор'),#            Person('Балакирев', 34, 'программист и преподаватель'),#            Person('Пушкин', 32, 'поэт и писатель')]# zadaniye 4.7.6# class Planet:#     def __init__(self, name, diametr, period_solar, period):#         self._name = name#         self._diametr = diametr#         self._period_solar = period_solar#         self._period = period### class SolarSystem:#     __obj = None#     __slots__ = ('_mercury', '_venus', '_earth', '_mars', '_jupiter', '_saturn', '_uranus', '_neptune')##     def __new__(cls, *args, **kwargs):#         if cls.__obj is None:#             cls.__obj = super().__new__(cls)#         return cls.__obj###     def __init__(self):#         self._mercury = Planet('Меркурий', 4878, 87.97, 1407.5)#         self._venus = Planet('Венера', 12104, 224.7, 5832.45)#         self._earth = Planet('Земля', 12756, 365.3, 23.93)#         self._mars = Planet('Марс', 6794, 687, 24.62)#         self._jupiter = Planet('Юпитер', 142800, 4330, 9.9)#         self._saturn = Planet('Сатурн', 120660, 10753, 10.63)#         self._uranus = Planet('Уран', 51118, 30665, 17.2)#         self._neptune = Planet('Нептун', 49528, 60150, 16.1)### s_system = SolarSystem()# zadaniye 4.7.7# class Star:#     __slots__ = '_name', '_massa', '_temp',##     def __init__(self, name, massa, temp):#         self._name = name#         self._massa = massa#         self._temp = temp### class WhiteDwarf(Star):#     __slots__ = '_type_star', '_radius',##     def __init__(self, name, massa, temp, type_star, radius):#         super().__init__(name, massa, temp)#         self._type_star = type_star#         self._radius = radius### class YellowDwarf(Star):#     __slots__ = '_type_star', '_radius',##     def __init__(self, name, massa, temp, type_star, radius):#         super().__init__(name, massa, temp)#         self._type_star = type_star#         self._radius = radius### class RedGiant(Star):#     __slots__ = '_type_star', '_radius',##     def __init__(self, name, massa, temp, type_star, radius):#         super().__init__(name, massa, temp)#         self._type_star = type_star#         self._radius = radius### class Pulsar(Star):#     __slots__ = '_type_star', '_radius',##     def __init__(self, name, massa, temp, type_star, radius):#         super().__init__(name, massa, temp)#         self._type_star = type_star#         self._radius = radius### stars = [RedGiant('Альдебаран', 5, 3600, 'красный гигант', 45),#          WhiteDwarf('Сириус А', 2.1, 9250, 'белый карлик', 2),#          WhiteDwarf('Сириус B', 1, 8200, 'белый карлик', 0.01),#          YellowDwarf('Солнце', 1, 6000, 'желтый карлик', 1)]### white_dwarfs = list(filter(lambda x: isinstance(x, WhiteDwarf), stars))# print(white_dwarfs)# class Note:#     _cyrillic_notes = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')##     def __init__(self, name, ton):#         self._name = name#         self._ton = ton##     def __setattr__(self, key, value):#         if key == '_name' and value not in self._cyrillic_notes:#             raise ValueError('недопустимое значение аргумента')#         if key == '_ton' and value not in (-1, 0, 1):#             raise ValueError('недопустимое значение аргумента')#         object.__setattr__(self, key, value)### class Notes:#     __slots__ = '_do', '_re', '_mi', '_fa', '_solt', '_la', '_si'#     _cyrillic_notes = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')#     _obj = None##     def __new__(cls, *args, **kwargs):#         if cls._obj is None:#             cls._obj = super().__new__(cls)#         return cls._obj##     def __del__(self):#         Notes._obj = None##     def __init__(self):#         self._do = Note('до', 0)#         self._re = Note("ре", 0)#         self._mi = Note("ми", 0)#         self._fa = Note("фа", 0)#         self._solt = Note("соль", 0)#         self._la = Note("ля", 0)#         self._si = Note("си", 0)##     def __getitem__(self, item):#         if not (0 <= item < 7):#             raise IndexError('недопустимый индекс')#         return getattr(self, self.__slots__[item])### n = Notes()# # nota = n[3]# # print(nota)# print(n)# zadaniye 4.7.10# class Function:#     def __init__(self):#         self._amplitude = 1.0     # амплитуда функции#         self._bias = 0.0          # смещение функции по оси Oy##     def __call__(self, x, *args, **kwargs):#         return self._amplitude * self._get_function(x) + self._bias##     def _get_function(self, x):#         raise NotImplementedError('метод _get_function должен быть переопределен в дочернем классе')##     def __add__(self, other):#         if type(other) not in (int, float):#             raise TypeError('смещение должно быть числом')##         obj = self.__class__(self)#         obj._bias = self._bias + other#         return obj##     def __mul__(self, other):#         if type(other) not in (int, float):#             raise TypeError('амплитуда должна быть числом')##         obj = self.__class__(self)#         obj._amplitude *= other#         return obj### class Linear(Function):#     def __init__(self, k=None, b=None):#         super().__init__()#         if type(k) == Linear:#             self._k, self._b = k._k, k._b#         else:#             self._k = k#             self._b = b##     def _get_function(self, x):#         return self._k * x + self._b### f = Linear(1, 0.5)# y1 = f(0)     # 0.5# y2 = f(0)    # 10.5# zadaniye 5.1.5# list_test = "8 11 abcd -7.5 2.0 -5".split()# print(list_test)### def is_str_int(value):#     try:#         return int(value)#     except:#         return False## print(sum(filter(lambda x: not isinstance(x, bool), map(is_str_int, list_test))))## print(sum(map(int, filter(is_str_int, list_test))))# zadaniye 5.1.9# list_test = "1 -5.6 True abc 0 23.56 hello".split()### def is_str_int(value):#     try:#         return int(value)#     except:#         try:#             return float(value)#         except:#             return value### lst_out = list(map(lambda x: is_str_int(x), list_test))# class Triangle:#     def __init__(self, a, b, c):#         self.__check_value(a, b, c)#         self._a = a#         self._b = b#         self._c = c##     @staticmethod#     def __check_value(*args):#         for i in args:#             if type(i) not in (int, float) or i <= 0:#                 raise TypeError('стороны треугольника должны быть положительными числами')##         if args[0] > args[1] + args[2] or args[1] > args[0] + args[2] or args[2] > args[1] + args[0]:#             raise ValueError('из указанных длин сторон нельзя составить треугольник')## input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]# lst_tr = []# for i in input_data:#     try:#         tr = Triangle(*i)#     except(TypeError, ValueError):#         pass#     else:#         lst_tr.append(tr)## print(lst_tr)# zadaniye 5.1.11# class FloatValidator:#     def __init__(self, min_value, max_value):#         self.min_value = min_value#         self.max_value = max_value##     def __call__(self, value):#         if type(value) != float or not (self.min_value <= value <= self.max_value):#             raise ValueError('значение не прошло валидацию')## class IntegerValidator:#     def __init__(self, min_value, max_value):#         self.min_value = min_value#         self.max_value = max_value##     def __call__(self, value):#         if type(value) != int or not (self.min_value <= value <= self.max_value):#             raise ValueError('значение не прошло валидацию')### def is_valid(lst, validators):#     res = []#     for i in lst:#         for v in validators:#             try:#                 v(i)#                 res.append(i)#                 break#             except ValueError:#                 pass#     return res## fv = FloatValidator(0, 10.5)# iv = IntegerValidator(-10, 20)# lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])   # [1, 4.5]# zadaniye# zadaniye 5.2.5# try:#     x, y = input().split()#     res = int(x) + int(y)# except:#     try:#         res = float(x) + float(y)#     except:#         res = x + y# finally:#     print(res)# zadaniye 5.2.6# class Point:#     def __init__(self, x=0, y=0):#         self._x = x#         self._y = y### x, y = input().split()# try:#     pt = Point(int(x), int(y))# except:#     try:#         pt = Point(float(x), float(y))#     except:#         pt = Point()# finally:#     print(f"Point: x = {pt._x}, y = {pt._y}")# zadaniye 5.2.8# def get_loss(w1, w2, w3, w4):#     try:#         z = w1 // w2#     except ZeroDivisionError:#         return 'деление на ноль'#     else:#         y = 10 * z - 5 * w2 * w3 + w4#         return y## get_loss(2, 0, 3, 4)# zadaniye 5.2.9# class Rect:#     def __init__(self, x, y, width, height):#         self.__check_x_y_w_h(x, y, width, height)#         self._x = x#         self._y = y#         self._width = width#         self._height = height##     @staticmethod#     def __check_x_y_w_h(x, y, width, height):#         check = (int, float)#         if type(x) not in check or type(y) not in check or type(width) not in check or type(#                 height) not in check or not width > 0 or not height > 0:#             raise ValueError('некорректные координаты и параметры прямоугольника')##     def _get_coord(self):#         a = self._x, self._y#         # b = self._x + self._weight, self._y#         # c = self._x, self._y - self._height#         d = self._x + self._width, self._y - self._height#         return a, d##     def is_collision(self, rect):#         xyu = [self._get_coord()[0][0] < rect._get_coord()[1][0],#                self._get_coord()[1][0] > rect._get_coord()[0][0],#                self._get_coord()[0][1] >= rect._get_coord()[1][1],#                self._get_coord()[1][1] <= rect._get_coord()[0][1]]#         print(xyu)#         if all(xyu):#             raise TypeError('прямоугольники пересекаются')## def is_collision(r1, r2):#     try:#         r1.is_collision(r2)#     except TypeError:#         return True#     return False## lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]## lst_not_collision = [lst_rect[i] for i in range(len(lst_rect))#                      if not any(is_collision(lst_rect[i], lst_rect[j]) for j in range(len(lst_rect)) if i != j)]### print(lst_not_collision)## r = Rect(3, 2, 2, 5)# rr = Rect(1, 4, 6, 2)# print(r.is_collision(rr))# def input_int_numbers():#     return tuple(int(x) for x in input().split())## while True:#     try:#         print(*input_int_numbers())#         break#     except:#         continue# class ValidatorString:#     def __init__(self, min_length, max_length, chars):#         self.__min_length = min_length#         self.__max_length = max_length#         self.__chars = chars##     def is_valid(self, string):#         if not self.__min_length <= len(string) <= self.__max_length or self.__chars and not any(char in self.__chars for char in string):#             raise ValueError('недопустимая строка')#         return string### class LoginForm:#     def __init__(self, login_validator, password_validator):#         self.login_validator = login_validator#         self.password_validator = password_validator#         self._login = None#         self._password = None##     def form(self, request):#         if "login" not in request or "password" not in request:#             raise TypeError('в запросе отсутствует логин или пароль')#         self._login = self.login_validator.is_valid(request.get('login'))#         self._password = self.password_validator.is_valid(request.get('password'))### login_v = ValidatorString(4, 50, "")# password_v = ValidatorString(10, 50, "!$#@%&?")# lg = LoginForm(login_v, password_v)# login, password = input().split()# try:#     lg.form({'login': login, 'password': password})# except (TypeError, ValueError) as e:#     print(e)# else:#     print(lg._login)#zadaniye 3.5.6# class StringText:#     def __init__(self, lst):#         self.lst_words = list(lst)##     def __len__(self):#         return len(self.lst_words)##     def __lt__(self, other):#         return len(self) < len(other)##     def __le__(self, other):#         return len(self) <= len(other)## stich = ["Я к вам пишу – чего же боле?",#         "Что я могу еще сказать?",#         "Теперь, я знаю, в вашей воле",#         "Меня презреньем наказать.",#         "Но вы, к моей несчастной доле",#         "Хоть каплю жалости храня,",#         "Вы не оставите меня."]# strip_chars = '–?!,.;'# lst_text = [StringText(x.strip(strip_chars) for x in line.split() if len(x.strip(strip_chars)) > 0) for line in stich]# lst_text_sorted = sorted(lst_text, reverse=True)# lst_text_sorted = [' '.join(x.lst_words) for x in lst_text_sorted]