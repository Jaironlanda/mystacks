from fastapi import APIRouter

router = APIRouter(prefix='/items', tags=['Item'])

@router.get('/')
async def item():
  return {'message': 'Items root'}