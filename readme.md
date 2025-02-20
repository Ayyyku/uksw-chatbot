# UKSW Chatbot

## Instalation

1. clone this repository to your local machine

```bash
git clone https://github.com/vincnx/uksw-chatbot.git
```

2. generate & activate python virtual environment

```bash
python -m venv .venv
```

- activate venv (windows)

```bash
.venv\Scripts\activate
```

- activate venv (linux/mac)

```bash
source .venv/bin/activate
```

3. install the project dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Use the chatbot

1. run the project

```bash
python src/main.py
```

2. open the project in your browser

### Add new intent

You can add new intent by editing the 'data/intents_indo.json' file.

the json format is as follows:

```json
{
  "intents": [
    {
      "tag": "sapaan",
      "patterns": ["Hai", "Halo", "Apa kabar", "Bagaimana kabarmu?"],
      "responses": [
        "Halo",
        "Senang bertemu denganmu",
        "Hai, apakah ada yang bisa saya bantu?"
      ]
    },
    ...
  ]
}
```

- `tag`: the tag / unique identifier of the intent
- `patterns`: the patterns of the intent / question
- `responses`: the responses of the intent / answer

### Train the model

to train the model, you only need to run all the code blocks in src/modelTrainer.ipynb file
