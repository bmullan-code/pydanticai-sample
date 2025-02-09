from sqlalchemy import Column, Integer, String
from database import Base

# Define the User model
class User(Base):
    __tablename__ = "users"


#       id = Column(Integer, primary_key=True, index=True)
#     username = Column(String(50), unique=True)
#     email = Column(String(50), unique=False)
#     posts = relationship("Post",back_populates="user", lazy="joined")

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    account_status = Column(String(50), nullable=False)
    subscription_plan = Column(String(50), nullable=False)