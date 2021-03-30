from fastapi import FastAPI 
import requests
import uvicorn

app = FastAPI()


@app.get("/")
def get_root():
    return {"Hello": "World"}

@app.get("/delay/{sec}")
def get_delay(sec: int):


    requests.get("https://httpbin.org/delay/{}".format(sec))
    return {"sec": sec}

@app.post("/anything")
def post_anything():
    r = requests.post("https://httpbin.org/anything")
    return r.json

