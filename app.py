from flask import Flask, request, render_template
import yaml

app = Flask(__name__)

def load_config():
    with open("config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)
    return config

config = load_config()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    language = request.args.get('language', 'English')
    greeting = config['greetings'].get(language, 'Hello world')
    return greeting

if __name__ == '__main__':
    app.run(host=config['flask']['host'], port=config['flask']['port'], debug=config['flask']['debug'])
