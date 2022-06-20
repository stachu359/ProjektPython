from fastapi import FastAPI
from pydantic import BaseModel

class Gieldabase(BaseModel):
    nazwa: str
    cena_kupna:int
    cena_sprzedazy:int


class GieldaOut(Gieldabase):
    id_akcji:int

    class Config:
        orm_mode=True

class ErrorInfo(BaseModel):
    message:str



"""
    class Config:
        schema_extra ={
            "example":{
                "nazwa": "BankoPKO",
                "cena_kupna":16,
                "cena_sprzedazy":14
            }
        }
        """  