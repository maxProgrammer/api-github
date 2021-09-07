from unittest.mock import Mock

from libpythonmax import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'maxProgrammer',
        'id': 87916631,
        'avatar_url': 'https://avatars.githubusercontent.com/u/87916631?v=4'
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('maxProgrammer')
    assert 'https://avatars.githubusercontent.com/u/87916631?v=4' == url
