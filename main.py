from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"zimba": "zamba", "bazimba": "zazamba"}


@app.get("/reviews")
async def root():
    return {"id": "1", "something": "sajdsjsadadsj"}
