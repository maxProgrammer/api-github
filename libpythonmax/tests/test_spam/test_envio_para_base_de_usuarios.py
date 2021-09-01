from libpythonmax.spam.enviador_de_email import Enviador
from libpythonmax.spam.main import EnviadorDeSpam


def test_envio_de_span(sessao):
    enviador_de_spam= EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'maxwneto.poo@gmail.com',
        'Programador Python',
        'Estou me tornando um programador Profissional.'
    )

