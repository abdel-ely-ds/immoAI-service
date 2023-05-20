from typing import Optional

from fastapi import FastAPI, Depends, Query
import pandas as pd

from services.dashboard_service import DashboardService

app = FastAPI()
df: Optional[pd.DataFrame] = None


@app.on_event("startup")
async def startup_event():
    global df
    df = pd.read_csv("data.csv")


@app.get('/')
def root():
    return {"message": "working"}


@app.get("/dashboard", status_code=200)
async def get_dashboard(country: str = Query("Country3", description="Country you are interested in"),
                        city: str = Query("City5", description="City you are interested in"),
                        service: DashboardService = Depends()):
    return service.overview(df, country=country, city=city)
