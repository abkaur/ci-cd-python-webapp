import os
from flask import Flask

admin_password = os.getenv("ADMIN_PASSWORD", "not-set")
print("Admin Password (from env):", admin_password)

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hi, this is Abhijot. Welcome to my Flask app running in the cloud! 🚀'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
