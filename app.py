from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]
app = FastAPI(
  title="Bank API",
  version="1.0.0",
  middleware=middleware
)

@app.get(path="/")
async def getIndex(request:Request):
  return "Hello Docker"