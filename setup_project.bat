@echo off
REM Passo 1: Iniciar a virtual env
python -m venv venv

REM Passo 2: Ativar venv no Windows
call venv\Scripts\activate

REM Passo 3: Instalar dependências do projeto
pip install -r requirements.txt

REM Passo 4: Atualizar banco de dados com as migrations
python manage.py migrate

REM Passo 5: Criar super usuário
python manage.py createsuperuser

REM Finalizar venv no Windows
deactivate
