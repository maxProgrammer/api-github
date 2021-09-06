from libpythonmax.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Max', email='maxwneto.poo@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Max', email='maxwneto.poo@gmail.com'),
                Usuario(nome='Heitor', email='heitorssneto@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
