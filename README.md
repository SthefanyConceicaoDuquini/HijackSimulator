# Starting the Docker Environment

Make sure Docker Desktop is running.

```bash
cd bgp/bgp-sim-v2
python3 gen_topo.py
docker-compose up -d --build
```

# Starting the Graphical Interface

```bash
cd ../bgp-grafico
python3 -m venv venv
source venv/bin/activate
pip install flask
python app.py
```

# Open the Simulator Web Interface

Open the following URL in your browser:

```text
http://127.0.0.1:5001
```

# Shutting Down Docker

```bash
cd ../bgp-sim-v2
docker-compose down
docker network prune -f
```
