from flask import Flask
app = Flask(__name__)

@app.route("/")
x = 5
y = 10
print(x + y)
