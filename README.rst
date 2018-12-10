====================
Desafio Técnico Onyo
====================

Este projeto é a implementação do desafio técnico proposto pela Onyo
como parte do seu processo de contratação.
O objetivo do desafio é criar dois microsserviços integrados,
que disponibilizam informações através de uma REST API.

Conforme sugerido na `especificação fornecida <especificacao.md>`_,
um microsserviço oferece consulta de CEPs, e o outro serviço de cadastro de funcionários
que usa o microsserviço de CEP para consultar endereços no cadastro de novos funcionários.


REST API
========

A API de cada sistema está documentado através do Swagger a partir dos seguintes links:

* http://onyo-cep.herokuapp.com/
* http://onyo-funcionario.herokuapp.com/

.. attention::

    Algumas operações só são disponibilizadas a usuários autenticados.
    Para visualizar todas as operações,
    faça o login no sistema de :code:`cep` use :code:`fulano:1234`.
    No sistema de :code:`funcionario`, use :code:`beltrano:1234`.


Exemplos de Uso
===============

Os exemplos abaixo são baseados no projeto `HTTPie <https://httpie.org>`_


Obter Lista de CEPs
-------------------

.. code:: bash

    $ http GET http://onyo-cep.herokuapp.com/api/v1/ceps/
    HTTP/1.1 200 OK
    Allow: GET, POST, HEAD, OPTIONS
    Cache-Control: max-age=600
    Connection: keep-alive
    Content-Length: 541
    Content-Type: application/json
    Date: Mon, 10 Dec 2018 16:57:58 GMT
    Expires: Mon, 10 Dec 2018 17:07:58 GMT
    Server: gunicorn/19.9.0
    Vary: Accept, Cookie
    Via: 1.1 vegur
    X-Frame-Options: SAMEORIGIN

    [
        {
            "bairro": "Jardim Maria Estela",
            "cep": "04180112",
            "localidade": "São Paulo",
            "logradouro": "Travessa 19 de Agosto",
            "uf": "SP",
            "url": "http://onyo-cep.herokuapp.com/api/v1/ceps/04180112/"
        },
        {
            "bairro": "Parque Villa Flores",
            "cep": "13175667",
            "localidade": "Sumaré",
            "logradouro": "Avenida Ipê Amarelo",
            "uf": "SP",
            "url": "http://onyo-cep.herokuapp.com/api/v1/ceps/13175667/"
        },
        {
            "bairro": "Jardim da Penha",
            "cep": "29060480",
            "localidade": "Vitória",
            "logradouro": "Rua Marquês de Olinda",
            "uf": "ES",
            "url": "http://onyo-cep.herokuapp.com/api/v1/ceps/29060480/"
        }
    ]


Cadastrar Novo CEP
------------------

Atenção: o cadastro e alterações em registros são operações permitidas apenas a usuários autenticados.
O projeto já tem um usuário autenticado cujo username e senha são :code:`fulano:1234`.

.. code:: bash

    $ http -a fulano:1234 POST http://onyo-cep.herokuapp.com/api/v1/ceps/ \
         cep=03047000 \
         logradouro="Rua 21 de Abril" \
         bairro=Brás \
         localidade="São Paulo" \
         uf=SP

    HTTP/1.1 201 Created
    Allow: GET, POST, HEAD, OPTIONS
    Connection: keep-alive
    Content-Length: 162
    Content-Type: application/json
    Date: Mon, 10 Dec 2018 17:05:26 GMT
    Location: http://onyo-cep.herokuapp.com/api/v1/ceps/03047000/
    Server: gunicorn/19.9.0
    Vary: Accept, Cookie
    Via: 1.1 vegur
    X-Frame-Options: SAMEORIGIN

    {
        "bairro": "Brás",
        "cep": "03047000",
        "localidade": "São Paulo",
        "logradouro": "Rua 21 de Abril",
        "uf": "SP",
        "url": "http://onyo-cep.herokuapp.com/api/v1/ceps/03047000/"
    }


Obter Registro de um CEP
------------------------

.. code:: bash

    $ http GET http://onyo-cep.herokuapp.com/api/v1/ceps/29060480/
    HTTP/1.1 200 OK
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    Cache-Control: max-age=600
    Connection: keep-alive
    Content-Length: 177
    Content-Type: application/json
    Date: Mon, 10 Dec 2018 17:09:31 GMT
    Expires: Mon, 10 Dec 2018 17:19:31 GMT
    Server: gunicorn/19.9.0
    Vary: Accept, Cookie
    Via: 1.1 vegur
    X-Frame-Options: SAMEORIGIN

    {
        "bairro": "Jardim da Penha",
        "cep": "29060480",
        "localidade": "Vitória",
        "logradouro": "Rua Marquês de Olinda",
        "uf": "ES",
        "url": "http://onyo-cep.herokuapp.com/api/v1/ceps/29060480/"
    }


Obter Lista de Funcionários
---------------------------

