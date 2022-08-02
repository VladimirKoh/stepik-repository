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
class Track:
    def __init__(self, start_x=0, start_y=0):
        self.start_x = start_x
        self.start_y = start_y
        self.__list_Track = []

    def add_track(self, tr):
        self.__list_Track.append(tr)

    def get_tracks(self):
        return tuple(self.__list_Track)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __len__(self):
        len_1 = ((self.start_x - self.__list_Track[0].x) ** 2 + (self.start_y - self.__list_Track[0].y) ** 2) ** 0.5
        return int(len_1 + sum(self.__get_lenght(i) for i in range(1, len(self.__list_Track))))

    def __get_lenght(self, i):
        return ((self.__list_Track[i-1].x - self.__list_Track[i].x) ** 2 + (self.__list_Track[i-1].y - self.__list_Track[i].y) ** 2) ** 0.5



class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self._max_speed = max_speed

    @property
    def x(self):
        return self.to_x

    @property
    def y(self):
        return self.to_y

    @property
    def max_speed(self):
        return self._max_speed



track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
print(len(track1), len(track2))
res_eq = track1 == track2