from fastapi import FastAPI
from starlette.responses import JSONResponse

from app.config.settings import settings

app = FastAPI(title=settings.app.title)


def foo() -> JSONResponse:
    return JSONResponse(content={"msg": "ok"})


@app.get("/")
def index() -> JSONResponse:
    return foo()
