from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from Models.catalog import Catalog
catalog_db = [
    {"id": 1, "name": "Luis", "age": 30},
    {"id": 2, "name": "Ana", "age": 23},
    {"id": 3, "name": "Jose", "age": 27},
    {"id": 4, "name": "Patty", "age": 15}
]
origins = ["http://localhost:5173", "https://luisavalosmaker.web.app"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Hola Mundo vat"}


@app.get("/api/v1/catalog/", response_model=list[Catalog])
def get_catalog_all():
    return catalog_db


@app.get("/api/v1/catalog/{catalog_id}", response_model=Catalog)
def get_catalog(catalog_id: int):
    for catalog in catalog_db:
        if catalog["id"] == catalog_id:
            return catalog
    raise HTTPException(status_code=404, detail="Catalog not found")


@app.post("/api/v1/catalog/", response_model=Catalog)
def create_catalog(catalog_data: Catalog):
    new_catalog = catalog_data.model_dump()
    catalog_db.append(new_catalog)
    return new_catalog


@app.delete("/api/v1/catalog/{catalog_id}", response_model=Catalog)
def delete_catalog(catalog_id: int):
    for catalog in catalog_db:
        if catalog["id"] == catalog_id:
            catalog_deleted = catalog
            catalog_db.remove(catalog)
            return catalog_deleted
    raise HTTPException(status_code=404, detail="Catalog not found")
