from sqlmodel import Field, SQLModel

class Peserta(SQLModel):
    nama: str | None = None
    sekolah: str | None = None

class PesertaDB(Peserta, table=True):
    id: int | None = Field(default=None, primary_key=True)
