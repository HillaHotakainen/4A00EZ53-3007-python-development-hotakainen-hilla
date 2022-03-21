
def generate_html_page(title, fruit1, fruit2, fruit3, returning_line, many_money, button):
    return f"""<!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>{title}</title>
      </head>
      <body>
        <p>{many_money}</p>
        <img src="{fruit1}"width="100" height="100">
        <img src="{fruit2}"width="100" height="100">
        <img src="{fruit3}"width="100" height="100">
        <p>{returning_line}</p>
        <form action="http://127.0.0.1:5000/slot-machine" method="GET">
        <button>{button}</button>
        </form>
      </body>
    </html>"""