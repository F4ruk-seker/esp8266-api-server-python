import datetime

from fastapi import FastAPI

from _information import Database
from _information import notification
import json
import asyncio

import time
app = FastAPI(title="pars")


db = Database()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/esp/{ID}/sensor/{value}")
async def update_esp_sensor_status(ID:str,value: int):
    def delay_calculator():
        _delay_date = data.get('delay')
        if _delay_date:
            return datetime.datetime.now().timestamp() > _delay_date

    data = db.getEspData(ID)

    if data:
        db.updateEspData(ID=ID, value=str(value))
        if data.get('alert_border') and value > data.get('alert_border') and delay_calculator() != False:
            db.update_alert_time_out(ID)
            notification("a","a")
        return data

    else:
        return {"detail":"Not Found"}

@app.get("/esp/{ID}/status")
async def get_esp_status(ID):
    data = db.getEspData(ID)
    if data:
        return data
    else:
        return {"detail":"Not Found"}
