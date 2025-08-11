# M2A Teste Tecnico

## Setup

### 1. Clone o repositório

```bash
$ git clone git@github.com:alantnk/m2a-app.git
$ cd m2a-app
```

### 2. Virtual Environment

Crie e ative um ambiente virtual

**Veja:** [**How to install virtualenv on Linux and Windows**](https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/)

### 3. Variaveis de ambiente

Renomeie arquivo `.env.example` para `.env`

### 4. Instale os pacotes

Execute a instalação

```bash
$ pip install -r requirements.txt
```

### 5. Migrations

Execute as migrations

```bash
$ python3 manage.py migrate
```

### 6. Carregue o Banco de Dados (opcional para testes)

Execute os dados iniciais

```bash
$ python3 manage.py loaddata db.json
```

### 7. Inicie o projeto

Inicie o projeto

```bash
$ python3 manage.py runserver
```

## Acesso

Caso siga o item **6 Carregue o Banco de Dados** os seguintes usuários terão acesso:

1. **username:** admin (acesso django-admin)
2. **username:** jane (acesso básico)

A senha para ambos é **qwerty**.

## Testes (incompleto)

Execute os testes:

```bash
$ pytest
```
