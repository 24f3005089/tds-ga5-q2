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
        divisor = 30.0
    elif req.spec == "v2":
        divisor = req.days_in_actual_month
    else:
        raise HTTPException(status_code=400, detail="Invalid spec")

    return {"charge": diff * (req.days_remaining / divisor)}
