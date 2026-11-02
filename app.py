from flask import Flask, render_template, abort

app = Flask(__name__)

# Usualmente, hubiese elegido una base de datos con sqlite, sin embargo, para algo tan corto y que no necesita escalar, noe s necesariot ampoco
entradas = [
    {
        "id": 1,
        "titulo": "Buritaca, un lugar para desconectarse",
        "resumen": "Por qué esta playa se volvió mi favorita.",
        "imagen": "buritaca.jpg",
        "texto": [
            "Buritaca es de esas playas donde el celular deja de importar. No tiene mucho, y justo por eso me gusta: mar, arena, algo de comer y ya.",
            "Trabajo con clientes todo el día, así que un fin de semana sin notificaciones se nota. Vuelvo a Bogotá con más ganas de volver al computador (o bueno, menos en realidad, y más ganas de quedarme)",
            "Si alguna vez van, lleven efectivo y no esperen mucha señal."
        ]
    },
    {
        "id": 2,
        "titulo": "Baloncesto: lo que me deja la cancha",
        "resumen": "Un deporte que me gusta más de lo que sé jugarlo.",
        "imagen": "baloncesto.jpg",
        "texto": [
            "No soy bueno jugando baloncesto, pero lo veo y lo juego cuando puedo. Lo que más me gusta es que no hay manera de pensar en otra cosa mientras juegas.",
            "Además se parece un poco a trabajar en equipo en la vida real: si nadie pasa el balón, se pierde, así tengas al mejor jugador.",
            "Mi meta para este año es mejorar el tiro libre. Voy lento, pero voy."
        ]
    },
    {
        "id": 3,
        "titulo": "Aprendiendo a programar siendo psicólogo",
        "resumen": "CS50, Flask y varios errores por el camino.",
        "imagen": "cs50.jpg",
        "texto": [
            "Soy psicólogo, así que programar no era lo que se esperaba de mí. Empecé con CS50x de harvardx sólo por explorar alguna otra opción mientras aún buscaba mi camino en la psicología.",
            "Lo que más me costó fue CSS. Todavía no me siento cómodo, y a veces cambio un valor solo para ver qué pasa. Python es un dulcesito fácil de digerir, pero flask llega para enseñarme que no hay que ser tan sobrado.",
            "Este blog entero, lo hice reutilizando algunos conceptos de lo que ya había escrito para mi proyecto final de CS50x. De hecho, el certificado que está en la imagen es mi certificado real."
        ],
        "certificado": "https://courses.edx.org/certificates/4cdfd12d69c9442ea567b7aed0f68fd7"
    }
]


# Este helper conserva el menu a la vista
@app.context_processor
def menu():
    return dict(entradas=entradas)


# Esto costó un poco, pues es la primera evez que utilizo github pages, pero básicamente mantiene la extensión en un formato que pages pueda identificarlas
@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/entrada<int:id>.html")
def entrada(id):
    for e in entradas:
        if e["id"] == id:
            return render_template("entrada.html", e=e)
    abort(404)


if __name__ == "__main__":
    app.run(debug=True)
