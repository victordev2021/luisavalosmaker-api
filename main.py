from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from Models.project import Project
project_db = [
    {"id": 1, "name": "Mezón Cocina", "category": "Cocina",
        "detail": "asdfasd", "url": "http//:asdasd", "type": 0},
    {"id": 2, "name": "Mueble Televisor", "category": "Dormitorio",
        "detail": "asdfasd", "url": "https://drive.google.com/file/d/1Afq5_ikrwvCWkoJDs70nUA40JgCub2x0/view?usp=sharing", "type": 0},
    {"id": 3, "name": "Isla Flotante", "category": "Cocina",
        "detail": "asdfasd", "url": "http//:asdasd", "type": 1},
    {"id": 4, "name": "Velador Personalizado", "category": "Dormitorio",
        "detail": "asdfasd", "url": "http//:asdasd", "type": 0},
    {"id": 5, "name": "Modulo de Estantes", "category": "Oficina",
        "detail": "asdfasd", "url": "http//:asdasd", "type": 0},
    {"id": 6, "name": "Escritorios", "category": "Oficina",
        "detail": "asdfasd", "url": "http//:asdasd", "type": 0},
    {"id": 7, "name": "Modulo Televisor", "category": "Sala",
        "detail": "asdfasd", "url": "http//:asdasd", "type": 1},
    {"id": 8, "name": "Closet dos cuerpos", "category": "Dormitorio",
        "detail": "asdfasd", "url": "http//:asdasd", "type": 0},
    {"id": 9, "name": "Peinador Pequeño", "category": "Dormitorio",
        "detail": "asdfasd", "url": "http//:asdasd", "type": 2},
    {"id": 10, "name": "Modulo Libros", "category": "Sala",
        "detail": "asdfasd", "url": "http//:asdasd", "type": 0},
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
    return {"message": "Proyectos muebles"}


@app.get("/api/v1/project/", response_model=list[Project])
def get_projects():
    return project_db


@app.get("/api/v1/project/{project_id}", response_model=Project)
def get_project(project_id: int):
    for project in project_db:
        if project["id"] == project_id:
            return project
    raise HTTPException(status_code=404, detail="Catalog not found")


@app.post("/api/v1/project/", response_model=Project)
def create_project(project_data: Project):
    new_project = project_data.model_dump()
    project_db.append(new_project)
    return new_project


@app.delete("/api/v1/project/{project_id}", response_model=Project)
def delete_project(project_id: int):
    for project in project_db:
        if project["id"] == project_id:
            project_deleted = project
            project_db.remove(project)
            return project_deleted
    raise HTTPException(status_code=404, detail="Catalog not found")
