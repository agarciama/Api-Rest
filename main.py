from fastapi import FastAPI, HTTPException
from typing import List
from data import Articulo, db

app = FastAPI()

#Crear un nuevo artículo
@app.post("/articulos/crear", response_model=Articulo)
async def crear_articulo(articulo: Articulo):
    db.append(articulo)
    return articulo

#Leer todos los artículos
@app.get("/articulos/", response_model=List[Articulo])
async def leer_articulos():
    return db

#Leer un artículo por su ID
@app.get("/articulos/{articulo_id}", response_model=Articulo)
async def leer_articulo(articulo_id: int):
    articulo = next((art for art in db if art.id == articulo_id), None)
    if articulo is None:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")
    return articulo

#Modificar un artículo por su ID
@app.put("/articulos/modificar/{articulo_id}", response_model=Articulo)
async def modificar_articulo(articulo_id: int, articulo: Articulo):
    idx = next((index for index, art in enumerate(db) if art.id == articulo_id), None)
    if idx is None:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")
    db[idx] = articulo
    return articulo

#Borrar un artículo por su ID
@app.delete("/articulos/borrar/{articulo_id}", response_model=Articulo)
async def borrar_articulo(articulo_id: int):
    idx = next((index for index, art in enumerate(db) if art.id == articulo_id), None)
    if idx is None:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")
    return db.pop(idx)
