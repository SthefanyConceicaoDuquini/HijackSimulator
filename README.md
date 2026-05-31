# HijackSimulator

This project can be run entirely from the repository root without moving any folders.

## Requirements

- Docker Desktop running
- Python 3 installed

## Starting the Environment

From the project root, generate the BIRD configuration files and start the containers:

```bash
python3 gen_topo.py
docker compose up -d --build
```

## Starting the Web Interface

Still from the project root, install Flask, and run the application:

```bash
pip install flask
python3 app.py
```

## Opening the Interface

Open this address in your browser:

```text
http://127.0.0.1:5001
```

## Stopping the Environment

To stop the containers:

```bash
docker compose down
```
