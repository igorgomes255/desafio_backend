# Para rodar o docker

`1)` Descomente a linha 88 em _core_/settings.py para o docker encontrar o host

    Exemplo de como deverá ficar

    82  DATABASES = {
    83  "default": {
    84      "ENGINE": "django.db.backends.postgresql",
    85      "NAME": os.getenv("POSTGRES_DATABASE"),
    86      "USER": os.getenv("POSTGRES_USERNAME"),
    87      "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
    88      "HOST": "cnab_desafio",
    89      "PORT": 5432,
    90  }

}

`2)` Mude as configurações em `init.sql`

    Em init.sql mude o nome de usuário, coloque a senha e o banco de dados conforme o que está no .env
    para o docker criar o usuário e o banco de dados a partir do init.sql e depois poder acessar o
    banco de dados pelo .env

    Exemplo no .env

    POSTGRES_USERNAME=meu_usuário
    POSTGRES_PASSWORD=minha_senha
    POSTGRES_DATABASE=meu_bd

    Exemplo no init.sql

    CREATE USER meu_usuário CREATEROLE CREATEDB SUPERUSER PASSWORD 'minha_senha';

    CREATE DATABASE meu_bd;

`3)` Após essas mudanças, rode o comando `docker-compose up` no seu terminal

    Caso tenha feito os passos acima conforme descritos o docker não irá encontrar nenhum erro e rodará normalmente

    Para acessar vá no navegador e digite http://localhost:8000/api/upload/
