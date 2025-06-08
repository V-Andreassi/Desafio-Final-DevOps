import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_home(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b"Minha API de DevOps est" in res.data 

def test_listar_usuarios_vazio(client):
    res = client.get('/usuarios')
    assert res.status_code == 200
    assert res.json == []

def test_adicionar_usuario(client):
    res = client.post('/usuarios', json={"nome": "Ana", "idade": 30})
    assert res.status_code == 201
    assert res.json["nome"] == "Ana"

def test_adicionar_usuario_dados_invalidos(client):
    res = client.post('/usuarios', json={"nome": "Sem idade"})
    assert res.status_code == 400

def test_buscar_usuario_existente(client):
    res_post = client.post('/usuarios', json={"nome": "Carlos", "idade": 25})
    user_id = res_post.json["id"]
    res = client.get(f'/usuarios/{user_id}')
    assert res.status_code == 200
    assert res.json["nome"] == "Carlos"

def test_buscar_usuario_inexistente(client):
    res = client.get('/usuarios/999')
    assert res.status_code == 404