class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.list = iter(self.list_of_list)
        self.iter_items = [iter([])]
        return self

    def __next__(self):
        try:
            if self.iter_items:
                iter_item = self.iter_items[-1]
            else:
                iter_item = self.list

            item = next(iter_item)
            if type(item) == list:
                self.iter_items.append(iter(item))
                item = self.__next__()

        except StopIteration:
            if self.iter_items:
                self.iter_items.pop()
                return self.__next__()
            else:
                raise StopIteration

        return item


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
