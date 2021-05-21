import uuid

from flask import Flask, jsonify, request
from pydantic import ValidationError, BaseModel, EmailStr, Field

app = Flask(__name__)

@app.errorhandler(ValidationError)
def handle_validation_exception(error):
  response = jsonify(error.errors())
  response.status_code = 400
  return response


class Blog(BaseModel):
  id: str = Field(default_factory=lambda: str(uuid.uuid4()))
  author: EmailStr
  title: str
  content: str



@app.route('/create-blog', methods=['POST'])
def create_blog():
  data = request.get_json() or {}
  Blog(**data)
  return dict(status='ok'), 201
