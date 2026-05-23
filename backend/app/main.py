from fastapi import FastAPI
from app.routes.expense_routes import router

from app.database.database import engine
from app.database.database import Base
from app.models.expense_model import Expense
from app.models.user_model import User
from app.routes.auth_routes import router as auth_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)
app.include_router(auth_router)


@app.get("/")
def home():
    return {"message": "AI Expense Tracker Backend Running"}

