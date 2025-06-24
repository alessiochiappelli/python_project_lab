
class Greeter:
    """Classe che rappresenta un generatore di saluti personalizzati."""
    
    def __init__(self, name: str, greeting: str = "Ciao"):
        """Costruttore: viene eseguito alla creazione dell'oggetto."""
        self.name = name  # Attributo dell'istanza
        self.greeting = greeting
    
    def greet(self) -> str:
        """Metodo che restituisce un saluto."""
        return f"{self.greeting}, {self.name}! Benvenuto nel progetto Python."

