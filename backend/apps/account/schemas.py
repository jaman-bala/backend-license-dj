from ninja import Schema


class UserSchemas(Schema):
    id: int
    username: str
    email: str
    password: str
    first_name: str
    last_name: str
    is_staff: bool
    is_active: bool

