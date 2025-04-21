from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
from app_store_scraper import AppStore

app = FastAPI()

@app.get("/")
async def root():
    return {"zimba": "zamba", "bazimba": "zazamba"}


@app.get("/reviews")
def get_reviews():
    app = AppStore(
        country='us',
        app_name="Lumi: styling & shopping",
        app_id='1637080045'
    )
    app.review(how_many=50)
    df = pd.DataFrame(app.reviews)
    return JSONResponse(content=df.to_dict(orient="records"))
