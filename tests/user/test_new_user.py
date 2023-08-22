from src.service.service_user import ServiceUser


class TestNewUser:
    service = ServiceUser()

    def test_add_user_success(self):
        xpected_result = "Usuário Cadastrado"
        result = self.service.add_user_checked(name="liza", job="QA")
        assert result == xpected_result

    def test_add_user_already_exist(self):
        pass
