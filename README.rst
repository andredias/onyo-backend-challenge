
Instruções para Desenvolvimento
===============================

.. code:: bash

    $ docker-compose up

O arquivo :code:`docker-compose.yml` já contém a configuração própria para o ambiente de desenvolvimento.
As pastas relativas aos diretórios :code:`cep` e :code:`funcionario` estão
montadas como volumes nos respectivos containers.

Durante o desenvolvimento,
as URLs são:

.. csv-table::
    :header-rows: 1
    :stub-columns: 1

    , CEP, Funcionario
    List, http://localhost:8001/api/v1/ceps/, http://localhost:8002/api/v1/funcionarios/
    Detail, http://localhost:8001/api/v1/ceps/<CEP>/, http://localhost:8002/api/v1/funcionarios/<CPF>/




Instruções para Instalação no Heroku
====================================

.. code:: bash

    $ docker-compose build
    $ heroku container:login
    $ docker push registry.heroku.com/onyo-cep/web
    $ docker push registry.heroku.com/onyo-funcionario/web
    $ heroku container:release web --app onyo-cep
    $ heroku container:release web --app onyo-funcionario

O acesso aos serviços instalados no Heroku é feito pelos links abaixo:


.. csv-table::
    :header-rows: 1
    :stub-columns: 1

    , CEP, Funcionario
    List, http://onyo-cep.herokuapp.com/api/v1/ceps/, http://onyo-funcionario.herokuapp.com/api/v1/funcionarios/
    Detail, http://onyo-cep.herokuapp.com/api/v1/ceps/<CEP>/, http://onyo-funcionario.herokuapp.com/api/v1/funcionarios/<CPF>/
