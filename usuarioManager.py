class UsuarioManager:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuário '{usuario.obter_nome()}' adicionado à biblioteca.")

    def remover_usuario(self, usuario):
        if usuario in self.usuarios:
            self.usuarios.remove(usuario)
            print(f"Usuário '{usuario.obter_nome()}' removido da biblioteca.")
        else:
            print(f"Usuário '{usuario.obter_nome()}' não está registrado na biblioteca.")

    def buscar_usuario(self, nome):
        for usuario in self.usuarios:
            if usuario.obter_nome() == nome:
                return usuario
        return None