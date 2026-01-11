from fastapi import FastAPI , HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routes import router


app = FastAPI()

origins = [
    "http://localhost:3000", # ur frontend link
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=[origins],
    allow_credentials=True,
    allow_methods=["GET , POST"], # allowed HTTP requests 
    allow_headers=["*"],
)


app.include_router(router)
