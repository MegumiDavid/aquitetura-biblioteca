# Exemplo de uso do código:
from livro import Livro
from usuario import Usuario
from biblioteca import Biblioteca

# Criação de alguns livros
livro1 = Livro("Python para Iniciantes", "John Smith", 2018)
livro2 = Livro("Python Avançado", "Jane Doe", 2020)

# Criação de usuários
usuario1 = Usuario("Alice", "alice@example.com")
usuario2 = Usuario("Bob", "bob@example.com")

# Criação da biblioteca
biblioteca = Biblioteca()

# Adicionar livros à biblioteca
biblioteca.livros.adicionar_item(livro1)
biblioteca.livros.adicionar_item(livro2)

# Adicionar usuários à biblioteca
biblioteca.usuarios.adicionar_item(usuario1)
biblioteca.usuarios.adicionar_item(usuario2)

# Empréstimo de livro
biblioteca.emprestar_livro(livro1, usuario1)

# Tentativa de empréstimo de livro indisponível
try:
    biblioteca.emprestar_livro(livro2, usuario2)
except Exception as e:
    print("An exception occurred:", str(e))

# Devolução de livro
biblioteca.devolver_livro(livro1, usuario1)

# Remoção de livro
biblioteca.livros.remover_item(livro2)

# Remoção de usuário
biblioteca.usuarios.remover_item(usuario2)

# Busca de livro e usuário
livro_encontrado = biblioteca.livros.buscar_item(livro1)
usuario_encontrado = biblioteca.usuarios.buscar_item(usuario1)

# Exemplo de uso dos métodos de acesso
if livro_encontrado:
    print(livro_encontrado.titulo)
if usuario_encontrado:
    print(usuario_encontrado.nome)