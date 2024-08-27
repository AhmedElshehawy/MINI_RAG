# MINI RAG

This is a minimal implementation of the RAG model for question answering.

## Requirements

- Python 3.8

### Install Python using miniconda

1. Download and install Miniconda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)
2. Create a new environment using the following command:

    ```bash
    conda create -n mini-rag python=3.8 pip
    ```

3. Activate the environment:

    ```bash
    conda activate mini-rag
    ```

### Installation

### Install required packages

```bash
pip install -r requirements.txt
```

### Setup the environment variables

```bash
cp .env.example .env
```

Set your enviroment variables in the `.env` file. Like `OPENAI_API_KEY` value.

## Run FastAPI server

```bash
uvicorn --reload --host 0.0.0.0 --port 5000 main:app
```
## Postman collection

Download the postman collection from [here](assets/mini-rag-collection.postman_collection.json)