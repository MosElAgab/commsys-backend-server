import pytest
import requests as req
from app import create_app
# print(x)
# print(create_app)
# # from app.models.design import Design

@pytest.fixture
def app():
    app = create_app()
    return app

def test_it_works():
    app = create_app()
    app.run(debug=True, port=5001)
    url = 'http://127.0.0.1:5001/design/100'
    reposnse = req.get(url)
    print(reposnse.status_code)
    assert reposnse.status_code
    # data = reposnse.json()
    # print(data)