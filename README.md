# 🐍 python_project_lab – Blocco 03: Introduzione alla Programmazione a Oggetti (OOP)

Estensione del progetto didattico dedicata all’apprendimento dei concetti base dell’OOP in Python.  
In questo branch esploriamo la costruzione e l’uso di classi, imparando a modellare oggetti con stato interno e comportamento, secondo i principi della programmazione moderna.

## 📦 Struttura del progetto

```
python_project_lab/
├── src/
│   └── app/
│       ├── __init__.py
│       ├── utils.py           # Funzione greet (ora wrapper su classe Greeter)
│       └── greeter.py         # Classe Greeter con attributi e metodi
├── scripts/
│   ├── test_script.py
│   └── cli_greet.py           # Usa Greeter per salutare da terminale
├── tests/
│   └── test_utils.py          # Test automatici e parametrizzati su Greeter
├── venv/                      # Ambiente virtuale (escluso dal repo)
├── main.py                    # Entry point del progetto (usa Greeter)
├── requirements.txt
└── README.md
```

## 🧰 Requisiti

- Python 3.x
- `venv` per l’ambiente virtuale
- `pytest` per il testing

## ⚙️ Setup del progetto

```bash
git clone ...

cd python_project_lab
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🚀 Esecuzione

### Main:

```bash
PYTHONPATH=src python3 main.py
```

### CLI:

```bash
PYTHONPATH=src python3 scripts/cli_greet.py --name Alessio
```

## 🧪 Testing

```bash
PYTHONPATH=src pytest
```

## 🧠 Concetti chiave introdotti in questo blocco

| Termine             | Significato |
|---------------------|-------------|
| Classe              | Modello per creare oggetti con stato e comportamento |
| Istanza             | Oggetto concreto creato da una classe |
| Attributo           | Variabile legata a un oggetto (es. `self.name`) |
| Metodo              | Funzione definita dentro una classe |
| `__init__`          | Metodo speciale che inizializza l’oggetto alla creazione |
| `self`              | Riferimento all’istanza corrente |
| Incapsulamento      | Pratica di proteggere lo stato interno di un oggetto |
| Refactor            | Ristrutturazione del codice per migliorarne leggibilità e manutenibilità |

## 🎯 Obiettivi didattici del blocco

- Comprendere cosa sono classi, istanze, attributi e metodi
- Iniziare a modellare il comportamento di un oggetto
- Applicare il concetto di incapsulamento e riflessione sul design
- Consolidare il passaggio da funzioni a oggetti mantenendo testabilità