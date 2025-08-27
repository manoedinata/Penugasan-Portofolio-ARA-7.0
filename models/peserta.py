from sqlmodel import Field, SQLModel

class Peserta(SQLModel):
    nama: str
    sekolah: str

class PesertaDB(Peserta, table=True):
    id: int | None = Field(default=None, primary_key=True)
