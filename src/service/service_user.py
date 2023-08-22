from src.modeis.store import Store
from src.modeis.user import User


class ServiceUser:
    #INICIA LOGO O BANCO
    def __init__(self):
        self.store = Store()
    #METODO VERIRICA ANTES DE ADICIONAR USUARIO
    def add_user_checked(self, name, job):
        if name is not None and job is not None:
            if isinstance(name, str) and isinstance(job, str):
                if self.search_user(name):
                    return "Usuário Já Cadastrado"
                else:
                    user = User(name, job)
                    self.store.bd.append(user)
                    return "Usuário Cadastrado Com Sucesso"
            else:
                return "Não é uma String"
        else:
            return "Não se cadastra None"
    def remove_user_checked(self, nome):
        if nome is not None:
            if isinstance(nome, str):
                if self.search_user(nome):
                    achou = self.search_user(nome)
                    self.store.bd.remove(achou)
                    return "O Usuário removido"
                else:
                    return "Usuáio inexistente ou Já Foi Removido"
            else:
                return "Não é uma String"
        else:
            return "Não se remove Usuário None"

    def update_user_checked(self, nome, novonome):
        if nome is not None and novonome is not None:
            if isinstance(nome, str) and isinstance(novonome, str):
                if self.search_user(nome):
                    for int, user in enumerate(self.store.bd):
                        if self.store.bd[int].name == nome:
                         user.name = novonome
                         return "Usuário Atualizado"
                else:
                    return "Usuário Não encontrado Para Atualizar"
            else:
                return "Não é uma String"
        else:
            return "Não Se Atualiza None"
    def get_user_by_name(self, name):
        if name is not None:
            if isinstance(name, str):
                if self.search_user(name):
                   found = self.search_user(name)
                   return found.name
                else:
                    return "Usuário Não Encontrado"
            else:
                return "Parametro de Busca Não é uma String"
        else:
            return "Parametro de Busca None"

    def search_user(self, name):
         for user in self.store.bd:
            if user.name == name:
               return user
         return False

    def list_bank(self):
        for nomes in self.store.bd:
            print("Nome:", nomes.name, "||  Pofissão: ", nomes.job)


