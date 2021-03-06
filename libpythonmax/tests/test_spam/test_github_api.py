from unittest.mock import Mock

import pytest as pytest

from libpythonmax import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/87916631?v=4'
    resp_mock.json.return_value = {
        'login': 'maxProgrammer',
        'id': 87916631,
        'avatar_url': url
    }
    get_mock = mocker.patch('libpythonmax.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('maxProgrammer')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('maxwneto')
    assert 'https://avatars.githubusercontent.com/u/20145347?v=4' == url
