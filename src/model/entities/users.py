from sqlalchemy import Column, Integer, String, Boolean
from src.model import Base

class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(100), nullable=False)
    user_email = Column(String(100), nullable=False)
    user_password = Column(String(20), nullable=False)
    user_admin = Column(Boolean, default=False)
    user_status = Column(Boolean, default=True)

    def __repr__(self):
        return f"users(user_id={self.user_id}, user_name={self.user_name}, user_email={self.user_email}, user_password={self.user_password}, user_admin{self.user_admin} user_status={self.user_status})"
