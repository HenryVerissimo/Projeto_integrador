from sqlalchemy import Column, String, Integer, Boolean
from src.model import Base


class Admin(Base):
    __tablename__ = "admin"

    admin_id = Column(Integer, primary_key=True)
    admin_name = Column(String(100), nullable=False)
    admin_email = Column(String(100), nullable=False)
    admin_password = Column(String(20), nullable=False)
    admin_level = Column(Integer, default=1)
    admin_status = Column(Boolean, default=True)