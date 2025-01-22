# GUARDIAN TESTE
Aplicação para o teste da empresa guardian gestora.

## COMEÇANDO
### Pré requisitos
Segue abaixo a lista dos frameworks e técnologias que são pré requisitos para essa aplicação funcionar
- [Django Framework](https://www.djangoproject.com/download/)
- [Django Rest Framework (DRF)](https://www.django-rest-framework.org/#installation)
- [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/readme.html)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

### Instalando
Para instalar as dependências é simples, primeiro crie um âmbiente virtual de sua preferência, neste exemplo usarei Venv do python mesmo:
```
python -m venv Venv
```
Logo após clone o repósitório do projeto dentro da pasta raiz onde está o Venv:
```
git clone https://github.com/JuanTrindade/GuardianTeste/
```
Agora é simples, instale os pacotes necessários apenas utilizando o script abaixo:
```
pip install requirements.txt
```
E para uma última instalação possivelmente o Django irá reclamar do pacote ``psycopg2`` apenas rode:
```
pip install psycopg2-binary
```
E pronto, agora o projeto está quase pronto pra ser inicializado!

## CONFIGURANDO A BASE DE DADOS
A base de dados utilizada nestá aplicação é um ``PostgreSQL`` pressupondo que você já tera o mesmo instalado na máquina, apenas acesse o shell do postgre e rode:
```
CREATE DATABASE my_db;
```
Agora crie um ``.env`` na pasta raiz da aplicação com as seguintes váriaveis:
```js
DB_NAME=name
DB_USER=user
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
```
Agora a base de dados está configurada!

## Inicie o Projeto
Depois de toda aplicação configurada apenas rode na pasta raiz:
```
python manage.py runserver
```
Para ter acesso aos endpoints documentados pelo swagger acesse ``http://127.0.0.1:8000/swagger/``

## CRIADO COM:
- [Python 3.13](https://www.python.org/downloads/)
- [Django Framework](https://www.djangoproject.com/download/)
- [Django Rest Framework (DRF)](https://www.django-rest-framework.org/#installation)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Swagger](https://drf-yasg.readthedocs.io/en/stable/readme.html)

## Authors
- Juan Trindade 🖥️
