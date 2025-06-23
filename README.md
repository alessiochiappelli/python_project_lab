# 🐍 python_project_lab

Repository didattica per imparare a organizzare un progetto Python moderno, con struttura modulare, script riutilizzabili e test automatici.

## 📦 Struttura del progetto

```
python_project_lab/
├── src/                 # Codice applicativo
│   └── app/
│       ├── __init__.py
│       └── utils.py
├── scripts/             # Script di supporto
│   └── test_script.py
├── tests/               # Test automatici
│   └── test_utils.py
├── venv/                # Ambiente virtuale (non incluso nel repo)
├── main.py              # Punto di ingresso
├── requirements.txt     # Dipendenze del progetto
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

# Entra nella cartella
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

### Esegui uno script interno:

```bash
PYTHONPATH=src python3 scripts/test_script.py
```

oppure con l’approccio a moduli (se la struttura lo consente):

```bash
python3 -m src.scripts.test_script
```

## 🧪 Esegui i test

```bash
PYTHONPATH=src pytest
```

## 📚 Glossario dei concetti chiave

| Termine        | Significato |
|----------------|-------------|
| Modulo         | File `.py` che contiene funzioni o classi riutilizzabili |
| Package        | Cartella con `__init__.py` che può contenere moduli o altri package |
| Import         | Meccanismo per usare codice scritto altrove |
| PYTHONPATH     | Variabile d’ambiente che dice a Python dove cercare moduli |
| Ambiente virtuale | Spazio isolato per le dipendenze di un progetto |
| Test           | Verifica automatica del comportamento del codice |
| `-m`           | Opzione per eseguire moduli come parte di un package |

## 🧠 Obiettivo didattico

Questa repository è pensata per imparare:

- a organizzare un progetto Python
- a separare codice, script e test
- a usare `PYTHONPATH` in modo corretto
- a scrivere test automatici con `pytest`
