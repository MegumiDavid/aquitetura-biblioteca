from typing import TypeVar, Generic, List

T = TypeVar('T')

class Items(Generic[T]):
    def __init__(self):
        self.items: List[T] = []

    def adicionar_item(self, item) -> None:
        if item in self.items:
            raise Exception('Nao foi possivel inserir o item, pois o item ja foi inserido')
        self.items.append(item)
    
    def remover_item(self, item) -> None:
        if item in self.items:
            self.items.remove(item)
        raise Exception('Nao foi possivel remover o item, pois o item nao foi encontrado')

    def buscar_item(self, item) -> T or None:
        if item in self.items:
            return item
        return None