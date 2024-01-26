from fastapi import APIRouter, HTTPException
from src.models.query_model import QueryModel

# router for user
router = APIRouter(prefix='/user')


@router.get('/')
def index():
    return {'Hello': 'Bye'}
