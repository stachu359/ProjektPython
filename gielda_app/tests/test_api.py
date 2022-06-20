from urllib import response
from ..main import app
from fastapi.testclient import TestClient
from fastapi import status

client =TestClient(app)

def test_gielda_no_query_params():
    response=client.get("/gielda")
    assert response.status_code==status.HTTP_200_OK
    data=response.json()
    assert isinstance(data,list)

def test_gielda_params():
    response=client.get("/gielda?id_akcji=1")
    assert response.status_code==status.HTTP_200_OK
    data=response.json()
    assert isinstance(data,list)

def test_gielda_post():
    body={
        "nazwa":"Akcja",
        "cena_kupna": 13,
        "id_akcji":1,
        "cena_sprzedazy": 34
    } 
    response=client.post("/gielda", json=body)
    assert response.status_code-204==status.HTTP_201_CREATED

def test_gielda_delete():
    response=client.delete("/gielda?id_akcji=1")
    assert response.status_code==status.HTTP_204_NO_CONTENT
   