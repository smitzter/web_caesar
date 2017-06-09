from flask import Flask
app = Flask(_name_)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return"Hello World"

    app.run()
