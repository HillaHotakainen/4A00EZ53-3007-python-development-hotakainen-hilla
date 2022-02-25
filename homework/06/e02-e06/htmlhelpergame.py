
def generate_html_page_game(title, fruit1, fruit2, fruit3, win):
    return f"""<!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>{title}</title>
      </head>
      <body>
        <img src="{fruit1}"width="100" height="100">
        <img src="{fruit2}"width="100" height="100">
        <img src="{fruit3}"width="100" height="100">
        <p>{win}</p>
      </body>
    </html>"""