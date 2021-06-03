from app import ma
from app.main.models import User


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        # Fields to expose
        model = User

    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
    date_created = ma.auto_field()
    status = ma.auto_field()
