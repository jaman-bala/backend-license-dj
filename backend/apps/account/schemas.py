from ninja import Schema

class LoginInput(Schema):
    username: str
    password: str
