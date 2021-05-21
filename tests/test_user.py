from pydantic.error_wrappers import ValidationError

from project.user import User

def test_user_validation_failure():
  try:
    User(email='fake')
  except ValidationError as err:
    assert any([ e['type'] == 'value_error.email' for e in err.errors() ])

def test_user_validation_success():
  email = 'real@email.com'
  user = User(email=email)
  assert user.email == email
