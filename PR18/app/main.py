from fastapi import FastAPI
from app.data.database import engine, Base
from app.routers.objects import router as objects_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Cloud Application - Object Storage API",
    description="Лабораторная работа №18: Хранение файлов и объектов",
    version="1.0.0"
)

app.include_router(objects_router)

@app.get("/", summary="Корневой эндпоинт")
def root():
    return {"message": "Cloud Application Object Storage API is running", "docs": "/docs"}