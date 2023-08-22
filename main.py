from src.modeis.store import Store
from src.modeis.user import User
from src.service.service_user import ServiceUser
"""
#CRIANDO UM USUARIOS COMUM DIRETO DA PAG USER
user = User("Eliza", "Design")
print("Endereço na memoria: " ,user)
print("Nome: ", user.name)
print("Profissão: ", user.job)
user_2 = User("Maria", "Tec. Infermagem")
print("Endereço na memoria: " ,user_2)
print("Nome: ", user_2.name)
print("Profissão: ", user_2.job)
#CCRIANDO O BANCO DIRETO DA PAG STORE
banco = Store()
banco.bd.append(user)
banco.bd.append(user_2)
print(banco)
"""
#CRIANDO UM SERVIÇO ONDE ELE SE ENCARREGA DE CHAMAR O USER E STORE(BANCO)

service = ServiceUser()
"""
result = service.add_user("Eliza ", "Design")
print("O que me retorna o metodo: ",result)
result = service.add_user("Maria","QA")
print("O que me retorna o metodo: ",result)
print("Imprimindo o Banco pos[0]: Nome: ",service.store.bd[0].name, "Profissão: ", service.store.bd[0].job)
print("Imprimindo o Banco pos[1]: Nome: ",service.store.bd[1].name, "Profissão: ", service.store.bd[1].job)
"""
print("$$$$$$$$$CADASTRO$$$$$$$$$$$")
verificar = service.add_user_checked("Eliza", "QA")
print(verificar)
verificar = service.add_user_checked("Maria", "QA")
print(verificar)
print("$$$$$$$$$ CADASTRO REPETIDO $$$$$$$$$$$")
verificar = service.add_user_checked("Eliza", "QA")
print(verificar)
print("$$$$$$$$$ PESQUISA $$$$$$$$$$$")
pesq = service.search_user("Eliza")
print(pesq)
print("$$$$$$$$$ LISTA $$$$$$$$$$$")
lista = service.list_bank()
print("$$$$$$$$$C DELETAR $$$$$$$$$$$")
delelar = service.remove_user_checked("El")
print(delelar)
print("$$$$$$$$$ LISTA $$$$$$$$$$$")
lista2 = service.list_bank()
print("$$$$$$$$$ DELETAR SEM EXISTIR $$$$$$$$$$$")
delelar2 = service.remove_user_checked("iza")
print(delelar2)
print("$$$$$$$$$ LISTA $$$$$$$$$$$")
lista4 = service.list_bank()
print("$$$$$$$$$ ATUALIZANDO $$$$$$$$$$$")
atualizar = service.update_user_checked(123, "Santos")
print(atualizar)
atualizar2 = service.update_user_checked("Eliza", "Oliveira")
print(atualizar2)
print("$$$$$$$$$ LISTA $$$$$$$$$$$")
lista3 = service.list_bank()
print("$$$$$$$$$ Buscar $$$$$$$$$$$")
found = service.get_user_by_name("Santos")
print(found)




