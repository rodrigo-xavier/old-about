# about-me

Passo a passo para executar o projeto no seu computador:

Primeiro instale o pyenv, para obter um ambiente python limpo.

O código a seguir executa o instalador automático do pyenv.

    curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

Em seguida, instale o python versão 3.8.3 utilizando o pacote pyenv, da seguinte forma:

    pyenv install 3.8.3
    pyenv shell 3.8.3

Faça um clone do meu repositório:

    git clone https://github.com/rodrigo-xavier/about-me.git

Agora crie uma virtualenv, ative-a, faça o upgrade do pip e instale os requisitos do projeto:

    python -m venv virtualenv
    source virtualenv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt

E então crie um arquivo chamado .env no diretório principal, com os seguintes dados:

    DEBUG=True
    SECRET_KEY=
    ALLOWED_HOSTS=['localhost', '127.0.0.1', '192.168.0.*']
    INTERNAL_IPS=['localhost', '127.0.0.1', '192.168.0.*']
    ENGINE = 'django.db.backends.sqlite3'
    ADMINS=[('Nome', 'email@email.com')]
    MANAGERS=[('Nome', 'email@email.com')]
    
Entre no seguinte site para gerar sua própria SECRET_KEY e insira-a no .env, no campo designado:

*   https://djecrety.ir/

Agora, antes de rodar o projeto, é necessário gerar as migrations, criar um superusuário:

        python manage.py makemigrations
        python manage.py migrate
        python manage.py createsuperuser

Entre com nome e email desejados, e em seguida designe uma senha.

O site está pronto para ser executado. rode o seguinte comando:

        python manage.py runserver localhost:8000

E em seguida, no seu navegador, abra a página http://localhost:8000/

Eu particularmente, prefiro abrir uma das portas de rede do meu computador para poder acessar o site em outros dispositivos na mesma rede, fazendo o seguinte:

        sudo apt-get install ufw
        sudo ufw allow 8000
       
Descubra o seu endereço ip de alguma forma, e então basta rodar (Assumindo no exemplo que meu ip é 192.168.5.191)

        python manage.py runserver 192.168.5.191:8000

Agora, acessando http:/192.168.5.191:8000/ no navegador de qualquer dispositivo de sua rede, será possivel visualizar o site.


**OBSERVAÇÕES**

*   Para logar no sistema, é necessário acessar http:/192.168.5.191:8000/root/
*   Para editar o perfil, basta estar logado no sistema e acessar a seguinte página http://192.168.0.191:8000/cv/edit/profile
