from decimal import Decimal
from ninja import ModelSchema, Schema
from pydantic import Field, BaseModel, EmailStr, constr, conint, conlist , confloat, condecimal
from datetime import date, datetime
from income.models import Income
from typing import Optional
from account.models import Users
class UserSchema(Schema):
    id: int
    username: str

class IncomeSchema(Schema):
    id: int
    source: str = None
    amount: Decimal
    description: str = None
    date: date
    user: Optional[UserSchema] = None
    created_at: datetime
    updated_at: datetime

class CreateIncomeSchema(BaseModel):
    source: Optional[str] = None
    amount: Decimal
    description: Optional[str] = None
    date: datetime = Field(default_factory=date.today)
    user_id: Optional[int] = None