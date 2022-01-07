from flask import Flask

app = Flask(__name__)

app.secret_key = "Secrets don't make friends!"