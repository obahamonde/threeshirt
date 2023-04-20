from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

static = StaticFiles(directory="static", html=True)

app = FastAPI()

app.mount("/", static, name="static")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)