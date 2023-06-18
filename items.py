from typing import TypeVar, Generic, List

T = TypeVar('T')

class Items(Generic[T]):
    def __init__(self):
        self.items: List[T] = []

    # adiciona um item na lista se ele ja nao estiver na lista
    def adicionar_item(self, item) -> None:
        if item in self.items:
            raise Exception('Nao foi possivel inserir o item, pois o item ja foi inserido')
        self.items.append(item)
    
    # remove um item na lista se estiver na lista
    def remover_item(self, item) -> None:
        if item in self.items:
            self.items.remove(item)
        raise Exception('Nao foi possivel remover o item, pois o item nao foi encontrado')

    # busca um item na lista e retorna
    def buscar_item(self, item) -> T or None:
        if item in self.items:
            return item
        return None