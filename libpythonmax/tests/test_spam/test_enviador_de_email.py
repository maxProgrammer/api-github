import pytest

from libpythonmax.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['maxwneto.poo@mail.com', 'snetomax@gmail.com']
)
def test_remetent(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'maxwneto@gmail.com',
        'Programador Python',
        'Estou me tornando um programador Profissional.'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'max']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'maxwneto@gmail.com',
            'Programador Python',
            'Estou me tornando um programador Profissional.'
        )
