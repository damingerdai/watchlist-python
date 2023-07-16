# import connexion
from flask import Flask

app = Flask(__name__)

print(app)

@app.route('/')
def hello():
    return 'welcome to My Watchlist!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)
