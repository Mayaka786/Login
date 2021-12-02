from werkzeug.security import check_password_hash, generate_password_hash
from . import db, login_manager


def get_by_mail_username(username_mail):
    user = User.query.filter_by(username=username_mail).first()
    if user is None:
        user = User.query.filter_by(email=username_mail).first()
    return user


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)

    posts = db.relationship("Post", backref="posts", lazy=True)

    @property
    def password(self):
        raise AttributeError("You cannnot read the password attribute")

    @password.setter
    def password(self, password_raw):
        self.password_hash = generate_password_hash(password_raw)

    def verify_password(self, password_raw):
        return check_password_hash(self.password_hash, password_raw)

    @classmethod
    def get_user(cls, id):
        return User.query.get(id)

    def __repr__(self):
        return f"User('{self.email}')"


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"User('{self.title}')"
