import pytest
from application import create_app


class TestApplication():
    @pytest.fixture
    def client(self):
        app = create_app('config.MockConfig')
        return app.test_client()

    @pytest.fixture
    def valid_user(self):
        return {
            "first_name": "Gabriel",
            "last_name": "Alves",
            "cpf": "430.703.818-55",
            "email": "gabriel0611@gmail.com",
            "birth_date": "2002-11-06"
        }
    
    @pytest.fixture
    def invalid_user(self):
        return {
            "first_name": "Gabriel",
            "last_name": "Alves",
            "cpf": "430.703.818-55",
            "email": "gabriel0611@gmail.com",
            "birth_date": "2002-11-06"
        }

    def test_get_users(self, client):
        response = client.get('/users')
        assert response.status_code == 200

    def test_post_user(self, client, valid_user, invalid_user):
        response = client.post('/user', json=valid_user)
        assert response.status_code == 200
        assert b"successfully" in response.data

        response = client.post('/user', json=valid_user)
        assert response.status_code == 200
        assert b"successfully" in response.data
