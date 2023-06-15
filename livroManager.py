class LivroManager:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.obter_titulo()}' adicionado à biblioteca.")

    def remover_livro(self, livro):
        if livro in self.livros:
            self.livros.remove(livro)
            print(f"Livro '{livro.obter_titulo()}' removido da biblioteca.")
        else:
            print(f"Livro '{livro.obter_titulo()}' não está na biblioteca.")

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.obter_titulo() == titulo:
                return livro
        return None