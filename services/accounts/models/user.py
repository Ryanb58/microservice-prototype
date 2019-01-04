from sqlalchemy import Column, Integer, String

class User(db.Model):
    """User table used to represent people in meatspace."""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    email = Column(String)
    password = Column(String)
    confirm_token = Column(String)
    password_reset_token = Column(String)

    def __repr__(self):
       return "<User(name='%s', email='%s', password='%s')>" % (
                            self.name, self.email, self.password)

