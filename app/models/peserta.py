from sqlmodel import Field, SQLModel

class PesertaBase(SQLModel):
    nama: str
    sekolah: str

class PesertaAdd(PesertaBase):
    pass

class PesertaEdit(SQLModel):
    nama: str | None = None
    sekolah: str | None = None

class Peserta(PesertaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
