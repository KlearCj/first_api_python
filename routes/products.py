#Importo APIRouter de fastApi
from fastapi import APIRouter

#Creo una instancia
router= APIRouter()

#Le digo que protocolo va a usar y creo una función. :D
@router.get('/products')
async def get_products():
    return 'Hello products'