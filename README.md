# 🐍 python_project_lab – Blocco 02: CLI e funzioni riutilizzabili

Estensione del progetto base, dedicata all’introduzione delle interfacce da riga di comando (CLI) in Python.  
In questo branch impariamo a creare script professionali che ricevono input da terminale, usano funzioni modulari e sono completamente testati.

## 📦 Struttura del progetto

```
python_project_lab/
├── src/
│   └── app/
│       ├── __init__.py
│       └── utils.py           # Funzione greet(name) riutilizzabile
├── scripts/
│   ├── test_script.py
│   └── cli_greet.py           # Script CLI eseguibile da terminale
├── tests/
│   └── test_utils.py          # Test parametrizzati su greet()
├── venv/                      # Ambiente virtuale (escluso dal repo)
├── main.py                    # Entry point del progetto
├── requirements.txt
└── README.md
```

## 🧰 Requisiti

- Python 3.x
- `venv` per l’ambiente virtuale
- `pytest` per il testing

## ⚙️ Setup del progetto

```bash
# Clona il progetto
git clone ...

cd python_project_lab

# Crea e attiva l'ambiente virtuale
python3 -m venv venv
source venv/bin/activate  # macOS/Linux

# Installa le dipendenze
pip install -r requirements.txt
```

## 🚀 Esecuzione

### Esegui `main.py`:

```bash
PYTHONPATH=src python3 main.py
```

### Esegui uno script di debug:

```bash
PYTHONPATH=src python3 scripts/test_script.py
```

### 📟 Esecuzione via CLI

Lo script `cli_greet.py` consente di salutare un utente passando il nome da terminale.

```bash
PYTHONPATH=src python3 scripts/cli_greet.py --name Alessio
```

🟢 Output:

```
Ciao, Alessio! Benvenuto nel progetto Python.
```

Puoi visualizzare l’aiuto con:

```bash
python3 scripts/cli_greet.py --help
```

Output:

```
usage: cli_greet.py [-h] --name NAME

Script di saluto personalizzato via terminale.

options:
  -h, --help   show this help message and exit
  --name NAME  Nome della persona da salutare
```

## 🧪 Esegui i test

```bash
PYTHONPATH=src pytest
```

## 📚 Glossario dei concetti chiave

| Termine               | Significato |
|-----------------------|-------------|
| Modulo                | File `.py` che contiene funzioni o classi riutilizzabili |
| Package               | Cartella con `__init__.py` che può contenere moduli o altri package |
| Import                | Meccanismo per usare codice scritto altrove |
| PYTHONPATH            | Variabile d’ambiente che dice a Python dove cercare moduli |
| Ambiente virtuale     | Spazio isolato per le dipendenze di un progetto |
| Test                  | Verifica automatica del comportamento del codice |
| Test parametrizzato   | Test eseguito con input multipli grazie a `@pytest.mark.parametrize` |
| CLI                   | Interfaccia da terminale per eseguire script Python |
| `argparse`            | Modulo Python per gestire gli argomenti da terminale |
| `--help`              | Opzione automatica per mostrare le istruzioni d’uso |
| `-m`                  | Opzione per eseguire moduli come parte di un package |

## 🧠 Obiettivo didattico

Questo branch estende le basi della struttura Python per introdurre:

- uso di `argparse` per creare interfacce CLI professionali
- separazione tra parsing e logica applicativa
- funzioni riutilizzabili e testabili
- test automatizzati su più casi d’uso
