<br>
<h1 id="cnab"><b>1. Parsear arquivos CNAB</b></h1>
<br>

## Essa aplicação consiste em parsear arquivos de texto CNAB para mandar para o banco de dados

`Exemplo de como é parseado um texto CNAB`

    Arquivo de texto recebido: 3201903010000014200096206760174753****3153153453JOÃO MACEDO   BAR DO JOÃO

    Depois de ser parseado ele irá mandar para o banco de dados assim:

    {
    	"type": 3,
    	"date": "2019-03-01",
    	"value": "142.00",
    	"cpf": "09620676017",
    	"card": "4753****3153",
    	"hour": "15:34:53",
    	"owner_shop": "JOÃO MACEDO",
    	"name_shop": "BAR DO JOÃO"
    },

---

<br>
<h1 id="initialization"><b>2. Inicialização do projeto localmente</b></h1>
<br>

Primeiramente deve assegurar-se de que tem a [última versão do python](https://www.python.org/downloads/) instalada em sua máquina, além do [PostgreSQL](https://www.postgresql.org/) se optar por rodar as migrações da API para o database localmente.

Após estas instalações, cheque se o _`pip3`_, o _`python3`_ e o _`postgres`_ foram instalados corretamente:

```powershell
python3 --version   # Python 3.11.0

pip3 --version      # pip 22.3.1 from C:\Python311\[...]\pip

psql --version      # psql (PostgreSQL) 14.5
```

Atualize seu _`pip`_ para evitar possíveis erros durante as instalações de pacotes:

```powershell
# Windows
python.exe -m pip install --upgrade pip

# Linux
sudo -H pip3 install --upgrade pip

# MacOS
pip3 install --upgrade pip
```

Como toda aplicação desenvolvida em Python, será necessário iniciar um ambiente virtual para concentrar todas as instalações de extensões dentro do diretório do projeto. Para isso, vamos criar esse ambiente virtual através do seguinte comando:

```powershell
python -m venv venv
```

Agora, ative seu ambiente virtual:

```powershell
# Linux & MacOS
.\venv\bin\activate

# Windows
.\venv\Scripts\activate
```

Vamos instalar as dependências necessárias para o bom funcionamento da API de modo geral. Para isso, já dentro do ambiente virtual, utilize o comando abaixo para instalar estas dependências:

```powershell
pip install -r requirements.txt
```

`Arquivo .env`

Esse projeto foi feito para rodar pelo postgres, e por isso é necessário ter um arquivo .env na raiz do projeto para colocar as informações pessoais do seu postgres

```
Exemplo:

SECRET_KEY=informe_sua_secret_key

POSTGRES_DATABASE=informe_o_banco_de_dados
POSTGRES_USERNAME=informe_seu_usuario_postgres
POSTGRES_PASSWORD=informe_sua_senha_postgres

```

Com todos estes passos encaminhados, você agora precisa executar as migrations, para que todas estas presentes nos apps da API possam constar no database:

```powershell
python manage.py migrate
```

Como último passo, rode o servidor local:

```bash
python .\manage.py runserver

# Se tudo estiver ok, você verá algo semelhante a isso aparecer em seu terminal:
Performing system checks...

System check identified no issues (0 silenced).
January 05, 2023 - 22:20:06
Django version 4.1.5, using settings '_core_.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Pronto! Temos nosso servidor 100% funcional rodando localmente!

<br>

---

<br>
<h1 id="docker"><b>3. Sobre a aplicação</b></h1>
<br>

## \*\* IMPORTANTE

    Essa aplicação contém templates, então ela exclusivamente foi feita para rodar no navegador.

Essa aplicação é composta por três rotas

`1) http://localhost:8000/api/upload/`

    Responsável por receber o arquivo .txt, o arquivo é salvo no banco de dados afim de poder manipular os dados
    Para enviar o arquivo, escolha o arquivo .txt e clique em upload

`2) http://localhost:8000/api/transactions/`

    Essa rota é responsável por parsear o arquivo .txt recebido e mandar as informações para o banco de dados
    Para parsear clique no botão enviar APÓS enviar o arquivo

`3) http://localhost:8000/api/cnab/`

    Essa rota é responsável por mostrar o totalizador do saldo em conta de cada loja

<br>
<h1 id="docker"><b>4. Docker</b></h1>
<br>

**_OPCIONAL_**: Essa aplicação também pode ser rodada no docker, porém deixei apenas como um opcional

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
