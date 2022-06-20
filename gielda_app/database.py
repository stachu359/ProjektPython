
from urllib import response
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy import delete
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from gielda_app.schemas import GieldaOut, Gieldabase

SQLALCHEMY_DATABASE_URL= "sqlite:///./example.db"

engine=create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False})
SessionLocal= sessionmaker(bind=engine, autocommit= False, autoflush= False)

Base =declarative_base()

class Gielda(Base):
    __tablename__="gielda"

    id_akcji=Column(Integer, primary_key=True)
    nazwa=Column(String)
    cena_kupna=Column(Integer, default=0)
    cena_sprzedazy=Column(Integer, default=0)

def get_gielda(id_akcji:int, db: Session):
    return db.query(Gielda).filter(
        Gielda.id_akcji==id_akcji).first()

def get_gieldas(db: Session ):
    return db.query(Gielda).all()

def post_gielda(nazwa:str, cena_kupna:int, cena_sprzedazy:int,db: Session):
    
    new_gielda=Gielda(nazwa=nazwa, 
                    cena_kupna=cena_kupna, 
                    cena_sprzedazy=cena_sprzedazy, 
                    )
    db.add(new_gielda)
    db.commit()
    db.refresh(new_gielda)
    return new_gielda

def delete_gielda( id_akcji:int, db: Session):
    db.execute(delete(Gielda).where(Gielda.id_akcji==id_akcji))
    db.commit()    
    
def drop_gielda(db:Session):
    rows=db.query(Gielda).count()
    for x in range(rows+1):
        db.execute(delete(Gielda).where(Gielda.id_akcji==x))
    db.commit()