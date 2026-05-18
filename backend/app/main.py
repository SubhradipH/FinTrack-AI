from fastapi import FastAPI
from app.routes.expense_routes import router

from app.database.database import engine
from app.database.database import Base
from app.models.expense_model import Expense

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.get("/")
def home():
    return {"message": "AI Expense Tracker Backend Running"}