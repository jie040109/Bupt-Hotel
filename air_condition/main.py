from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import (
   admin,user,schedule
)

app = FastAPI()

origins = [
    "http://localhost:8080/",
    "http://10.29.80.241:8080/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(admin.router)
app.include_router(user.router)
app.include_router(schedule.router)

    


