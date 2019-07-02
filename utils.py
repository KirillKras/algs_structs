import sys


class MemorySum:
    def __init__(self):
        self.__sum_memory = 0

    def extend(self, *args):
        for obj in args:
            self.__add(obj)

    def __add(self, obj):
        mem_size = sys.getsizeof(obj)
        self.__sum_memory += mem_size
        if hasattr(obj, '__iter__'):
            if hasattr(obj, 'items'):
                for key, value in obj.items():
                    self.__add(key)
                    self.__add(value)
            elif not isinstance(obj, str):
                for item in obj:
                    self.__add(item)

    def __repr__(self):
        return f'Переменные заняли в сумме {self.__sum_memory} байт'