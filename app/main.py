from fastapi import FastAPI
from app.api.bring import bring

app = FastAPI()


app.include_router(bring, prefix='/api/v1/bring', tags=['bring'])