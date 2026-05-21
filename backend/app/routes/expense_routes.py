from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.expense_schema import Expense
from app.models.expense_model import Expense as ExpenseModel
from app.database.database import get_db


router =APIRouter()


@router.post("/expenses")
def add_expense(expense: Expense, db: Session=Depends(get_db)):
    new_expense=ExpenseModel(
        title=expense.title,
        amount=expense.amount,
        category=expense.category
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return{
        "message": "Expense Added Successfully",
        "data": new_expense
    }
    
@router.get("/expenses")
def get_expenses(db: Session=Depends(get_db)):
    expenses=db.query(ExpenseModel).all()
    return expenses
    
@router.put("/expenses/{expense_id}")
def update_expense(
    expense_id: int,
    expense: Expense,
    db: Session = Depends(get_db)
):

    existing_expense = db.query(ExpenseModel).filter(
        ExpenseModel.id == expense_id
    ).first()

    if not existing_expense:
        return {"message": "Expense not found"}

    existing_expense.title = expense.title
    existing_expense.amount = expense.amount
    existing_expense.category = expense.category

    db.commit()
    db.refresh(existing_expense)

    return {
        "message": "Expense updated successfully",
        "data": existing_expense
    }


@router.delete("/expenses/{expense_id}")
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):

    expense = db.query(ExpenseModel).filter(
        ExpenseModel.id == expense_id
    ).first()

    if not expense:
        return {"message": "Expense not found"}

    db.delete(expense)
    db.commit()

    return {"message": "Expense deleted successfully"}
