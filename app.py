from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    language = request.args.get('language', 'English')
    greeting = get_greeting(language)
    return greeting

def get_greeting(language):
    greetings = {
        'English': 'Hello world',
        'French': 'Bonjour le monde',
        'Hindi': 'Namastey sansar'
    }
    return greetings.get(language, 'Hello world')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
