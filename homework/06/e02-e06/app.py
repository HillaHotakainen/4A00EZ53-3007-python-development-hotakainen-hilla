from flask import Flask
import datetime

# create Flask object, give module name
# where to look for resources, like templates or static files
app = Flask(__name__)

# if url is in root
@app.route("/myname")
def hello_world():
    return "<p>Hello, Hilla!</p>"

@app.route("/date")
def date():
    x = datetime.datetime.now()
    return f"<p>{x}</p>"

# start the app if using python3 app.py
if __name__ == "__main__":
    app.run(debug=True)