from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_route():
    return {"message":"Hello I built this app"}
@app.get("/status")
def checkStatus():
    return {"system":"online",
            "user":"Backened Engineer"}