

Instruções para Instalação no Heroku
====================================

CEP
---

.. code:: bash

    $ docker-compose build
    $ heroku container:login
    $ docker push registry.heroku.com/onyo-cep/web
    $ docker push registry.heroku.com/onyo-funcionario/web
    $ heroku container:release web --app onyo-cep
    $ heroku container:release web --app onyo-funcionario
