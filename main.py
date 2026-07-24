from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal

app = FastAPI()

class Request(BaseModel):
    old_price: float
    new_price: float
    days_remaining: int
    days_in_actual_month: int
    spec: Literal["v1", "v2"]

@app.post("/proration")
def proration(req: Request):
    diff = req.new_price - req.old_price

    if req.spec == "v1":
        charge = diff * (req.days_remaining / 30)
    else:
        charge = diff * (req.days_remaining / req.days_in_actual_month)

    return {"charge": charge}