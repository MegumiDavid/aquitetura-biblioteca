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
# Verifica se foi possivel adicionar o livro na biblioteca
livro1_foi_adicionado = biblioteca.livros.adicionar_item(livro1)
if (livro1_foi_adicionado): 
     print(f'Livro {livro1.titulo} adicionado')
else:
     print(f'Nao foi possivel adicionar o livro {livro1.titulo}')

livro2_foi_adicionado = biblioteca.livros.adicionar_item(livro2)
if (livro2_foi_adicionado): 
     print(f'Livro {livro2.titulo} adicionado')
else:
     print(f'Nao foi possivel adicionar o livro {livro2.titulo}')

# Adicionar usuários à biblioteca
biblioteca.adicionar_usuario(usuario1)
biblioteca.adicionar_usuario(usuario2)

# Empréstimo de livro
usuario1.emprestar_livro(livro1)

# Tentativa de empréstimo de livro indisponível
usuario2.emprestar_livro(livro1)

# Devolução de livro
usuario1.devolver_livro(livro1)

# Remoção de livro
biblioteca.remover_livro(livro2)

# Remoção de usuário
biblioteca.remover_usuario(usuario2)

# Busca de livro e usuário
livro_encontrado = biblioteca.buscar_livro("Python para Iniciantes")
usuario_encontrado = biblioteca.buscar_usuario("Alice")

# Exemplo de uso dos métodos de acesso
if livro_encontrado:
    print(livro_encontrado.obter_titulo())
if usuario_encontrado:
    print(usuario_encontrado.obter_nome())