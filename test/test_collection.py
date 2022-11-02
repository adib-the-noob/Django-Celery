from rest_framework.test import APIClient

class TestPost:
    def test_create_post(self):
        client = APIClient()
        response = client.post('/posts/',{
        "title": "Hellllllllop",
        "body": "This is Mew",
        "author": 1
        })