.. code:: bash

    $ http GET http://onyo-funcionario.herokuapp.com/api/v1/funcionarios/
    HTTP/1.1 200 OK
    Allow: GET, POST, HEAD, OPTIONS
    Cache-Control: max-age=600
    Connection: keep-alive
    Content-Length: 807
    Content-Type: application/json
    Date: Mon, 10 Dec 2018 17:11:30 GMT
    Expires: Mon, 10 Dec 2018 17:21:30 GMT
    Server: gunicorn/19.9.0
    Vary: Accept, Cookie
    Via: 1.1 vegur
    X-Frame-Options: SAMEORIGIN

    [
        {
            "bairro": "Parque Villa Flores",
            "cep": "13175667",
            "complemento": "casa 10",
            "cpf": "12345678901",
            "localidade": "Sumaré",
            "logradouro": "Avenida Ipê Amarelo",
            "nome": "Beltrano",
            "numero": "100",
            "uf": "SP",
            "url": "http://onyo-funcionario.herokuapp.com/api/v1/funcionarios/12345678901/"
        },
        {
            "bairro": "Brás",
            "cep": "03047000",
            "complemento": null,
            "cpf": "22334455667",
            "localidade": "São Paulo",
            "logradouro": "Rua 21 de Abril",
            "nome": "Fulano",
            "numero": "21",
            "uf": "SP",
            "url": "http://onyo-funcionario.herokuapp.com/api/v1/funcionarios/22334455667/"
        },
        {
            "bairro": "Jardim Maria Estela",
            "cep": "04180112",
            "complemento": null,
            "cpf": "11223344556",
            "localidade": "São Paulo",
            "logradouro": "Travessa 19 de Agosto",
            "nome": "Sicrano de Tal",
            "numero": "108",
            "uf": "SP",
            "url": "http://onyo-funcionario.herokuapp.com/api/v1/funcionarios/11223344556/"
        }
    ]


Cadastro de Funcionário
-----------------------

Operações de alterações de registro só são permitidas para usuários autenticados.
O sistema já possui um usuário autenticado: :code:`beltrano:1234`.

.. code:: bash

    $ http -a beltrano:1234 POST http://onyo-funcionario.herokuapp.com/api/v1/funcionarios/ \
        cpf=12121212121 \
        nome="Bozo" \
        cep="03047000" \
        numero="1964" \
        complemento="i666"

    HTTP/1.1 201 Created
    Allow: GET, POST, HEAD, OPTIONS
    Connection: keep-alive
    Content-Length: 252
    Content-Type: application/json
    Date: Mon, 10 Dec 2018 17:15:21 GMT
    Location: http://onyo-funcionario.herokuapp.com/api/v1/funcionarios/12121212121/
    Server: gunicorn/19.9.0
    Vary: Accept, Cookie
    Via: 1.1 vegur
    X-Frame-Options: SAMEORIGIN

    {
        "bairro": "Brás",
        "cep": "03047000",
        "complemento": "i666",
        "cpf": "12121212121",
        "localidade": "São Paulo",
        "logradouro": "Rua 21 de Abril",
        "nome": "Bozo",
        "numero": "1964",
        "uf": "SP",
        "url": "http://onyo-funcionario.herokuapp.com/api/v1/funcionarios/12121212121/"
    }



Obter Registro de Funcionário
-----------------------------

.. code:: bash

    $ http GET http://onyo-funcionario.herokuapp.com/api/v1/funcionarios/22334455667/
    HTTP/1.1 200 OK
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    Cache-Control: max-age=600
    Connection: keep-alive
    Content-Length: 250
    Content-Type: application/json
    Date: Mon, 10 Dec 2018 17:19:43 GMT
    Expires: Mon, 10 Dec 2018 17:29:43 GMT
    Server: gunicorn/19.9.0
    Vary: Accept, Cookie
    Via: 1.1 vegur
    X-Frame-Options: SAMEORIGIN

    {
        "bairro": "Brás",
        "cep": "03047000",
        "complemento": null,
        "cpf": "22334455667",
        "localidade": "São Paulo",
        "logradouro": "Rua 21 de Abril",
        "nome": "Fulano",
        "numero": "21",
        "uf": "SP",
        "url": "http://onyo-funcionario.herokuapp.com/api/v1/funcionarios/22334455667/"
    }



Instruções para Desenvolvimento
===============================

As instruções para instalar, rodar e testar estão disponíveis no arquivo `Makefile <Makefile>`_:

.. include:: Makefile
    :code: make


Alternativamente,
você pode usar apenas os containers do Docker:


.. code:: bash

    $ docker-compose up

Como os diretórios dos projetos :code:`cep` e :code:`funcionario`
estão mapeados diretamente dentro dos containers,
alterações locais nos projetos forçam o reinício dos serviços nos containers.

.. tip::

    Veja `docker-compose.yml <docker-compose.yml>`_ para mais detalhes.



Instruções para Instalação no Heroku
====================================

.. code:: bash

    $ docker-compose build
    $ heroku container:login
    $ docker push registry.heroku.com/onyo-cep/web
    $ docker push registry.heroku.com/onyo-funcionario/web
    $ heroku container:release web --app onyo-cep
    $ heroku container:release web --app onyo-funcionario
