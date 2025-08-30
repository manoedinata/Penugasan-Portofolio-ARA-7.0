# Penugasan Portofolio ARA 7.0
# IT Dev - Backend: CRUD web app
# Tech stack used: FastAPI & SQLModel
# Hendra Manudinata - 5027251051

from typing import Annotated
from fastapi import FastAPI, HTTPException, Query, Request
from sqlmodel import select
from fastapi.templating import Jinja2Templates # For web UI only
from fastapi.responses import HTMLResponse # For web UI only

from app.settings import settings

# Import database utils AND models
from app.database import SessionDep
from app.models.peserta import Peserta, PesertaAdd, PesertaEdit

openapi_tags = {
    "name": "Peserta",
    "description": "Operasi CRUD peserta.",
},

app = FastAPI(title=settings.app_name, openapi_tags=openapi_tags)
templates = Jinja2Templates(directory="app/templates") # For web UI only


@app.get("/", include_in_schema=False, response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.html"
    )

@app.get("/peserta/", tags=["Peserta"])
def get_all_peserta(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Peserta]:
    peserta = session.exec(select(Peserta).offset(offset).limit(limit)).all()
    return peserta

@app.post("/peserta/", tags=["Peserta"])
def add_peserta(peserta: PesertaAdd, session: SessionDep) -> Peserta:
    peserta = Peserta.model_validate(peserta)
    session.add(peserta)
    session.commit()
    session.refresh(peserta)
    return peserta

@app.get("/peserta/{peserta_id}", tags=["Peserta"])
def get_peserta(peserta_id: int, session: SessionDep) -> Peserta:
    peserta = session.get(Peserta, peserta_id)
    if not peserta:
        raise HTTPException(status_code=404, detail="Peserta tidak ditemukan")
    return peserta

# NOTE: Untuk edit peserta, seharusnya menggunakan method PUT atau PATCH
# namun request dari website, terutama dari form, biasanya hanya mendukung GET & POST
# Bisa diubah menjadi PATCH.
# @app.patch("/peserta/{peserta_id}")
@app.post("/peserta/{peserta_id}", tags=["Peserta"])
def edit_peserta(peserta_id: int, peserta: PesertaEdit, session: SessionDep) -> Peserta:
    peserta_data = session.get(Peserta, peserta_id)
    if not peserta:
        raise HTTPException(status_code=404, detail="Peserta tidak ditemukan")

    # Convert peserta model to dict, excluding unset values
    peserta_updated = peserta.model_dump(exclude_unset=True)
    # Update peserta_data with new values
    peserta_data.sqlmodel_update(peserta_updated)

    session.add(peserta_data)
    session.commit()
    session.refresh(peserta_data)
    return peserta_data

@app.delete("/peserta/{peserta_id}", tags=["Peserta"])
def delete_peserta(peserta_id: int, session: SessionDep):
    peserta = session.get(Peserta, peserta_id)
    if not peserta:
        raise HTTPException(status_code=404, detail="Peserta tidak ditemukan")
    session.delete(peserta)
    session.commit()

    # return {"ok": True}
    return peserta
