from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, Router
from account.models import Users
from finance911.logger import logger
from income.models import Income
from income.api.schemas import IncomeSchema, CreateIncomeSchema, UserSchema
from django.utils import timezone

# app = NinjaAPI()
router = Router()

@router.get("/incomes", response=list[IncomeSchema])
def list_incomes(request):
    incomes = Income.objects.select_related('user').all()
    return [
        IncomeSchema(
            id=income.id,
            source=income.source,
            amount=income.amount,
            description=income.description,
            date=income.date,
            user=UserSchema(id=income.user.id, username=income.user.username) if income.user else None,
            created_at=income.created_at,
            updated_at=income.updated_at,
        )
        for income in incomes
    ]
@router.post("/incomes", response=IncomeSchema)
def create_income(request, payload: CreateIncomeSchema):
    try:
        logger.info(f'{payload.dict()}')
        user = get_object_or_404(Users, id=payload.user_id) if payload.user_id else None
        
        income = Income.objects.create(
            source=payload.source,
            amount=payload.amount,
            description=payload.description,
            date=payload.date or timezone.now(),
            user=user,
        )
        
        logger.info(f"Income created: {income.id}")
        
        return IncomeSchema(
            id=income.id,
            source=income.source,
            amount=income.amount,
            description=income.description,
            date=income.date,
            user=UserSchema(id=user.id, username=user.username) if user else None,
            created_at=income.created_at,
            updated_at=income.updated_at,
        )
    except Exception as e:
        logger.error(f"Error creating income: {str(e)}")
