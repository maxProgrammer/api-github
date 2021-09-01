from libpythonmax.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Max')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Max'), Usuario(nome='Heitor')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
