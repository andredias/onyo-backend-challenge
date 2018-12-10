import pytest
from django.urls import reverse
from .models import Funcionario
from django.contrib.auth.models import User

pytestmark = pytest.mark.django_db


@pytest.fixture
def populate_db():
    User.objects.create_user('beltrano', 'beltrano@gmail.com', '1234')
    Funcionario.objects.create(
        cpf='12345678901',
        nome='Beltrano',
        cep='13175667',
        logradouro='Avenida Ipê Amarelo',
        numero='100',
        complemento='casa 10',
        bairro='Parque Villa Flores', localidade='Sumaré', uf='SP'
    )
    Funcionario.objects.create(
        cpf='11223344556',
        nome='Sicrano de Tal',
        cep='04180112',
        logradouro='Travessa 19 de Agosto',
        numero='108',
        bairro='Jardim Maria Estela', localidade='São Paulo', uf='SP'
    )
    Funcionario.objects.create(
        cpf='22334455667',
        nome='Fulano',
        cep='03047000',
        logradouro='Rua 21 de Abril',
        numero='21',
        bairro='Brás', localidade='São Paulo', uf='SP'
    )


def test_empty_funcionarios(apiclient):
    response = apiclient.get(reverse('funcionario-list'))
    assert response.status_code == 200
    assert len(response.json()) == 0


def test_funcionarios_get(apiclient, populate_db):
    response = apiclient.get(reverse('funcionario-list'))
    assert response.status_code == 200
    json = response.json()
    assert len(json) == 3
    assert json[0]['nome'] == 'Beltrano'


def test_funcionarios_post_unauthenticated(apiclient, populate_db):
    response = apiclient.post(reverse('funcionario-list'), {
        'cpf': '10987654321',
        'nome': 'Joca',
        'cep': '29060480',
        'numero': '100',
    })
    assert response.status_code == 403


def test_funcionarios_post_authenticated(apiclient, populate_db):
    apiclient.login(username='beltrano', password='1234')
    response = apiclient.post(reverse('funcionario-list'), {
        'cpf': '10987654321',
        'nome': 'Joca',
        'cep': '29060480',
        'numero': '100',
    })
    assert response.status_code == 201
    json = response.json()
    assert json['logradouro'] == 'Rua Marquês de Olinda'


def test_funcionarios_post_duplicated_funcionario(apiclient, populate_db):
    apiclient.login(username='beltrano', password='1234')
    response = apiclient.post(reverse('funcionario-list'), dict(
        cpf='12345678901',
        nome='Beltrano',
        cep='13175667',
        numero='100',
    ))
    assert response.status_code == 400


def test_funcionarios_detail_get(apiclient, populate_db):
    response = apiclient.get(reverse('funcionario-detail', args=['12345678901']))
    assert response.status_code == 200
    assert len(response.json()) == 10


def test_funcionarios_detail_get_inexistent_funcionario(apiclient, populate_db):
    response = apiclient.get(reverse('funcionario-detail', args=['12345678']))
    assert response.status_code == 404


def test_funcionarios_detail_patch_unauthenticated(apiclient, populate_db):
    response = apiclient.patch(reverse('funcionario-detail', args=['12345678901']), {
        'cep': '29060480', 'numero': '99', 'complemento': ''})
    assert response.status_code == 403


def test_funcionarios_detail_patch_authenticated(apiclient, populate_db):
    apiclient.login(username='beltrano', password='1234')
    response = apiclient.patch(reverse('funcionario-detail', args=['12345678901']), {
        'cep': '29060480', 'numero': '99', 'complemento': ''})
    assert response.status_code == 200
    json = response.json()
    assert json['bairro'] == 'Jardim da Penha'
    assert len(json) == 10


def test_funcionarios_detail_patch_authenticated_nonexistent_cep(apiclient, populate_db):
    apiclient.login(username='beltrano', password='1234')
    response = apiclient.patch(reverse('funcionario-detail', args=['12345678901']), {
        'cep': '99999999', 'numero': '99', 'complemento': ''})
    assert response.status_code == 400
    assert b'{"detail":"CEP: N\xc3\xa3o encontrado."}' in response.content


def test_funcionarios_detail_delete(apiclient, populate_db):
    apiclient.login(username='beltrano', password='1234')
    response = apiclient.delete(reverse('funcionario-detail', args=['12345678901']))
    assert response.status_code == 204


def test_api_root(apiclient):
    response = apiclient.get(reverse('api-root'))
    assert response.status_code == 200


def test_funcionario_str(populate_db):
    funcionario = Funcionario.objects.get(pk='12345678901')
    assert 'Beltrano' in str(funcionario)
