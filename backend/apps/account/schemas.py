from ninja import Schema

class UserSchemas(Schema):
    id: int
    username: str
    first_name: str
    last_name: str
