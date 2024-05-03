from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Articulo(BaseModel):
    id: int
    titulo: str
    modelo: str
    precio: int
    contenido: str

# Inicializando la 'base de datos' en memoria
db: List[Articulo] = [
    Articulo(id=0, titulo="iPhone 12", modelo="A2403", precio=799, contenido="Lanzado en 2020"),
    Articulo(id=1, titulo="iPhone 11", modelo="A2111", precio=699, contenido="Lanzado en 2019"),
    Articulo(id=2, titulo="iPhone X", modelo="A1865", precio=899, contenido="Lanzado en 2017"),
    Articulo(id=3, titulo="iPhone 8", modelo="A1863", precio=449, contenido="Lanzado en 2017"),
    Articulo(id=4, titulo="iPhone 7", modelo="A1778", precio=449, contenido="Lanzado en 2016"),
    Articulo(id=5, titulo="iPhone 6s", modelo="A1688", precio=449, contenido="Lanzado en 2015")
]


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
