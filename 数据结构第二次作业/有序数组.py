from typing import Any
from collections.abc import Sequence
class OrderedArrayInsert:
    def __init__(self, iterable: Sequence[Any]):
        self.iterable = list(iterable)
    def insert(self, element: Any) -> None:
        insert_index = 0
        current_len = len(self.iterable)
        for index, value in enumerate(self.iterable):
            if element < value:
                insert_index = index
                break
            else:
                insert_index = current_len
        self.iterable.append("")
        for i in range(current_len, insert_index, -1):
            self.iterable[i] = self.iterable[i - 1]
        self.iterable[insert_index] = element
a=[12,21,35,67]
ordered_array = OrderedArrayInsert(a)
ordered_array.insert(56)
print(ordered_array.iterable)
ordered_array.insert(99)
print(ordered_array.iterable)