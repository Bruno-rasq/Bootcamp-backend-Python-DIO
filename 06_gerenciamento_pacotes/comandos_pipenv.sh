pip install pipenv // instalar o pipenv

python -m venv .env
source .env/bin/activate // ativa o ambiente
deactivate // desativa o ambiente

pipenv install nome_pacote // instalar um pacote
pipenv uninstall nome_pacote // desistala um pacote
pipenv lock

pipenv graph // mostra o grafo do pacote