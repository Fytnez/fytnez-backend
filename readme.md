# Breve Descrição da Proposta:

O objetivo geral do projeto FYTNEZ é ser uma aplicação mobile multiplataforma que possibilite ao usuário gerir suas atividades fitness do dia a dia, seja na sua dieta ou na prática de atividades físicas.


# Informações sobre o projeto "fytnez-backend"

## Primeiros passos:
1. Iniciar a virtual env
```
  $ python -m venv venv
```

2. Ativar venv no windows
```
  $ venv/Scripts/activate
```

3. Instalar dependências do projeto
```
  $ pip install -r requirements.txt
```

4. Atualizar banco de dados com as migrations
```
  $ python manage.py migrate
```

5. Criar super usuário
```
  $ python manage.py createsuperuser
```

6. Rodar o projeto
```
  $ python manage.py runserver
```

## Comandos essenciais:
- Rodar o projeto
```
  $ python manage.py runserver
```
- Criar migration com as novas alterações
```
  $ python manage.py makemigrations --name nome_da_migration
```
- Atualizar banco de dados com as migrations
```
  $ python manage.py migrate
```

# Sobre a equipe
## Integrantes e Cargos:
**P.O.:** Gustavo de Oliveira Guidetti

**Scrum Master:** Santyero Mesquita Borges dos Santos

**Devs:**
- Jonatas da Silva de Oliveira
- Luiz Fernando Brasil
- Felipe Adryan da Hora
- Pedro Henrique Santos Kusiak

## Tecnologias a serem utilizadas:
- Flutter (Dart)
- Django (Python)
- React (Typescript)

## Repositórios:
- [fytnez_mobile](https://github.com/Fytnez/fytnez_mobile)
- [fytnez-backend](https://github.com/Fytnez/fytnez-backend)
- [fytnez-frontend](https://github.com/Fytnez/fytnez-frontend)
