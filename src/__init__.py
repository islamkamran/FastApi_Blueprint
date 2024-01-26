from fastapi import FastAPI
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(docs_url=None if os.environ.get("DOCS_URL") == 'None'
              else os.environ.get("DOCS_URL"),
              redoc_url=None if os.environ.get("RE_DOC_URL") == 'None'
              else os.environ.get("RE_DOC_URL"))

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# import components and business logic class here

# routes here
from .routes import api_router, user_router
# nested routes
api_router.router.include_router(router=user_router.router)
app.include_router(router=api_router.router)
