from fastapi import FastAPI
from routes import users
from routes import products
app= FastAPI()

#en la instancia de fastapi uso a la función include router para hacer la ruta.
app.include_router(users.router)
app.include_router(products.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}