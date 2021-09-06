import pytest as pytest

from libpythonmax.spam.enviador_de_email import Enviador
from libpythonmax.spam.main import EnviadorDeSpam
from libpythonmax.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Max', email='maxwneto.poo@gmail.com'),
            Usuario(nome='Heitor', email='heitorssneto@gmail.com')
        ],
        [
            Usuario(nome='Max', email='maxwneto.poo@gmail.com')

        ]
    ],
)
def test_qde_de_span(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'maxwneto.poo@gmail.com',
        'Programador Python',
        'Estou me tornando um programador Profissional.'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


def test_parametros_de_span(sessao):
    usuario = Usuario(nome='Max', email='maxwneto.poo@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'heitorssneto@gmail.com',
        'Programador Python',
        'Estou me tornando um programador Profissional.'
    )
    assert enviador.parametros_de_envio == (
        'heitorssneto@gmail.com',
        'maxwneto.poo@gmail.com',
        'Programador Python',
        'Estou me tornando um programador Profissional.'
    )
