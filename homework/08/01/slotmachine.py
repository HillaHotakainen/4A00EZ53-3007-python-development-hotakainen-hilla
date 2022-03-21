from flask import Flask
from htmlhelper import generate_html_page
from flask import make_response
from flask import request

app = Flask(__name__)

@app.route("/slot-machine")
def slot_machine():
    import random
    money = request.cookies.get('money')
    if money == None:
        money = 20
    else:
        money = int(money)
    
    returning_line = ""
    response = make_response(f"<p>{returning_line}</p>")
    response.set_cookie("money", f"{money}")

    many_money = f"You have will have {money}e"
    x = random.randint(0,2)
    y = random.randint(0,2)
    z = random.randint(0,2)
    fruit_list = ["static/image1.png", "static/image2.png", "static/image3.png"]
    fruit1 = fruit_list[x]
    fruit2 = fruit_list[y]
    fruit3 = fruit_list[z]

    title = "Slot machine"
    button = "Play the game"
    if x == y and x == z:
        returning_line = "You win 5e"
        money = int(money) + 5
        page = generate_html_page(title, fruit1, fruit2 , fruit3, returning_line, many_money, button)
        response = make_response(page)
    elif x != y or x != z and money > 0:
        returning_line = "You lost 1e"
        money = int(money) - 1
        page = generate_html_page(title, fruit1, fruit2 , fruit3, returning_line, many_money, button)
        response = make_response(page)
    elif x != y or x != z and money <= 1:
        returning_line = "You run out of money, game over!"
        button = "Restart"
        page = generate_html_page(title, fruit1, fruit2 , fruit3, returning_line, many_money, button)
        response = make_response(page)
        response.delete_cookie("money")
        return response
    
    response.set_cookie("money", f"{money}")
    return response

if __name__ == "__main__":
    app.run(debug=True)