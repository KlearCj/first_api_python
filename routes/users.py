#Importo APIRouter de fastApi
from fastapi import APIRouter

#Creo una instancia
router= APIRouter()

#Le digo que protocolo va a usar y creo una función. :D
@router.get('/users')
async def get_users():
    return 'Hello users'
