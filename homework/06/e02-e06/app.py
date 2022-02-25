from re import X
from webbrowser import Elinks
from flask import Flask
import datetime
from htmlhelper import generate_html_page
from htmlhelpergame import generate_html_page_game

# create Flask object, give module name
# where to look for resources, like templates or static files
app = Flask(__name__)

# if url is in root
@app.route("/myname")
def hello_world():
    return "<p>Hello, Hilla!</p>"

@app.route("/date")
def date():
    title = "Date"
    content = datetime.datetime.now()
    page = generate_html_page(title, content)
    return page

@app.route("/slot-machine")
def slot_machine():
    import random
    x = random.randint(0,2)
    y = random.randint(0,2)
    z = random.randint(0,2)
    win = ""
    if x == y and x == z:
        win = "YOU WIN"


    fruit_list = ["static/image1.png", "static/image2.png", "static/image3.png"]
    title = "Slot machine"
    fruit1 = fruit_list[x]
    fruit2 = fruit_list[y]
    fruit3 = fruit_list[z]
    page = generate_html_page_game(title, fruit1, fruit2 , fruit3, win)
    return page

# start the app if using python3 app.py
if __name__ == "__main__":
    app.run(debug=True)