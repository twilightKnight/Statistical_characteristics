from _collections_abc import Iterable
from math import gcd
import numpy as np

ENCODING = 'cp1251'
ALPHABET_SIZE = 256


class StaticalCharacteristic:

    def __init__(self, container, encrypted_container):

        self.container,\
            self.encrypted_container = self.__reform_data(container, encrypted_container)

    def maximum_difference(self):
        return max(self.__abs_list(self.__items_difference()))

    def average_absolute_difference(self):
        return sum(self.__abs_list(self.__items_difference())) / (len(self.container) * len(self.container[0]))

    def normalised_average_absolute_difference(self):
        divider = 0
        for item_list in self.container:
            for item in item_list:
                if isinstance(item, str):
                    divider += self.__char_to_int(item)
                else:
                    divider += abs(int(item))
        return sum(self.__abs_list(self.__items_difference())) / divider

    def average_quadratic_error(self):
        return self.__quadratic_error() / (len(self.container) * len(self.container[0]))

    def normalised_average_quadratic_error(self):
        divider = 0
        for item_list in self.container:
            for item in item_list:
                if isinstance(item, str):
                    item = self.__char_to_int(item)
                divider += int(item) ** 2
        return self.__quadratic_error() / divider

    def __items_difference(self):
        item_difference = []
        for item_list1, item_list2 in zip(self.container, self.encrypted_container):
            for item1, item2 in zip(item_list1, item_list2):
                if isinstance(item1, str) and isinstance(item2, str):
                    item1 = self.__char_to_int(item1)
                    item2 = self.__char_to_int(item2)
                item_difference.append(int(item1) - int(item2))
        return item_difference

    def __quadratic_error(self):
        sum_ = 0
        for item in self.__items_difference():
            if isinstance(item, str):
                item = self.__char_to_int(item)
            sum_ += int(item) ** 2
        return sum_

    @staticmethod
    def __reform_data(data1, data2):
        if type(data1) != type(data2):
            raise TypeError("Input must be the same type")
        elif isinstance(data1, str) and isinstance(data2, str):
            str_len = gcd(len(data1), len(data2))
            reformed_data1 = [data1[x:x + str_len] for x in range(0, len(data1), str_len)]
            reformed_data2 = [data2[x:x + str_len] for x in range(0, len(data2), str_len)]
        elif isinstance([y for y in [x for x in data1]], Iterable) and isinstance([y for y in
                                                                                   [x for x in data2]], Iterable):
            reformed_data1 = np.array(data1).transpose(2, 0, 1).reshape(3, -1)
            reformed_data2 = np.array(data2).transpose(2, 0, 1).reshape(3, -1)
        elif isinstance([x for x in data1], Iterable) and isinstance([x for x in data2], Iterable):
            reformed_data1, reformed_data2 = data1, data2
        else:
            raise ValueError("Items must strings or Iterable[Iterable]")

        if type(reformed_data1) == np.ndarray and type(reformed_data2) == np.ndarray:
            reformed_data1 = reformed_data1.tolist()
            reformed_data2 = reformed_data2.tolist()
        return reformed_data1, reformed_data2

    @staticmethod
    def __abs_list(list_):
        return [abs(element) for element in list_]

    @staticmethod
    def __char_to_int(char):
        return int.from_bytes(char.encode(ENCODING), byteorder='big')
