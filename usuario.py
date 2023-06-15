# pip install validate_email
# from validate_email_address import validate_email
# validate_email(email)

import re

class Usuario:
    def __init__(self, nome: str, email: str):
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("O nome deve ser uma string não vazia.")
        if not isinstance(email, str) or not self._validar_email(email):
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

    def _validar_email(self, email) -> bool:
        if email.strip() == "":
            return False
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
          return True
        else:
          return False
