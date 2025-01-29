from fastapi import FastAPI
from app.routers import categoty, products

app = FastAPI()


@app.get('/')
async def welcome() -> dict:
    return {"message": "My e-commerce app"}

app.include_router(categoty.router)
app.include_router(products.router)
