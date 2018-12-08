import pytest
from django.urls import reverse
from .models import CEP
from django.contrib.auth.models import User

pytestmark = pytest.mark.django_db


@pytest.fixture
def populate_db():
    User.objects.create_user('fulano', 'fulano@gmail.com', '1234')
    CEP.objects.create(
        cep='13175667',
        logradouro='Avenida Ipê Amarelo',
        bairro='Parque Villa Flores', localidade='Sumaré', uf='SP'
    )
    CEP.objects.create(
        cep='04180112',
        logradouro='Travessa 19 de Agosto',
        bairro='Jardim Maria Estela', localidade='São Paulo', uf='SP'
    )
    CEP.objects.create(
        cep='03047000',
        logradouro='Rua 21 de Abril',
        bairro='Brás', localidade='São Paulo', uf='SP'
    )


def test_empty_ceps(apiclient):
    response = apiclient.get(reverse('cep-list'))
    assert response.status_code == 200
    assert len(response.json()) == 0


def test_ceps_get(client, populate_db):
    response = client.get(reverse('cep-list'))
    json = response.json()
    assert response.status_code == 200
    assert len(json) == 3
    assert json[0]['cep'] == '03047000'


def test_ceps_post_unauthenticated(apiclient, populate_db):
    response = apiclient.post(reverse('cep-list'), {
        'cep': '29060490',
        'logradouro': 'Rua Marquês de Olinda',
        'bairro': 'Jardim da Penha', 'localidade': 'Vitória', 'uf': 'ES'})
    assert response.status_code == 403


def test_ceps_post_authenticated(apiclient, populate_db):
    apiclient.login(username='fulano', password='1234')
    response = apiclient.post(reverse('cep-list'), {
        'cep': '29060480',
        'logradouro': 'Rua Marquês de Olinda',
        'bairro': 'Jardim da Penha', 'localidade': 'Vitória', 'uf': 'ES'})
    assert response.status_code == 201
    assert reverse('cep-detail', args=['29060480']) in response.json()['url']


def test_ceps_post_duplicated_cep(apiclient, populate_db):
    apiclient.login(username='fulano', password='1234')
    response = apiclient.post(reverse('cep-list'), {
        'cep': '13175667',
        'logradouro': 'Avenida Ipê Amarelo',
        'bairro': 'Parque Villa Flores', 'localidade': 'Sumaré', 'uf': 'SP'})
    assert response.status_code == 400


def test_ceps_detail_get(apiclient, populate_db):
    response = apiclient.get(reverse('cep-detail', args=['13175667']))
    assert response.status_code == 200
    assert len(response.json()) == 6


def test_ceps_detail_get_inexistent_cep(apiclient, populate_db):
    response = apiclient.get(reverse('cep-detail', args=['12345678']))
    assert response.status_code == 404


def test_ceps_detail_patch_unauthenticated(apiclient, populate_db):
    response = apiclient.patch(reverse('cep-detail', args=['13175667']), {
        'bairro': 'Vila Flora'})
    assert response.status_code == 403


def test_ceps_detail_patch_authenticated(apiclient, populate_db):
    apiclient.login(username='fulano', password='1234')
    bairro = 'Vila Flora'
    response = apiclient.patch(reverse('cep-detail', args=['13175667']), {
        'bairro': bairro})
    assert response.status_code == 200
    json = response.json()
    assert json['bairro'] == bairro
    assert len(json) == 6


def test_ceps_detail_try_partial_update_with_put_authenticated(apiclient, populate_db):
    apiclient.login(username='fulano', password='1234')
    bairro = 'Vila Flora'
    response = apiclient.put(reverse('cep-detail', args=['13175667']), {
        'bairro': bairro})
    assert response.status_code == 400


def test_api_root(apiclient):
    response = apiclient.get(reverse('api-root'))
    assert response.status_code == 200


def test_cep_str(populate_db):
    cep = CEP.objects.get(pk='13175667')
    assert '13175667' in str(cep)
