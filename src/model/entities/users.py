from sqlalchemy import Column, Integer, String, Boolean
from src.model import Base

class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(100), nullable=False)
    user_email = Column(String(100), nullable=False)
    user_password = Column(String(20), nullable=False)
    user_status = Column(Boolean, default=True)

    def __repr__(self):
        return f"users(id={self.user_id}, user={self.user_name}, email={self.user_email}, password={self.user_password}, user_status={self.user_status})"
