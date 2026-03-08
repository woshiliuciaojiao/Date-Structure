from typing import Any,Iterable
class DeleteItem:
    def __init__(self,iterable:Iterable[Any]):
        self.iterable = list(iterable)
    def delete(self,index_to_delete:int)->list[Any]:
        length_of_iterable:int=len(self.iterable)
        for i in range(index_to_delete,length_of_iterable-1):
            self.iterable[i]=self.iterable[i+1]
        self.iterable.pop()
        return self.iterable
fruits:list[str]=["apple","banana","cherry","orange","mango"]
Delete_item=DeleteItem(fruits)
print(Delete_item.delete(3))
print(Delete_item.delete(1))
print(Delete_item.delete(2))




