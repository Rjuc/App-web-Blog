from flask_frozen import Freezer
from app import app, entradas

# Todo este documento tuvge que leer mucha documentación y  ayuda de IA para entenderlo. "docs" Es necesario para githubpages
app.config["FREEZER_DESTINATION"] = "docs"
app.config["FREEZER_RELATIVE_URLS"] = True

freezer = Freezer(app)


@freezer.register_generator
def entrada():
    for e in entradas:
        yield {"id": e["id"]}


if __name__ == "__main__":
    freezer.freeze()
