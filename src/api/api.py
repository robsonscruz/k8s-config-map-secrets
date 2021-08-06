from flask import Flask, request, Response, jsonify
from json import dumps, loads
import yaml, os

app = Flask('config-map')
app.debug = True
# Load global config
global_config_file = open("../config/api-config.yml")
global_config = yaml.load(global_config_file, Loader=yaml.FullLoader)
# Env
app.config['ENV'] = os.getenv("ENV", "development")
app.config['DB_USERNAME_SECRET'] = os.getenv("DB_USERNAME_SECRET", "not-defined")
app.config['DB_PASSWORD_SECRET'] = os.getenv("DB_PASSWORD_SECRET", "not-defined")

def load_env(environment):
    if environment not in global_config:
        return {"status": "ERROR", "message": "Item '{}' not found".format(environment)}

    return global_config.get(environment)

@app.route('/')
def index():
    return jsonify({"env": app.config['ENV'], "data": load_env(app.config['ENV']), "secrets": {"username": app.config['DB_USERNAME_SECRET'], "password": app.config['DB_PASSWORD_SECRET']}})

@app.route('/env/<string:environment>')
def env(environment):
    status_code = 200
    content = load_env(environment)
    if "status" in content and content["status"] == "ERROR":
        status_code = 400

    return jsonify({"global_env": app.config['ENV'], "local_env": environment, "data": content, "secrets": {"username": app.config['DB_USERNAME_SECRET'], "password": app.config['DB_PASSWORD_SECRET']}}), status_code

if __name__ == '__main__':
    app.run()
