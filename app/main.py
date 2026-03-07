from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()


def foo() -> JSONResponse:
    return JSONResponse(content={"msg": "ok"})


@app.get("/")
def index() -> JSONResponse:
    return foo()
