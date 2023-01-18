from sqlalchemy import Column, Integer, String, Text, DateTime
from app.db.session import Base


class BigDataInput(Base):
    __tablename__ = "big_data_input"

    idx = Column(Integer, primary_key=True, autoincrement=True)
    yy = Column(String)
    shtm = Column(String)
    std_no = Column(String)
