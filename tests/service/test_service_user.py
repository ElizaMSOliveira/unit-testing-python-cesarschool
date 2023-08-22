from src.service.service_user import ServiceUser


class TestServiceUser:

    def test_add_user_checked_com_sucesso(self):
        #Setup
        service = ServiceUser()
        resultado_esperado = "Usuário Cadastrado Com Sucesso"
        #Chamada
        resultado = service.add_user_checked("Eliza", "QA")
        #Avaliação
        assert resultado == resultado_esperado

    def test_add_user_checked_com_falha_parametro_none(self):
        #Setup
        servico = ServiceUser()
        resultado_esperado = "Não se cadastra None"
        #Chamada
        resultado = servico.add_user_checked(None, "QA")
        #Avaliação
        assert resultado == resultado_esperado

    def test_add_user_checked_com_falha_parametro_diferente_str(self):
        # Setup
        sevico = ServiceUser()
        resultado_esperado = "Não é uma String"
        # Chamada
        resultado = sevico.add_user_checked(12345, "QA")
        # Avaliação
        assert  resultado == resultado_esperado

    def test_add_user_checked_com_usuario_repetido(self):
        # Setup
        servico = ServiceUser()
        servico.add_user_checked("Eliza", "Engenheira")
        resultado_esperado = "Usuário Já Cadastrado"
        # Chamada
        resultado = servico.add_user_checked("Eliza", "Engenheira")
        # Avaliação
        assert resultado == resultado_esperado

    def test_remove_user_checked_com_sucesso(self):
        #Setup
        servico = ServiceUser()
        servico.add_user_checked("Eliza", "QA")
        resultado_esperado = "O Usuário removido"
        #Chamada
        resultado = servico.remove_user_checked("Eliza")
        #Avaliação
        assert resultado == resultado_esperado

    def test_remove_user_checked_com_falha_parametro_none(self):
        #Setup
        servico = ServiceUser()
        resultado_esperado = "Não se remove Usuário None"
        #Chamada
        resultado = servico.remove_user_checked(None)
        #Avaliação
        assert resultado == resultado_esperado

    def test_remove_user_checked_com_falha_parametro_diferente_str(self):
        #Setup
        servico = ServiceUser()
        resultado_esperado = "Não é uma String"
        #Chamada
        resultado = servico.remove_user_checked(12345)
        #Avaliação
        assert resultado == resultado_esperado

    def test_remove_user_checked_com_falha_inexistente(self):
        #Setup
        servico = ServiceUser()
        resultado = "Usuáio inexistente ou Já Foi Removido"
        #Chamada
        resultado_esperado = servico.remove_user_checked("José")
        #Avaliação
        assert resultado == resultado_esperado

    def test_update_user_checked_com_sucesso(self):
        #Setup
        servico = ServiceUser()
        servico.add_user_checked("Ana", "ADM")
        resultado_esperado = "Usuário Atualizado"
        #Chamada
        resultado = servico.update_user_checked("Ana", "AnaMaria")
        #Avaliação
        assert resultado == resultado_esperado

    def test_update_user_checked_com_falha_parametro_none(self):
        #Setup
        servico = ServiceUser()
        resultado_esperado = "Não Se Atualiza None"
        #Chamada
        resultado = servico.update_user_checked(None, "Ana Maria")
        #Avaliação
        assert resultado == resultado_esperado

    def test_update_user_checked_com_falha_parametro_diferente_str(self):
        #Setup
        servico = ServiceUser()
        resultado_esperado = "Não é uma String"
        #Chamada
        resultado = servico.update_user_checked(12345, "Maurino")
        #Avaliação
        assert resultado == resultado_esperado

    def test_update_user_checked_com_falha_inexistente(self):
        #Setup
        servico = ServiceUser()
        resultado_esperado = "Usuário Não encontrado Para Atualizar"
        #Chamada
        resultado = servico.update_user_checked("Maria", "João")
        #Avaliação
        assert resultado == resultado_esperado

    def test_get_user_by_name_com_sucesso(self):
        #Setup
        servico = ServiceUser()
        servico.add_user_checked("Eliza", "QA")
        resultado_esperado = "Eliza"
        #Chamada
        resultado = servico.get_user_by_name("Eliza")
        #Avaliação
        assert resultado == resultado_esperado

    def test_get_user_by_name_com_falha_parametro_none(self):
        #Setup
        servico = ServiceUser()
        resultado_esperado = "Parametro de Busca None"
        #Chamada
        resultado = servico.get_user_by_name(None)
        #Avaliação
        assert resultado == resultado_esperado

    def test_get_user_by_name_com_falha_parametro_diferente_str(self):
        #Setup
        servico = ServiceUser()
        resultado_esperado = "Parametro de Busca Não é uma String"
        #Chamada
        resultado = servico.get_user_by_name(12345)
        #Avaliação
        assert resultado == resultado_esperado

    def test_get_user_by_name_com_falha_inexistente(self):
        #Setup
        servico = ServiceUser()
        resultado_esperado = "Usuário Não Encontrado"
        #Chamada
        resultado = servico.get_user_by_name("Eliza")
        #Avaliação
        assert resultado == resultado_esperado

