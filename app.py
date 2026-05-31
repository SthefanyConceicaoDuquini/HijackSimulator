from flask import Flask, render_template, redirect, url_for
from pathlib import Path
import subprocess

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DOCKER_COMPOSE = ['docker', 'compose']

def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, stderr=subprocess.STDOUT, cwd=BASE_DIR).decode()
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    proto = run_cmd(DOCKER_COMPOSE + ['exec', '-T', 'as1', 'birdc', 'show', 'protocols'])
    route = run_cmd(DOCKER_COMPOSE + ['exec', '-T', 'as1', 'birdc', 'show', 'route'])
    status = 'Established' in proto
    is_hijacked = '1.1.1.1/32' in route
    return render_template('index.html', proto=proto, route=route, status=status, hijacked=is_hijacked)

@app.route('/attack')
def attack():
    # sequestra 1.1.1.1
    run_cmd(DOCKER_COMPOSE + ['exec', '-T', 'as2', 'ip', 'addr', 'add', '1.1.1.1/32', 'dev', 'lo'])
    return redirect(url_for('index'))

@app.route('/cleanup')
def cleanup():
    # limpa o sequestro
    run_cmd(DOCKER_COMPOSE + ['exec', '-T', 'as2', 'ip', 'addr', 'del', '1.1.1.1/32', 'dev', 'lo'])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
