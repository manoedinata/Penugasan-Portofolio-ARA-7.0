# Penugasan Portofolio ARA 7.0 - IT Dev Backend

Aplikasi _Create, Read, Update, Delete_ (CRUD) sederhana berbasis FastAPI & SQLModel, dengan database SQL seperti PostgreSQL.

Aplikasi ini menjadi penugasan portofolio pendaftaran staf [ARA 7.0](https://instagram.com/ara_its) divisi IT Dev, bagian Backend.

## Kenapa FastAPI? Bukan Flask?

Pada awalnya saya ingin menggunakan Flask karena lebih terbiasa. Namun, karena FastAPI saat ini semakin
_mature_ dan performanya juga _on par_ dengan framework JavaScript lain (source: _benchmark_ oleh FastAPI), penugasan
ini pada akhirnya menggunakan FastAPI. Dan juga, FastAPI menyediakan dokumentasi _API route_ secara otomatis berbasis
Swagger & OpenAPI spec, sehingga memudahkan untuk membuat REST API.

Namun, jika ditanya, saya lebih memilih Flask. :D

## API Docs

Dokumentasi API route dapat dilihat di [/docs](https://penugasan-porto-ara70.mdinata.my.id/docs).

## Directory Structure

```
├── alembic.ini  ---> Konfigurasi Alembic untuk database migration
├── app
│   ├── __init__.py
│   ├── database.py  ---> Konfigurasi database
│   ├── main.py  ---> Kode aplikasi utama
│   ├── models
│   │   └── peserta.py --> Models untuk data validation dan input ke ORM
│   └── settings.py ---> Konfigurasi aplikasi
├── main.py
├── migrations ---> Histori database migration untuk pembuatan tabel di database
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       ├── 6200c3a87c2d_initialize_tables.py
│       └── __pycache__
│           └── 6200c3a87c2d_initialize_tables.cpython-312.pyc
├── requirements.txt
└── vercel.json
```

## Cara Menjalankan

```bash
pip install -r requirements.txt

# For production
python3 main.py

# For development
fastapi dev app/main.py
```
