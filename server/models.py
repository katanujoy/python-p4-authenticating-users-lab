class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username
        }
