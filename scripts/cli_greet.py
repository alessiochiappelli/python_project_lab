import argparse
from app.greeter import Greeter

def run_cli_greet(name:str) -> str:
    """
    Crea un oggetto Greeter e stampa il saluto.
    """
    obj_greeter = Greeter(name)
    print(obj_greeter.greet())

def main():
    # Crea un parser per gli argomenti della riga di comando
    parser = argparse.ArgumentParser(
        description="Script di saluto personalizzato via terminale."
    )
    # Aggiungi un argomento per il nome dell'utente
    parser.add_argument(
        "--name",
        required=True,
        help="Il nome dell'utente da salutare."
    )
    # Ricevi gli argomenti dalla riga di comando
    args = parser.parse_args()
    
    run_cli_greet(args.name)


if __name__ == "__main__":
    main()
