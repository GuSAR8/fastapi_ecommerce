from fastapi import APIRouter


router = APIRouter(prefix='/categories', tags=['category'])


@router.get('/')
async def get_all_categories():
    ...


@router.post('/')
async def create_category():
    ...


@router.put('/')
async def update_category():
    ...


@router.get('/')
async def delete_category():
    ...
