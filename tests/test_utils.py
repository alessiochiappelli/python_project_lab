import pytest
from app.greeter import Greeter

# Test per la classe Greeter

# decoratore che permette di eseguire lo stesso test con più combinazioni di input e output attesi
@pytest.mark.parametrize(
    "name, greeting, expected_output",
    [
        ("Alessio", "Ciao", "Ciao, Alessio! Benvenuto nel progetto Python."),
        ("Ada", "Salve", "Salve, Ada! Benvenuto nel progetto Python."),
        ("Sconosciuto", "", ", Sconosciuto! Benvenuto nel progetto Python."),
        ("👾", "Yo", "Yo, 👾! Benvenuto nel progetto Python."),
    ]
)
def test_greeter_custom_greeting(name, greeting, expected_output):
    #crea un oggetto della classe Greeter
    obj_greeter = Greeter(name, greeting)
    
    assert obj_greeter.greet() == expected_output