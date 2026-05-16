from fastapi import APIRouter
from app.schemas.expense_schema import Expense

router =APIRouter()

# Temporary storage
expenses=[]

@router.post("/expenses")
def add_expense(expense: Expense):
    expenses.append(expense)
    return{
        "message": "Expense Added Successfully",
        "data": expense
    }
    
@router.get("/expenses")
def get_expenses():
    return expenses