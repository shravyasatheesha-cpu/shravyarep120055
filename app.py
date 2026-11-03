
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.now()

    return f"""
    <h1>Welcome to Cloud Computing</h1>
    <h2>Current Date and Time</h2>
    <h3>{now.strftime('%d-%m-%Y %H:%M:%S')}</h3>
    """

if __name__ == '__main__':
    app.run()
