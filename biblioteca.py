from items import Items
from livro import Livro
from usuario import Usuario

class Biblioteca:   
    def __init__(self):
        self.livros = Items[Livro]()
        self.usuarios = Items[Usuario]()
        self.emprestados = {}

    # verifica se o livro esta emprestado ou nao
    def esta_emprestado(self, livro) -> bool:
        if not livro in self.livros:
            raise Exception('Livro nao foi encontrado')
        return livro in self.emprestados
            
    # empresta o livro salvando em um dict contendo como chave o livro e como valor o usuario
    def emprestar_livro(self, livro: Livro, usuario: Usuario):
        if not livro in self.livros:
            raise Exception('Livro nao foi encontrado')  
        if not usuario in self.usuarios:
            raise Exception('Usuario nao foi encontrado')  
        if self.esta_emprestado(livro):
            raise Exception(f'Livro {livro.titulo} já está emprestado.')
        
        self.emprestados[livro] = usuario
        print(f'Livro {livro.titulo} emprestado para {usuario.nome}.')

    # devolve o livro emprestado apagando assim do dict de livros emprestados
    def devolver_livro(self, livro: Livro, usuario: Usuario):
        if not livro in self.livros:
            raise Exception('Livro nao foi encontrado')  
        if not usuario in self.usuarios:
            raise Exception('Usuario nao foi encontrado')
        if not self.esta_emprestado(livro):
            raise Exception(f'Livro {livro.titulo} não está emprestado.')

        if self.emprestados[livro] != usuario:
            raise Exception(f'O livro {livro.titulo} não foi emprestado para {usuario.nome}.')

        del self.emprestados[livro]
        print(f"Livro '{livro.titulo}' devolvido por {usuario.nome}.")                   