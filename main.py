# Penugasan Portofolio ARA 7.0
# IT Dev - Backend: CRUD web app
# Tech stack used: FastAPI & SQLModel
# Hendra Manudinata - 5027251051

from typing import Annotated
from fastapi import FastAPI, HTTPException, Query
from sqlmodel import select

# Import database utils AND models
# Models need to be imported to register them with SQLModel.metadata
from database import SessionDep
from models.peserta import Peserta, PesertaDB

app = FastAPI()


@app.get("/peserta/")
def get_all_peserta(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[PesertaDB]:
    peserta = session.exec(select(PesertaDB).offset(offset).limit(limit)).all()
    return peserta

@app.post("/peserta/")
def add_peserta(peserta: Peserta, session: SessionDep) -> PesertaDB:
    peserta = PesertaDB.model_validate(peserta)
    session.add(peserta)
    session.commit()
    session.refresh(peserta)
    return peserta

@app.get("/peserta/{peserta_id}")
def get_peserta(peserta_id: int, session: SessionDep) -> PesertaDB:
    peserta = session.get(PesertaDB, peserta_id)
    if not peserta:
        raise HTTPException(status_code=404, detail="Peserta tidak ditemukan")
    return peserta

# NOTE: Untuk edit peserta, seharusnya menggunakan method PUT atau PATCH
# namun request dari website, terutama dari form, biasanya hanya mendukung GET & POST
# Bisa diubah menjadi PATCH.
@app.post("/peserta/{peserta_id}")
def edit_peserta(peserta_id: int, peserta: Peserta, session: SessionDep) -> PesertaDB:
    peserta_data = session.get(PesertaDB, peserta_id)
    if not peserta:
        raise HTTPException(status_code=404, detail="Peserta tidak ditemukan")

    peserta_updated = peserta.model_dump(exclude_unset=True)
    peserta_data.sqlmodel_update(peserta_updated)

    session.add(peserta_data)
    session.commit()
    session.refresh(peserta_data)
    return peserta

@app.delete("/peserta/{peserta_id}")
def delete_peserta(peserta_id: int, session: SessionDep):
    peserta = session.get(PesertaDB, peserta_id)
    if not peserta:
        raise HTTPException(status_code=404, detail="Peserta tidak ditemukan")
    session.delete(peserta)
    session.commit()

    # return {"ok": True}
    return peserta
