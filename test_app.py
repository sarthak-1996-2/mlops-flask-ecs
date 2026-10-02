from app import app
import pytest
import json

@pytest.fixture
def client():
    return app.test_client()


def test_home(client):
    resp = client.get("/")
    assert resp.status_code == 200

def test_ping(client):
    resp = client.get("/ping")
    assert resp.status_code == 200

def test_aboutus(client):
    resp = client.get("/aboutus")
    assert resp.status_code == 200

def test_predict(client):
    test_data = {'Gender':"Male", 'Married':"Unmarried",'Credit_History' : "Unclear Debts",'ApplicantIncome':100000,'LoanAmount':2000000}
    resp = client.post("/predict", json=test_data)
    print("resp", resp)
    assert resp.text == "Your loan Rejected"
    assert resp.status_code == 200