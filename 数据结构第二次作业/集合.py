from collections.abc import Sequence
from typing import Any

class CustomSet:
    def __init__(self, iterable: Sequence[Any]):
        self.iterable = list(iterable)

    def insert_last(self, element: Any) -> bool:
       for index, item in enumerate(self.iterable):
           if item==element:
               return False
       self.iterable.append(element)
       return True

    def contains(self, element: Any) -> bool:
        return element in self.iterable

    def remove(self, element: Any) -> bool:
        if element not in self.iterable:
            return False
        self.iterable.remove(element)
        return True
fruits=['apple','banana','mango']
set_insert=CustomSet(fruits)
print(set_insert.insert_last('cherry'))
print(set_insert.iterable)
print(set_insert.remove('cherry'))
print(set_insert.iterable)
print(set_insert.contains('cherry'))
