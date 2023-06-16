class Livro:
    def __init__(self, titulo: str, autor: str, ano_publicacao: int):
        if not isinstance(titulo, str) or titulo.strip():
            raise ValueError("O título do livro deve ser uma string não vazia.")
        if not isinstance(autor, str) or autor.strip():
            raise ValueError("O autor do livro deve ser uma string não vazia.")
        if not isinstance(ano_publicacao, int) or ano_publicacao <= 0:
            raise ValueError("O ano de publicação do livro deve ser um inteiro positivo.")
        
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

    @property
    def titulo(self) -> str:
        return self._titulo

    @property
    def autor(self) -> str:
        return self._autor

    @property
    def ano_publicacao(self) -> int:
        return self._ano_publicacao
    

class Usuario:
    def __init__(self, nome: str, email: str):
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("O nome deve ser uma string não vazia.")
        if not isinstance(email, str) or nome.strip() == "":
            raise ValueError("O email não é válido.")
        
        self._nome = nome
        self._email = email
        self._livros_emprestados = []

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def email(self) -> str:
        return self._email
    

from typing import TypeVar, Generic, List

T = TypeVar('T')

class Items(Generic[T]):
    def __init__(self):
        self.items: List[T] = []

    def adicionar_item(self, item) -> bool:
        if item in self.items:
            return False
        self.items.append(item)
        return True
    
    def remover_item(self, item) -> bool:
        for item in self.items:
            self.items.remove(item)
            return True
        return False

    def buscar_item(self, item) -> T or None:
        for item in self.items:
            return item
        return None
    

from ast import List
from items import Items
from livro import Livro
from usuario import Usuario

class Biblioteca:
    def __init__(self):
        self.livros = Items[Livro]()
        self.usuarios = Items[Usuario]()
        self.emprestados = {}

    def esta_emprestado(self, livro) -> bool:
        return livro in self.emprestados
            
    def emprestar_livro(self, livro: Livro, usuario: Usuario):      
        if self.esta_emprestado(livro):
            raise Exception(f'Livro {livro.titulo} já está emprestado.')
        
        self.emprestados[livro] = usuario
        print(f'Livro {livro.titulo} emprestado para {usuario.nome}.')

    def devolver_livro(self, livro: Livro, usuario: Usuario):
        if not self.esta_emprestado(livro):
            raise Exception(f'Livro {livro.titulo} não está emprestado.')

        if self.emprestados[livro] != usuario:
            raise Exception(f'O livro {livro.titulo} não foi emprestado para {usuario.nome}.')

        del self.emprestados[livro]
        print(f"Livro '{livro.titulo}' devolvido por {usuario.nome}.")        
        
    def listar_livros_emprestados_por_usuario(self, usuario: Usuario) -> List[Livro]:
        livros_emprestados = []
        for livro, user in self.emprestados.items():
            if user == usuario:
                livros_emprestados.append(livro)
        return livros_emprestados
            