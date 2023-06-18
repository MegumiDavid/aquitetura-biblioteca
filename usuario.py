class Usuario:
    def __init__(self, nome: str, email: str):
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("O nome deve ser uma string não vazia.")
        if not isinstance(email, str) or email.strip() == "":
            raise ValueError("O email não é válido.")
        
        self._nome = nome
        self._email = email

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def email(self) -> str:
        return self._email