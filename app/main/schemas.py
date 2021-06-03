from app import ma


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("email", "date_created")
