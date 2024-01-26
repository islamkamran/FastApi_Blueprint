from fastapi import APIRouter
# main router
router = APIRouter(prefix= '/api/v1')

@router.get('/')
def index1():
    return 'Hello'
