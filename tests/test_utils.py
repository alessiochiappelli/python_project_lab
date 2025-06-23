from app.utils import greet

def test_greet():
    assert greet("Test") == "Ciao, Test! Benvenuto nel progetto python."
