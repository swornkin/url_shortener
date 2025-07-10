import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_shorten_url(client):
    response = client.post('/shorten', json={'url': 'https://openai.com'})
    assert response.status_code == 201
    data = response.get_json()
    assert 'short_url' in data
    assert data['short_url'].startswith('http://localhost:5000/')