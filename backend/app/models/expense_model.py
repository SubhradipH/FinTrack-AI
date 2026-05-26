from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database.database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    amount = Column(Float)
    category = Column(String)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )