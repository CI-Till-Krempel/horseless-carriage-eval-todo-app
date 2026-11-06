import pytest
from app import app, db, User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        with app.test_client() as client:
            yield client
        db.drop_all()

def test_user_registration_success(client):
    response = client.post('/register', data={
        'username': 'testuser',
        'password': 'securepassword'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Registration successful!' in response.data
    
    with app.app_context():
        user = User.query.filter_by(username='testuser').first()
        assert user is not None

def test_user_registration_duplicate_username(client):
    client.post('/register', data={
        'username': 'testuser',
        'password': 'securepassword'
    }, follow_redirects=True)
    
    response = client.post('/register', data={
        'username': 'testuser',
        'password': 'anotherpassword'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Username is already taken.' in response.data
