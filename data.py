from pydantic import BaseModel
from typing import List

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
