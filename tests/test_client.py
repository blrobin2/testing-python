import json
from pytest import fixture

import project.client as app_client

@fixture
def client():
  app_client.app.config['TESTING'] = True

  with app_client.app.test_client() as client:
    yield client

def test_create_blog_bad_request(client):
  response = client.post(
    '/create-blog',
    data=json.dumps(dict(
      author='John Doe',
      title=None,
      content='Some content'
    )),
    content_type='application/json'
  )

  assert response.status_code == 400
  assert response.json is not None

def test_create_blog_success(client):
  response = client.post(
    '/create-blog',
    data=json.dumps(dict(
      author='author@email.com',
      title='Great title',
      content='Some content'
    )),
    content_type='application/json'
  )

  assert response.status_code == 201
  assert response.json['status'] == 'ok'
