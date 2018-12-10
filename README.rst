

Instruções para Instalação no Heroku
====================================

CEP
---

.. code:: bash

    $ docker-compose build cep
    $ heroku container:login
    $ docker push docker push registry.heroku.com/onyo-cep/web
    $ heroku container:release web --app onyo-cep
