import pytest
from app.utils import greet

# Test per la funzione greet
# def test_greet():
#     assert greet("Test") == "Ciao, Test! Benvenuto nel progetto python."


# decoratore che ti permette di eseguire lo stesso test con più combinazioni di input e output attesi
@pytest.mark.parametrize(
    "name, expected_output",
    [
        ("Test", "Ciao, Test! Benvenuto nel progetto python."),
        ("Alessio", "Ciao, Alessio! Benvenuto nel progetto python."),
        ("👾", "Ciao, 👾! Benvenuto nel progetto python."),
        ("", "Ciao, ! Benvenuto nel progetto python."),
    ]
)
def test_greet(name, expected_output):
    assert greet(name) == expected_output