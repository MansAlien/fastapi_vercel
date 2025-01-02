Project structure:

fastapi-postgres/
├── app/
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── api.py
│   │   ├── crud.py
│   │   ├── models.py
│   │   ├── schemas.py
│   ├── items/
│   │   ├── __init__.py
│   │   ├── api.py
│   │   ├── crud.py
│   │   ├── models.py
│   │   ├── schemas.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── security.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── base.py
│   ├── main.py
│   ├── tests/
│       ├── __init__.py
│       ├── test_auth.py
│       ├── test_items.py
├── .env
├── requirements.txt
├── Dockerfile
├── docker-compose.yml

