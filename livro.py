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