from unittest.mock import Mock

import pytest as pytest

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
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'maxwneto.poo@gmail.com',
        'Programador Python',
        'Estou me tornando um programador Profissional.'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_span(sessao):
    usuario = Usuario(nome='Max', email='maxwneto.poo@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'heitorssneto@gmail.com',
        'Programador Python',
        'Estou me tornando um programador Profissional.'
    )
    enviador.enviar.asset_called_once_with(
        'heitorssneto@gmail.com',
        'maxwneto.poo@gmail.com',
        'Programador Python',
        'Estou me tornando um programador Profissional.'
    )
