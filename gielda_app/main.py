from typing import Optional
from urllib import response
from fastapi import FastAPI,status, HTTPException, Depends
from .schemas import GieldaOut, ErrorInfo
from .database import SessionLocal, engine, Base, get_gieldas as db_get_gieldas, post_gielda as db_post_gielda, get_gielda as db_get_gielda, delete_gielda as db_delete_gielda, drop_gielda as db_drop_gielda
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app=FastAPI()

def create_db_session():
    db_session=SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

@app.get("/",summary="Returns an index view.")
def index():

    return {"message":"Cokolwiek"}

@app.get('/gielda')
def get_gielda(db_session: Session=Depends(create_db_session)):
    #db_session=SessionLocal()
    #gielda=db_get_gielda(db_session)
    #db_session.close()
    #return gielda
    db_gielda=db_get_gieldas(db_session)
    return db_gielda if db_gielda else []


@app.get('/gielda/{id_akcji}', response_model=GieldaOut, responses={
    status.HTTP_404_NOT_FOUND:{"model":ErrorInfo}
})
def get_gielda(id_akcji: int,db_session: Session=Depends(create_db_session)):

    gielda=db_get_gielda(id_akcji,db_session)
    if gielda:
         return gielda            
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Akcja not found.")

@app.post('/gielda/{nazwa}/{cena_kupna}/{cena_sprzedazy}', response_model=GieldaOut, status_code=status.HTTP_201_CREATED)
def post_gielda( nazwa:str, cena_kupna:int, cena_sprzedazy:int,db_session: Session=Depends(create_db_session)):
    """
    Creates a new Akcja

    **Nazwa**: Nazwa Akcji
    **Cena_kupna**: cena kupna akcji
    **Cena_sprzedazy**: cena sprzedazy akcji
    """

    new_gielda=db_post_gielda(nazwa, cena_kupna, cena_sprzedazy, db_session)
    return new_gielda

@app.delete('/gielda/{id_akcji}', status_code=status.HTTP_204_NO_CONTENT)
def delete_akcja(id_akcji:int,db_session: Session=Depends(create_db_session)):

    db_gielda=get_gielda(id_akcji, db_session)
    if db_gielda:
        db_delete_gielda(id_akcji,db_session)


@app.delete('/gielda', status_code=status.HTTP_204_NO_CONTENT)
def drop_gielda(db_session: Session=Depends(create_db_session)):

    db_drop_gielda(db_session)   