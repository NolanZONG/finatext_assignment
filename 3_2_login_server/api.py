import hashlib
import logging
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class LoginRequest(BaseModel):
    username: str
    password: str


class FlagRequest(BaseModel):
    flag: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.put("/login")
def login(request: LoginRequest):
    # 计算 "admin" + password 的 SHA1 值
    combined_string = "admin" + request.password
    token = hashlib.sha1(combined_string.encode()).hexdigest()
    return {"token": token}

@app.put("/flag")
def flag(request: FlagRequest):
    logger.info(f"Flag request received: {request.flag}")
    return {"flag": request.flag}