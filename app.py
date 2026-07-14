<<<<<<< HEAD

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Infrastructure Automation with Monitoring & Self-Healing"

@app.route('/health')
def health():
    return "Application is Healthy"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Infrastructure Automation with Monitoring & Self-Healing"

@app.route('/health')
def health():
    return "Application is Healthy"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> c7c1cf4d96aa3aa57806fae83e335deeb6c244bb
