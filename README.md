# libpythonmax
Módulo para exemplificar construção de projetosd Python no curso PyTools

Nesse curso é ensinado como contribuir com projetos de código aberto

Perfil Gitbub: [maxProgrammer](https://github.com/maxProgrammer)

Suportada versão 3 de Python 

Tópicos a serem abordados:
1. Git
2. Pyenv
sudo pacman -S pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
exec "$SHELL"
pyenv install 3.9.6
pyenv install 2.7.18
pyenv global 3.9.6
pyenv which python


2. Virtualenv
python3 -m venv .venv
source .venv/bin/activate
which python
python -v
deactivate


3. PIP
pip install --upgrade pip
pip install requests
pip freeze > requirements.txt
4. pip install -r requirements.txt
