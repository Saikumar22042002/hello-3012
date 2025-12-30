"""Unit tests for the Flask application."""
import pytest
from app import app as flask_app

@pytest.fixture(scope='module')
def client():
    """Create and configure a new app instance for each test."""
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as test_client:
        yield test_client

def test_index_endpoint(client):
    """Test the main '/' endpoint for a 200 OK response and correct message."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Hello from hello-3012 on branch hello-v1"}

def test_health_endpoint(client):
    """Test the '/health' endpoint for a 200 OK response and healthy status."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}
