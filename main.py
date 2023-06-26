import types

class FlatIterator:

    def __init__(self, list_of_lists_1):
        self.list_of_lists_1 = list_of_lists_1

    def __iter__(self):
        self.iter = iter(self.list_of_lists_1)
        self.result = []
        self.count = -1
        return self

    def __next__(self):
        self.count += 1
        if len(self.result) == self.count:
            self.result = None
            self.count = 0
            while not self.result:
                self.result = next(self.iter)
        return self.result[self.count]

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()


def flat_generator(list_of_lists):
    for list_i in list_of_lists:
        for list_j in list_i:
            yield list_j


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
