import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <html>
      <head>
        <title>Abhijot's Cloud App</title>
        <style>
          body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 100px;
            background-color: #f2f2f2;
          }
          h1 {
            color: #4CAF50;
          }
          button {
            padding: 10px 20px;
            font-size: 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
          }
          button:hover {
            background-color: #45a049;
          }
        </style>
      </head>
      <body>
        <h1>Hi, this is Abhijot 👩‍💻</h1>
        <p>Welcome to my Flask app deployed on the cloud!</p>
        <button onclick="alert('Hello from Abhijot! 🎉')">Click Me!</button>
      </body>
    </html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

