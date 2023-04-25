import pokebase as pb
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == 'POST':
        create = request.form.get("quantidade")
        if not create:
            return render_template("base.html",
                                   error="Escreva o nome de um pokemon")

        create = create.lower()
        poke = pb.pokemon(create)
        try:
            pokelink = pb.SpriteResource('pokemon', poke.id)
            pokename = poke.name.upper()
            pokeimg = pokelink.url
        except:
            return render_template("base.html",
                                   error="Nome de um pokemon existente.")

        return render_template("card-pokemon.html",
                               pokeimg=pokeimg, pokename=pokename)
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)
